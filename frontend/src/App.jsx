import { useAuth } from 'react-oidc-context';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Home from './pages/Home';
import Browse from './pages/Browse';

function App() {
  const auth = useAuth();

  return (
    <>
    <Header/>
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/browse' element={<Browse/>} />
    </Routes>
    </>
  )
}

export default App


// if (auth.isLoading) {
//   return <div>Loading...</div>;
// }

// if (auth.error) {
//   return <div>Encountering error... {auth.error.message}</div>;
// }


{/* <div>
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
</div> */}