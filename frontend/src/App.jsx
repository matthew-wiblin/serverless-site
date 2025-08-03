import { useAuth } from 'react-oidc-context';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import '@mantine/core/styles.css';
import { MantineProvider } from '@mantine/core';
import Header from './components/Header';
import Home from './pages/Home';
import Browse from './pages/Browse';
import Account from './pages/Account';
import Login from './pages/Login';

function App() {
  const auth = useAuth();

  return (
    <MantineProvider>
      <Header/>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/browse' element={<Browse/>} />
        <Route path='/account' element={<Account/>} />
        <Route path='/login' element={<Login/>} />
      </Routes>
    </MantineProvider>
  )
}

export default App
