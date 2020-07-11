import React, {useState} from 'react';
import './App.css';
import RegisterPage from './Components/Register';
import LoginPage from './Components/Login';
import Header from './Components/Header';
import Home from './Components/Home';
import WelcomePage from './Components/Welcome';

import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";


function App() {

  const [title, updateTitle] = useState("Login");
  const [errorMessage, updateErrorMessage] = useState(null);
  const [user, setUser] = useState(null);

  return (

    <Router>
    <div className="App">
      <Header title={title}/>
        <div className="container d-flex align-items-center flex-column">
          <Switch>
            <Route path="/" exact={true}>
              <LoginPage showError={updateErrorMessage} updateTitle={updateTitle} setUser={setUser} user={user}/>
            </Route>
            <Route path="/register">
              <RegisterPage showError={updateErrorMessage} updateTitle={updateTitle} setUser={setUser} user={user}/>
            </Route>
            <Route path="/login">
              <LoginPage showError={updateErrorMessage} updateTitle={updateTitle} setUser={setUser} user={user}/>
            </Route>
            <Route path="/home">
              <Home showError={updateErrorMessage} updateTitle={updateTitle} setUser={setUser} user={user}/>
            </Route>
          </Switch>
        </div>
    </div>
    </Router>

  );  
}

export default App;