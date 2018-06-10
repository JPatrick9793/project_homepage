class Square extends React.Component {
  // Render components
  render() {
    // Make array for 1, 2, ...9
    var arrayVal = Array(9);
    for (var i = 1; i < 10; i++) {
      arrayVal[i] = i;
    }
    return (
      <select
        className="Square"
        name={this.props.number}
        value={this.props.boardValues[this.props.number]}
        onChange={this.props.onChange}
      >
        <option value="0" />

        {/* Square renders drop-down    */}
        {arrayVal.map(j => (
          <option key={j} value={j}>
            {j}
          </option>
        ))}
      </select>
    );
  }
}

class Game extends React.Component {
  // Constructor
  constructor(props) {
    super(props);
    this.state = { value: Array(81).fill(0) };

    this.handleClickSolve = this.handleClickSolve.bind(this);
    this.handleClickClear = this.handleClickClear.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  // Method to solve the board
  handleClickSolve() {
    // log for debug
    var boardString = this.state.value.join("");
    console.log(boardString);
    // Make ajax call to solve
    var self = this;
    $.ajax({
      type: "POST",
      url: "http://www.thejohnconway.com/testing/sudoku/" + boardString,
      cache: false,
      dataType: "json",
      // IF successful
      success: function(data) {
        // Log for debug
        console.log("Call Successful...");
        console.log(data.solution);
        // convert string to array
        let arrayString = data.solution.split("");
        let arrayNum = Array(81);
        // convert string array to numbers
        for (let i = 0; i < arrayString.length; i++) {
          let x = arrayString[i];
          arrayNum[i] = Number(x);
        }
        // Log it for debug
        console.log(arrayNum);
        // Update state value
        self.setState({ value: arrayNum });
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
    this.setState({ value: Array(81).fill(0) });
  }

  // Method to update the state.value array
  handleChange(event) {
    var newValues = this.state.value;
    newValues[event.target.name] = event.target.value;
    this.setState({ value: newValues });
  }

  // Render Components
  render() {
    // Make array for 1, 2, ...81
    var arraySquare = Array(81);
    for (var i = 0; i < 81; i++) {
      arraySquare[i] = i;
    }

    // Render the whole game
    return (
      <div className="Game">
        {/* Game renders Board */}
        <div className="Board">
          {/* Board renders Squares */}
          {arraySquare.map(i => (
            <Square
              key={i}
              number={i}
              boardValues={this.state.value}
              onChange={this.handleChange}
            />
          ))}
        </div>
        <br />
        <div id="buttonDiv">
          <input
            type="button"
            value="Solve!"
            onClick={this.handleClickSolve}
            className="SolverButton"
          />
          <input
            type="button"
            value="Clear"
            onClick={this.handleClickClear}
            className="SolverButton"
          />
        </div>
      </div>
    );
  }
}

ReactDOM.render(<Game />, document.getElementById("app"));
