import { useState } from 'react';
import { signIn, signUp } from 'aws-amplify/auth';
import '../aws-config';
import {Container, TextInput, PasswordInput, Button, Paper, Title, Stack, Notification, Tabs} from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';

export default function Login() {
  const [type, setType] = useState('login');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const [loading, { toggle }] = useDisclosure();

  const handleAuth = async () => { // seperate out into login function and signup
    try {
      toggle()
      if (type === 'login') {
        await signIn({ username, password });
      } else {
        await signUp({ // sign up not working correctly need to add verfication to email
          username,
          password,
          options: { userAttributes: { email } },
        });
      }
      window.location.href = '/';
    } catch (err) {
      console.error(err);
      setError(err.message || `${type} failed`);
    }
    toggle()
  };

  return ( // centralise the tabs somewhere 
    <Container size={420} my={40}>
      <Title align="center" mb={20}>Welcome</Title>
      <Paper withBorder shadow="md" p={30} radius="md">
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
          <Button loading={loading} fullWidth onClick={handleAuth}>{type === 'login' ? 'Login' : 'Sign Up'}</Button>
          {error && (
            <Notification color="red" withCloseButton={false} withBorder={true}>
              {error}
            </Notification>
          )}
        </Stack>
      </Paper>
    </Container>
  );
}
