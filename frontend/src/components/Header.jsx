import { useAuth } from 'react-oidc-context';
import { Link } from 'react-router-dom';
import pawLogo from '/paw-icon.png';
import './Header.css';

export default function Header() {
  const auth = useAuth();

  return (
    <header className="header">
      <div className="logo">
        <img src={pawLogo} className="logo"/>
      </div>
      <nav className="nav">
        <span className="welcome-message">
          {auth.isAuthenticated ? `Logged in as: ${auth.user?.profile.email}` : 'Pet Matcher'}
        </span>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/browse">Browse</Link></li>
          {auth.isAuthenticated ? (
            <li><button onClick={() => auth.signoutRedirect()}>Logout</button></li>
          ) : (
            <li><button onClick={() => auth.signinRedirect()}>Login</button></li>
          )}
        </ul>
      </nav>
    </header>
  )
}
