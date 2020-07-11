import React, {useState} from 'react';
// import PropTypes from 'prop-types';
// import { makeStyles } from '@material-ui/core/styles';
// import ListItem from '@material-ui/core/ListItem';
// import ListItemText from '@material-ui/core/ListItemText';
// import { FixedSizeList } from 'react-window';
// import InfiniteLoader from 'react-window-infinite-loader';
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  } from 'recharts';

import './ItemList.css';
import moment from 'moment';


// const useStyles = makeStyles((theme) => ({
//   root: {
//     width: '100%',
//     height: 400,
//     maxWidth: 700,
//     backgroundColor: theme.palette.background.paper,
//   },
// }));

function PriceLog(props) {

    console.log(props.pricelog)

    let data = props.pricelog.map(
        item => (
            {   
                time: item.time,
                price: item.price/100000
                
            }
        )
    )

    console.log(moment.unix(5816585339).format('D-ha'))


    console.log(data)


    if(props.pricelog.length > 0) {
        return (
            // <div>
            //     <header>Price Change Graph</header>
            //     <XYPlot width={900} height={600} xType="time" margin={{left: 100}}>
            //         <HorizontalGridLines style={{stroke: '#B7E9ED'}} />
            //         <VerticalGridLines style={{stroke: '#B7E9ED'}} />
            //         <XAxis
            //             title="Datetime"
            //             style={{
            //                 line: {stroke: '#ADDDE1'},
            //                 ticks: {stroke: '#ADDDE1'},
            //                 text: {stroke: 'none', fill: '#6b6b76', fontWeight: 600}
            //             }}
            //             tickformat = {(unixTime) => new Date(unixTime).toUTCString()}
            //         />
            //         <YAxis title="Price"/>
            //         <LineMarkSeries
            //             data={data}
            //             lineStyle={{stroke:"blue" ,fill: 'none'}}
            //             markStyle={{stroke:"blue"}}
            //         />
            //     </XYPlot>
            // </div>
            <div>
                <header>Price Change Graph</header>
                <div style={{fontSize: 14}}>
                    <LineChart
                        width={900}
                        height={500}
                        data={data}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis 
                            dataKey="time" 
                            tickFormatter = {(unixTime) => moment.unix(unixTime).format('DD-MM/ha')}
                        />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line dataKey="price" stroke="#8884d8" activeDot={{ r: 10 }} />
                    </LineChart>
                </div>  
            </div>  

        )
    } else {
        return null
    }
}

export default PriceLog;