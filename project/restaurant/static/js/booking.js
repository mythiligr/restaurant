$('#start_time').timepicker({
  timeFormat: 'hh:mm a',
  interval: 30,
  minTime: '10',
  maxTime: '09:00 PM',
  startTime: '10:00 AM',
  dropdown: true,
  scrollbar: true
});
$('#end_time').timepicker();
var error = false;
$('#start_time').timepicker('option', 'change', function(time) {
	var later = new Date(time.getTime() + (60 * 60 * 1000));
    $('#end_time').timepicker('setTime', later);
	var data = {'start_time': $('#start_time').val()}
	 $.ajax({
        data: data,
        type: 'POST',
        url: '/existing-time-check/',
        async: false,
        success: function(response) {
            if (response.count > 0) {
            	error = true;
            }else{
            	error = false;
            }
        }
    });
  });

$('#createBooking').submit(function() {
	if (error == false) {
		$.ajax({
		    data: $(this).serialize(),
		    type: 'POST',
		    url: '/Book-table/',
		    success: function(response) {
		    	console.log(response)
		        if (response.status == true) {
		        	window.location.href = "/booking/";
		        }
		    }
		});	
	}else{
		alert('This table already Booked');
	}
	return false;
});

