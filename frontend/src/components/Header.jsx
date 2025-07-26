import { useAuth } from 'react-oidc-context';
import { useState, useEffect } from 'react';
import { Anchor } from '@mantine/core';
import cameraLogo from '/camera-icon.png';
import './Header.css';

export default function Header() {
  const auth = useAuth();
  const [username, setUsername] = useState('');
  const pathname = window.location.pathname;

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
    <header className="header">
      <img src={cameraLogo} className="logo" alt="Camera Logo" />
      <div className="tabs-container">
        <Anchor href="/" className={`header-anchor ${pathname === '/' ? 'active' : ''}`}>Home</Anchor>
        <Anchor href="/browse" className={`header-anchor ${pathname === '/browse' ? 'active' : ''}`}>Browse</Anchor>
      </div>
      <div className="auth-container">
        {auth.isAuthenticated ? (
          <>
            <Anchor onClick={signOutRedirect} className="header-anchor">Logout</Anchor>
            <p className="header-text">{username}</p>
          </>
        ) : (
          <Anchor onClick={() => auth.signinRedirect()} className="header-anchor">Login</Anchor>
        )}
      </div>
    </header>
  );
}
