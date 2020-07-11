import React, {useState} from 'react';
import {useContext} from 'react';
import { withRouter } from "react-router-dom";
import './Home.css';
import {ItemList} from '../Components/ItemList';

function Home(props) {

    const [state , setState] = useState({
        user : "",
        url : "",
        successMessage: null
      })

    const [items, setItems] = useState([]);
    const limit = 10;
    const initialOffset = 0;
    const [currOffset, setCurrOffset] = useState(0);


    const handleChange = (e) => {
        const {id , value} = e.target   
        setState(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    const handleAddClick = (e) => {
        //IT WORKSSS
        e.preventDefault();
        console.log(localStorage.getItem('username'))
        if (!localStorage.getItem('username')) {
            alert('not logged in')
            redirectToLogin()
        } else {
            setState(prevState => ({
                ...prevState,
                'user' : localStorage.getItem('username')
            }))
            //parse url
            let url_tokens = state.url.split(".")
            console.log(url_tokens);
            console.log(url_tokens[url_tokens.length-1]);
            console.log(url_tokens[url_tokens.length-2]);
            if (url_tokens.length >= 2) {
                // setState(prevState => ({
                //     ...prevState,
                //     'item' : url_tokens[url_tokens.length-1]
                // }))
                // setState(prevState => ({
                //     ...prevState,
                //     'shop' : url_tokens[url_tokens.length-2]
                // }))
                // console.log(state.item);
                // console.log(state.shop);
                const payload={
                    "user":localStorage.getItem('username'),
                    "item_id":parseInt(url_tokens[url_tokens.length-1], 10),
                    "shop_id":parseInt(url_tokens[url_tokens.length-2], 10),
                }
                const requestOptions = {
                    method: 'POST',
                    credentials: 'include',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(payload)
                  }
                fetch(`/api/add-item`, requestOptions)
                    .then(response => response.json())
                    .then(function (response) {
                        console.log(response);
                        if(response.authenticated === -1){
                            console.log("not authenticated, logged out after inactivity");
                            props.showError('not authenticated, logged out after inactivity')
                            alert('Please log in again..');
                            redirectToLogin();
                        } else if(response.notfound === 1){
                            console.log("item not found in shopee");
                            props.showError('item not found in shopee');
                            alert('item not found in shopee');
                        } else if(response.duplicate === 1){
                            console.log("item exists in your tracker already")
                            props.showError('item exists in your tracker already')
                            alert('item exists in your tracker already')
                        } else{
                            setState(prevState => ({
                                ...prevState,
                                'successMessage' : 'successfully added item'
                            }))
                            alert('Successfully added item!')
                            getItems(limit, initialOffset);
                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
    
                
            } else {
                alert('Incorrect url')
            }
        }
        

    }

    const redirectToLogin = () => {
        props.updateTitle('Login')
        props.history.push('/login'); 
    }

    const redirectToHome = () => {
        props.updateTitle('Home')
        props.history.push('/home'); 
    }

    const checkLogin = () => {
        fetch(`/api/signed-in`, {credentials: 'include'})
            .then(response => response.json())
            .then(function (response) {
                if(response.authenticated === -1) {
                    alert("You are logged out. Please log in again.");
                    redirectToLogin()
                }
            })
            .catch(function(error) {
                console.log(error);
            });
    }

    const handlelogout = (e) => {
        e.preventDefault();
        fetch(`/api/log-out`, {method:'POST', credentials: 'include'})
            .then(response => response.json())
            .then(function (response){
                console.log(response)
                localStorage.setItem('username', null)
                redirectToLogin()
            })
            .catch(function(error) {
                console.log(error);
            });
    }

    const getItems = (limit, offset) => {
        const username = localStorage.getItem('username')
        setCurrOffset(offset+limit)
        console.log(username)
        fetch(`/api/item-list?username=${username}&limit=${limit}&offset=${offset}`, {credentials: 'include'})
            .then(response => response.json())
            .then(function (response){
                if (response.authenticated === -1) {
                    alert("You are logged out. Plese log in again.");
                    redirectToLogin()
                } else if (response.empty === 1) {
                    setItems([])
                    console.log(items)
                } else {
                    console.log(response.data);
                    setItems(response.data);
                }

            })
            .catch(function(error) {
                console.log(error);
            });
    }

    const getMoreItems = () => {
        const username = localStorage.getItem('username')
        setCurrOffset(currOffset+limit)
        console.log(username)
        console.log("curroffset",currOffset)
        fetch(`/api/item-list?username=${username}&limit=${limit}&offset=${currOffset}`, {credentials: 'include'})
            .then(response => response.json())
            .then(function (response){
                if (response.authenticated === -1) {
                    alert("You are logged out. Plese log in again.");
                    redirectToLogin()
                } else if (response.empty === 1) {
                    console.log(items)
                } else {
                    console.log(response.data);
                    let arr = items.concat(response.data)
                    setItems(arr)
                    let count = response.data.length;
                }

            })
            .catch(function(error) {
                console.log(error);
            });
    }

    React.useEffect(checkLogin, []);
    React.useEffect(() => getItems(limit, initialOffset), []);

    return(
        <div className="Home">
            <div className="logout">
                <button 
                    type="logout" 
                    className="btn btn-primary"
                    onClick={handlelogout}
                >Logout</button>
            </div>
            <div className="AddItemUrl">
                <form>
                    <div className="form-group text-left">
                    <label>Item URL to track</label>
                    <input type="Item url" 
                        className="form-control" 
                        id="url" 
                        placeholder="Enter item url" 
                        value={state.url}
                        onChange={handleChange}
                    />
                    </div>
                    <button 
                        type="addtotrack" 
                        className="btn btn-primary"
                        onClick={handleAddClick}
                    >Add</button>
                </form>
            </div>
            <div className="ItemList">
                <ItemList items={items} redirect={redirectToLogin} loadItem={getMoreItems} currOffset={currOffset} limit={limit} getItem={getItems}></ItemList>
            </div>
        </div>
        
    );
}

export default withRouter(Home);