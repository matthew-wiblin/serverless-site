import { useState, useEffect } from 'react';
import { Anchor } from '@mantine/core';
import cameraLogo from '/camera-icon.png';
import './Header.css';
import { getCurrentUser, signOut } from 'aws-amplify/auth';

export default function Header() {
  const [username, setUsername] = useState(null)

  const pathname = window.location.pathname;

  useEffect(() => { getCurrentUser().then(user => setUsername(user.username)).catch(console.error); }, []);

  return (
    <header className="header">
      <img src={cameraLogo} className="logo" alt="Camera Logo" />
      <div className="tabs-container">
        <Anchor href="/" className={`header-anchor ${pathname === '/' ? 'active' : ''}`}>Home</Anchor>
        <Anchor href="/browse" className={`header-anchor ${pathname === '/browse' ? 'active' : ''}`}>Browse</Anchor>
      </div>
      <div className="auth-container">
        {username ? (
          <>
            <Anchor href='/account' className={`header-anchor ${pathname === '/account' ? 'active' : ''}`}>Account - {username}</Anchor>
            <Anchor onClick={() => { signOut().then(() => window.location.href = '/'); }} className="header-anchor">Sign Out</Anchor>
          </>
        ) : (
          <Anchor href='/login' className={`header-anchor ${pathname === '/login' ? 'active' : ''}`}>Login / Sign Up</Anchor>
        )}
      </div>
    </header>
  );
}
