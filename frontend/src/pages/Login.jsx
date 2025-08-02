import React, { useState } from 'react';
import { signIn } from 'aws-amplify/auth';
import '../aws-config'; // make sure this runs first

export default function Login() {
  const [email, SetEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      await signIn({ email, username, password });
      console.log('Login successful');
    } catch (err) {console.log(err);setError(err)}
  };

  return (
    <div>
      <input placeholder="Email" onChange={e => SetEmail(e.target.value)} />
      <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
      <input placeholder="Password" type="password" onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
      {error && <div>{error}</div>}
    </div>
  );
}
