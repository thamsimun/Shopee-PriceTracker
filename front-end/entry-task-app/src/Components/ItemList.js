import React, {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { FixedSizeList } from 'react-window';
import InfiniteLoader from 'react-window-infinite-loader';
import './ItemList.css';
import PriceLog from '../Components/PriceLog'

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
    height: 400,
    maxWidth: 900,
    backgroundColor: theme.palette.background.paper,
  },
}));


export function ItemList(props) {
    const style = useStyles();
    const itemCount = props.items.length;
    const loadMoreItems = () => {};
    
    const [priceHistory, setPriceHistory] = useState([]);
    const [pricChangeLog, setPriceChangeLog] = useState([]);

    const renderRow = ({index, style}) => {
        if (index < props.items.length) {
            const item = props.items[index];
            return (
                <ListItem 
                    key={index} 
                    style={style} 
                >
                    <ListItemText 
                        primary={`${index + 1} - ${item.item_name}`} 
                        secondary={item.item_id}/>
                    <button 
                        type="show price" 
                        className="btn btn-primary"
                        onClick={() => handlePriceClick(item.item_id)}
                    >View Price Change</button>
                    <button 
                        type="delete" 
                        className="btn btn-primary"
                        onClick={() => handleDelete(item.item_id)}
                    >Delete</button>
                </ListItem>
            )
        }
      
    }

    const handleDelete = (item_id) => {
        const payload = {
            "user" : localStorage.getItem('username'),
            "item_id" : item_id,
        }
        const requestOptions = {
            method: 'POST',
            credentials: 'include',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        }
        fetch(`http://localhost/api/delete-item`, requestOptions)
            .then(response => response.json())
            .then(function (response) {
                if(response.authenticated === -1){
                    console.log("not authenticated, logged out after inactivity");
                    props.showError('not authenticated, logged out after inactivity')
                    alert('Please log in again..');
                    props.redirect();
                } else {
                    props.getItem(props.limit, 0);
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    // const redirectToLogin = () => {
    //     props.updateTitle('Login')
    //     props.history.push('/login'); 
    // }

    //edit this
    const handlePriceClick = (itemid) => {
        console.log("getting price log for ", itemid)
        fetch(`/api/get-price-change-log?item_id=${itemid}`, {credentials: 'include'})
        .then(response => response.json())
        .then(function (response) {
            if(response.authenticated === -1) {
                alert("You are not logged in. Please log in again.");
                //test if this works
                props.redirect()
            } else {
                console.log(response.data)
                setPriceHistory(response.data)
            }
        })
        .catch(function(error) {
            console.log(error);
        });
    }

    if(props.items.length) {
        return(
        <div>
            <header>Items Added</header>
            <div className={style.root}>
                <InfiniteLoader isItemLoaded={index => index < props.items.length} itemCount={itemCount} loadMoreItems={loadMoreItems}>
                    {({ onItemsRendered, ref }) => (
                        <FixedSizeList
                        height={400} 
                        width={900} 
                        itemSize={75}
                        itemCount={itemCount} 
                        onItemsRendered={onItemsRendered}
                        ref={ref}
                        >{renderRow}
                        </FixedSizeList>
                    )}
                </InfiniteLoader>
                <button 
                    type="load more" 
                    className="btn btn-primary"
                    onClick={props.loadItem}
                >Load More</button>
            </div>
            <div className='PriceChange'>
                <PriceLog pricelog={priceHistory} redirect={props.redirect}></PriceLog>
            </div>
        </div>

        );
    } else {
        return(
            <div></div>
        )
    }
}
