class Square extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {value: this.props.boardValues[this.props.number]}
    this.handleChange = this.handleChange.bind(this);
  }
  
  handleChange(event) {
    console.log('You have changed Game.state.value');
    this.setState({value: event.target.value});
    this.props.boardValues[this.props.number] = Number(event.target.value);
  }
  
  render() {
    // Make array for 1, 2, ...9
    var arrayVal = Array(9);
    for (var i = 1; i < 10; i++) {arrayVal[i] = i}
    return (
      <select
        className="Square"
        value={this.state.value}
        onChange={this.handleChange}>
        <option value="0"></option>
      
        {/* Square renders drop-down    */}
        {arrayVal.map((j) =>
           <option key={j} value={j}>{j}</option>)}
      
      </select>
    );
    
  }
  
}

class Game extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {value: Array(81).fill(0)};
    
    this.handleClickSolve = this.handleClickSolve.bind(this);
    this.handleClickClear = this.handleClickClear.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  
  // Method to solve the board
  handleClickSolve() {
    console.log("You have clicked the Game.handleClickSolve button");
    var boardString = this.state.value.join('')
    console.log(boardString); // log for debug
    // Make ajax call to solve
    $.ajax({
      type: "POST",
      url: "http://www.thejohnconway.com/testing/sudoku/" + boardString,
      cache: false,
      dataType: "json",
      // IF successful
      success: function(data) {
	      var x = data.solution;
	      console.log('x:\n')
	      console.log(x)
	      var x1 = '';
	      var x2 = '';
	      // Place commas
	      for (var i=0; i < x.length; i++) {
	      	x1 += x.charAt(i) + ',';}

	      console.log('x1:\n')
	      console.log(x1)

	      // Place newline chars
	      for (var i=0; i < x1.length; i+=18) {
      		x2 += x1.slice(i, i+18) + '\n';}

      	console.log(x2)
      	alert(x2);

            },

            // If unsuccessful
            error: function(data) {
              alert("Error occured");
              console.log(data);
            }
          });      
        }
  
  // Method to clear the board
  handleClickClear() {
    console.log("You have clicked the Game.handleClickClear button");
    // this.setState({value: Array(81).fill(0)});
    location.reload(true);
  }
  
  handleChange() {
    alert('Something');
  }
  
  render() {
    
    // Make array for 1, 2, ...81
    var arraySquare = Array(81);
    for (var i = 0; i < 81; i++) {arraySquare[i] = i}
    
    // Render the whole game
    return (
      <div className="Game">
        
        {/* Game renders Board */}
        <div className="Board">
          
          {/* Board renders Squares */}
          {arraySquare.map( (i) =>
                           
           <Square 
             key={i}
             number={i}
             boardValues={this.state.value}
             />)}
          
        </div>
        <br></br>
        <div id="buttonDiv">
          <input 
            type="button"
            value="Solve!"
            onClick={this.handleClickSolve}
            className="SolverButton"></input>
          <input 
            type="button"
            value="Clear"
            onClick={this.handleClickClear}
            className="SolverButton"></input>
        </div>
      </div>
    );
  }
  
}

ReactDOM.render(
  <Game />,
  document.getElementById('app')
);
