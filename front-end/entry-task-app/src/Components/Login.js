import React, {useState, useContext} from 'react';
import './Login.css';
import { withRouter } from "react-router-dom";


function LoginPage(props) {

  const [state , setState] = useState({
    user : "",
    password : "",
    successMessage: null
  })
  const handleChange = (e) => {
    const {id , value} = e.target   
    setState(prevState => ({
        ...prevState,
        [id] : value
    }))
  }
  const handleSubmitClick = (e) => {
    e.preventDefault();
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
    fetch(`/api/sign-in`, requestOptions)
      .then(response => response.json())
      .then(function (response) {
        console.log(response);
        if(response.incorrect === -1){
          console.log("Sign in successful");
          setState(prevState => ({
            ...prevState,
            'successMessage' : 'Sign in successful. Redirecting to home page..'
          }))
          redirectToHome();
          props.showError(null)
        } else{
          console.log("Username does not exists or password is incorrect");
          props.showError('Username does not exists or password is incorrect');
          alert('Username does not exists or password is incorrect')
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  const redirectToHome = () => {
      props.updateTitle('Home')
      props.setUser(state.user)
      localStorage.setItem('username', state.user)
      console.log(props.user)
      props.history.push('/home');
  }

  const redirectHome = () => {
      props.updateTitle('Home');
      props.history.push('/home');
  }
  const redirectToRegister = () => {
      props.history.push('/register'); 
      props.updateTitle('Register');
  }

  const checkLogin = () => {
    fetch(`/api/signed-in`, {credentials: 'include'})
        .then(response => response.json())
        .then(function (response) {
            if(response.authenticated === 1) {
                alert("You are logged in already. Redirecting to home page...");
                console.log(localStorage.getItem('username'))
                redirectHome();
            }
        })
        .catch(function(error) {
            console.log(error);
        });
}

  React.useEffect(checkLogin, [])

  return(

    <div className="card col-12 col-lg-4 login-card mt-2 hv-center">
        <form>
            <div className="form-group text-left">
            <label htmlFor="exampleInputUser1">Username</label>
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
            <div className="form-check">
            </div>
            <button 
                type="submit" 
                className="btn btn-primary"
                onClick={handleSubmitClick}
            >Submit</button>
        </form>
        <div className="alert alert-success mt-2" style={{display: state.successMessage ? 'block' : 'none' }} role="alert">
            {state.successMessage}
        </div>
        <div className="registerMessage">
            <span>Dont have an account? </span>
            <span className="loginText" onClick={() => redirectToRegister()}>Register</span> 
        </div>
    </div>

  )
}

export default withRouter(LoginPage);