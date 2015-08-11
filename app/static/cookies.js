$(function() {
	$('a#cookies').bind('click', function() {
		console.log($('#a :selected').text())
		var x = $('#a :selected').text() 
		console.log(x);
		Cookies.set('source', x);
		
		$.getJSON($SCRIPT_ROOT + '/traintable', {
       		a: $('#a :selected').text()
        	
      	}, function(data) {
        	$("#result").text(data.result);
      });
      return false;
	
	
	});
  });
