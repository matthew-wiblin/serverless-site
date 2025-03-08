import { useAuth } from 'react-oidc-context';
import { Link } from 'react-router-dom';
import pawLogo from '/paw-icon.png';
import './Header.css';

export default function Header() {
  const auth = useAuth();
  console.log('auth state = ', auth)

  const signOutRedirect = () => {
    const clientId = "6q9c36eaqodo1e612mel9rf3ho";
    const logoutUri = "http://localhost:5173";
    const cognitoDomain = "https://eu-west-2j2arzdszl.auth.eu-west-2.amazoncognito.com";
    window.location.href = `${cognitoDomain}/logout?client_id=${clientId}&logout_uri=${encodeURIComponent(logoutUri)}`;
    auth.removeUser();
  };

  return (
    <header className="header">
      <div className="logo">
        <img src={pawLogo} className="logo-img" alt="Paw Logo" />
        <p className="logo-text">Pet Matcher</p>
      </div>
      <nav className="nav">
        <Link to="/home">
          <button className="nav-btn">Home</button>
        </Link>
        <Link to="/browse">
          <button className="nav-btn">Browse</button>
        </Link>
        {auth.isAuthenticated ? (
          <button className="nav-auth-btn" onClick={signOutRedirect}>Logout</button>
        ) : (
          <button className="nav-auth-btn" onClick={() => auth.signinRedirect()}>Login</button>
        )}
      </nav>
    </header>
  );
}
