$(function() {
    console.log("Hello from robot js");
	$('button').click(function() {
        console.log("Button click!");
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
        // This is an AJAX HTTP request sent to the Flask web server.
        // TODO: Change this to be something like /servoValues
        //       with a payload of 4 servo degree values that are numbers between 0 and 180.
		$.ajax({
			url: '/signUpUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
