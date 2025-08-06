import { useState } from 'react';
import { signIn, signUp, confirmSignUp, resendSignUpCode } from 'aws-amplify/auth';
import '../aws-config';
import {Container, TextInput, PasswordInput, Button, Paper, Title, Stack, Notification, Tabs} from '@mantine/core';

export default function Login() {
  const [type, setType] = useState('login');
  const [step, setStep] = useState('form');
  const [loading, setLoading] = useState(false);
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmationCode, setConfirmationCode] = useState('');
  const [error, setError] = useState('');

  const handleAuth = async () => {
    setError('')
    try {
      setLoading(true)
      if (type === 'login') {
        const result = await signIn({ username, password });
        if (result.isSignedIn === false) {setStep('confirm'); resendSignUpCode({ username: username })}
        if (result.isSignedIn === true) {window.location.href = '/account'}
      } else {
        const { isSignUpComplete, userId, nextStep } = await signUp({username, password, options: { userAttributes: { email } }});
        if (nextStep?.signUpStep === 'CONFIRM_SIGN_UP') {setStep('confirm')}
        else {window.location.href = '/';}
      }
    } catch (err) {setError(err.message || `${type} failed`)}
    setLoading(false)
  };

  const handleConfirm = async () => {
    setError('');
    setLoading(true)
    try {
      await confirmSignUp({ username, confirmationCode });
      await signIn({ username, password });
      window.location.href = '/';
    } catch (err) {
      setError(err.message || 'Confirmation failed');
    }
    setLoading(false)
  };

  return (
    <Container size={420} my={40}>
      <Title align="center" mb={20}>Welcome</Title>
      <Paper withBorder shadow="md" p={30} radius="md">
        {step === 'form' && (
          <>
            <Tabs value={type} onChange={(val) => setType(val)} mb="md">
              <Tabs.List grow>
                <Tabs.Tab value="login">Login</Tabs.Tab>
                <Tabs.Tab value="signup">Sign Up</Tabs.Tab>
              </Tabs.List>
            </Tabs>
            <Stack>
              {type === 'signup' && (
                <TextInput
                  label="Email"
                  placeholder="you@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.currentTarget.value)}
                />
              )}
              <TextInput
                label="Username"
                placeholder="yourusername"
                value={username}
                onChange={(e) => setUsername(e.currentTarget.value)}
              />
              <PasswordInput
                label="Password"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.currentTarget.value)}
              />
              <Button loading={loading} fullWidth onClick={handleAuth}>
                {type === 'login' ? 'Login' : 'Sign Up'}
              </Button>
              {error && (
                <Notification color="red" withCloseButton={false} withBorder={true}>
                  {error}
                </Notification>
              )}
            </Stack>
          </>
        )}
        {step === 'confirm' && (
          <Stack>
            <TextInput
              label="Confirmation Code"
              placeholder="Enter the code sent to your email"
              value={confirmationCode}
              onChange={(e) => setConfirmationCode(e.currentTarget.value)}
            />
            <Button loading={loading} fullWidth onClick={handleConfirm}>
              Confirm Account
            </Button>
            {error && (
              <Notification color="red" withCloseButton={false} withBorder={true}>
                {error}
              </Notification>
            )}
          </Stack>
        )}
      </Paper>
    </Container>
  );
}
