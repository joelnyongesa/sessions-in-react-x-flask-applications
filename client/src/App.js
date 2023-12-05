import Login from './components/Login';
import Home from './components/Home';
import './App.css';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
        <Routes>
          <Route path='/' element={<Home />}  />
          <Route path='/login' element={<Login />} />
        </Routes>
    </div>
  );
}

export default App;
