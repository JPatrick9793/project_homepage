function myFunction(txt) {
	alert(txt);

    $.ajax({
      type: "POST",
      url: "http://www.thejohnconway.com/testing/sudoku/" + txt,
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


function alertSomething() {
    $.ajax({
      type: "GET",
      url: "http://www.thejohnconway.com/testing/sudoku/yes",
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
