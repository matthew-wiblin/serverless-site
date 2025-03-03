import pawLogo from '/paw-icon.svg';
import { useAuth } from "react-oidc-context";
import './App.css';

function App() {
  const auth = useAuth();

  const signOutRedirect = () => {
    const clientId = "6q9c36eaqodo1e612mel9rf3ho";
    const logoutUri = "http://localhost:5173";
    const cognitoDomain = "https://eu-west-2j2arzdszl.auth.eu-west-2.amazoncognito.com";
    window.location.href = `${cognitoDomain}/logout?client_id=${clientId}&logout_uri=${encodeURIComponent(logoutUri)}`;
  };

  if (auth.isLoading) {
    return <div>Loading...</div>;
  }

  if (auth.error) {
    return <div>Encountering error... {auth.error.message}</div>;
  }

  // if (auth.isAuthenticated) {
  //   return (
  //     <div>
  //       <pre> Hello: {auth.user?.profile.email} </pre>
  //       <pre> ID Token: {auth.user?.id_token} </pre>
  //       <pre> Access Token: {auth.user?.access_token} </pre>
  //       <pre> Refresh Token: {auth.user?.refresh_token} </pre>

  //       <button onClick={() => auth.removeUser()}>Sign out</button>
  //     </div>
  //   );
  // }
  return (
    <>
      <div>
        <a><img src={pawLogo} className="logo"/><h1>Paw Match</h1></a>
      </div>
      <div>
      {auth.isAuthenticated ? (
        <div>
          <pre>Hello: {auth.user?.profile.email}</pre>
          <pre>ID Token: {auth.user?.id_token}</pre>
          <pre>Access Token: {auth.user?.access_token}</pre>
          <pre>Refresh Token: {auth.user?.refresh_token}</pre>
        </div>
      ) : (
        <div> not authenticated </div>
      ) }
      <br /><br />
      <button onClick={() => auth.signinRedirect()}>Sign in</button>
      <button onClick={() => signOutRedirect()}>Sign out</button>
      </div>
    </>
  )
}

export default App
