import React from 'react';
import ReactDOM from 'react-dom'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'
import 'bootstrap/dist/css/bootstrap.min.css'
import './App.css'
//let HtmlToReactParser = require('html-to-react').Parser
//let iGrid = mGrid(10,10);


function Test() {
    // let newNodeClass = null;
    // let newNode = null;
    // let currentArrayRow = [];
    // let nodes = {};
    // let points = [];
    // let currTable = "<table>";
    // for (let y = 0; y < 10; y++) {
    //     console.log("TEST")
    //     let row = '<tr id="row' + y + '">';
    //     let currentArrayRow = [];
    //     for (let x = 0; x < 10; x++) {
    //         let newNodeId = toString(y-x), newNodeClass, newNode;
    //         newNode = newNodeId + newNodeClass;
    //         currentArrayRow.push(newNode);
    //         row += '<td id="' + newNodeId + '" class="' + newNodeClass + '"></td>';
    //         nodes[toString(newNodeId)] = newNode;
    //     }
    //     points.push(currentArrayRow);
    //     currTable += row + '</tr>';

    // }
    // currTable += '</table>'
    // console.log(currTable);
    // let htmltoreact = new HtmlToReactParser();
    // let arshia = htmltoreact.parse(currTable);
    return (<h1>He</h1>);
}
// function App(width, height) {

//     let rows = []
//     let cols = []
//     for(let y = 0; y < width.width; y++){
//         rows.push(y.toString())
//         console.log(y)
//     }
//     for(let x = 0; x < width.height; x++){
//         cols.push(x.toString())
//     }
//     // const rows = ['1', '2', '3', '4', '5','6','7','8']
//     // const cols = ['a', 'b', 'c', 'd','e']
//     console.log(rows);
//     return (
//             <div className = "App">
//                 <Container className="bigBox">
//                     {rows.map(r => <Row className="border" id={r}>
//                         {cols.map(c => <Col className="border" id={r+c}>{r+c}</Col>)}
//                     </Row>)}
//                 </Container>
//     </div>
// );
// }
// ReactDOM.render(<App width={20} height={20}/>, document.getElementById("root"));
ReactDOM.render(<p>HII</p>, document.getElementById("root"));
export default Test;