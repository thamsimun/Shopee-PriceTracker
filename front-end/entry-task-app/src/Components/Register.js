import React, {useState} from 'react';
import './Register.css';
import { withRouter } from "react-router-dom";

function RegisterPage(props) {
  const [state , setState] = useState({
      user : "",
      password : "",
      confirmPassword: "",
      successMessage: null
  })
  const sendDetailsToServer = () => {
    if(state.user.length && state.password.length) {
      props.showError(null);
      const payload={
          "user":state.user,
          "password":state.password,
      }
      const requestOptions = {
        method: 'POST',
        credentials: 'include',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      }
      fetch(`/api/sign-up`, requestOptions)
        .then(response => response.json())
        .then(function (response) {
          console.log(response);
          if(response.duplicate === -1){
            console.log("Sign up successful");
            setState(prevState => ({
              ...prevState,
              'successMessage' : 'Sign up successful. Redirecting to log in page..'
            }))
            redirectToLogin();
            props.showError(null)
          } else{
            console.log("Username exists already");
            props.showError('Username already exists.');
            alert('Username already exists.')
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    } else {
      props.showError('Please enter valid username and password')
    }
  }
  const redirectToHome = () => {
    props.updateTitle('Home')
    props.history.push('/home');
  }
  const redirectToLogin = () => {
    props.updateTitle('Login')
    props.history.push('/login'); 
  }
  const handleChange = (e) => {
      const {id , value} = e.target   
      setState(prevState => ({
          ...prevState,
          [id] : value
      }))
  }
  const handleSubmitClick = (e) => {
    e.preventDefault();
    if(state.password === state.confirmPassword) {
        sendDetailsToServer()    
    } else {
        props.showError('Passwords do not match');
    }
  }
  return(
    <div className="card col-12 col-lg-4 login-card mt-2 hv-center">
      <form>
        <div className="form-group text-left">
          <label htmlFor="exampleInputUserName1">Username</label>
          <input type="username" 
            className="form-control" 
            id="user" 
            placeholder="Enter username" 
            value={state.user}
            onChange={handleChange}
          />
        </div>
        <div className="form-group text-left">
          <label htmlFor="exampleInputPassword1">Password</label>
          <input type="password" 
            className="form-control" 
            id="password" 
            placeholder="Password"
            value={state.password}
            onChange={handleChange} 
          />
        </div>
        <div className="form-group text-left">
          <label htmlFor="exampleInputPassword1">Confirm Password</label>
          <input type="password" 
              className="form-control" 
              id="confirmPassword" 
              placeholder="Confirm Password"
              value={state.confirmPassword}
              onChange={handleChange} 
          />
        </div>
        <button 
            type="submit" 
            className="btn btn-primary"
            onClick={handleSubmitClick}
        >
            Register
        </button>
      </form>
      <div className="alert alert-success mt-2" style={{display: state.successMessage ? 'block' : 'none' }} role="alert">
        {state.successMessage}
      </div>
      <div className="mt-2">
        <span>Already have an account? </span>
        <span className="loginText" onClick={() => redirectToLogin()}>Login here</span> 
      </div>
    </div>
  )
}

export default withRouter(RegisterPage);
