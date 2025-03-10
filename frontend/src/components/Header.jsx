import { useAuth } from 'react-oidc-context';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import pawLogo from '/paw-icon.png';
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
      <nav>
        <div className='logo-div'>
          <Link to='/'><img src={pawLogo} className="logo" alt="Paw Logo" /></Link>
          <p className="header-text">Pet Matcher</p>
        </div>
        <div className='buttons-div'>
            <Link to='/'><button>Home</button></Link>
            <Link to='/browse'><button>Browse</button></Link>
            {auth.isAuthenticated ? (
              <>
              <button className='nav-auth-btn' onClick={signOutRedirect}>Logout</button>
              <p className="header-text">{username}</p>
              </>
            ) : (
              <button className='nav-auth-btn' onClick={() => auth.signinRedirect()}>Login</button>
            )}
        </div>
      </nav>
    </header>
  );
}
