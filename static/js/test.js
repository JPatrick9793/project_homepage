function myFunction(txt) {
    $.ajax({
      type: "POST",
      url: "http://www.thejohnconway.com/testing/sudoku",
      data: txt,
      cache: false,
      dataType: "json",
      // IF successful
      success: function(data) {
        alert("Success");
        console.log(data)
      },
      // If unsuccessful
      error: function(data) {
        alert("There was an error");
        console.log(data);
      }
    });
}


function alertSomething() {
    $.ajax({
      type: "POST",
      url: "http://www.thejohnconway.com/testing/sudoku",
      cache: false,
      dataType: "json",
      // IF successful
      success: function(data) {
        alert("Success");
      },
      // If unsuccessful
      error: function(data) {
        alert("There was an error");
        console.log(data);
      }
    });
}
