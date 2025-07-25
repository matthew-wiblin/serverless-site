import { useAuth } from 'react-oidc-context';
import { useState, useEffect } from 'react';
import { Anchor, Group } from '@mantine/core';
import cameraLogo from '/camera-icon.png';
import './Header.css';

export default function Header() {
  const auth = useAuth();
  const [username, setUsername] = useState('');

  useEffect(() => {
    try {setUsername(auth.user?.profile["cognito:username"]);}
    catch (error) {console.log(error)}
  }, [auth]);

  const signOutRedirect = () => {
    const clientId = "6q9c36eaqodo1e612mel9rf3ho";
    const logoutUri = "http://localhost:5173";
    const cognitoDomain = "https://eu-west-2j2arzdszl.auth.eu-west-2.amazoncognito.com";
    window.location.href = `${cognitoDomain}/logout?client_id=${clientId}&logout_uri=${encodeURIComponent(logoutUri)}`;
    auth.removeUser();
  };

  return (
    <header className='header'>
      <Group>
        <img src={cameraLogo} className="logo" alt="Camera Logo" style={{ width: '50px' }}/>
        <Anchor href='/'>Home</Anchor>
        <Anchor href='/browse'>Browse</Anchor>
        {auth.isAuthenticated ? (
          <>
          <Anchor onClick={signOutRedirect}>Logout</Anchor>
          <p className="header-text" style={{ fontSize: 18, color: '#000', fontWeight: 'bold', margin: 0 }}>{username}</p>
          </>
        ) : (
          <Anchor onClick={() => {auth.signinRedirect()}}>Login</Anchor>
        )}
      </Group>
    </header>
  );
}
