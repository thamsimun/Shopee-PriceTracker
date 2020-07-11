import React from 'react';
function WelcomePage(props) {
    props.updateTitle('Welcome to Shopee Price Tracker');
    return(
        <div className="mt-2">
            Home page content
        </div>
    )
}

export default WelcomePage;