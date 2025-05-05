import { useAuth } from 'react-oidc-context';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import '@mantine/core/styles.css';
import { MantineProvider } from '@mantine/core';
import Header from './components/Header';
import Home from './pages/Home';
import Browse from './pages/Browse';

function App() {
  const auth = useAuth();

  return (
    <MantineProvider>
      <Header/>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/browse' element={<Browse/>} />
      </Routes>
    </MantineProvider>
  )
}

export default App
