$(function() {
	$("#mylist li").click(function() {
		var x = $(this).text();
		console.log(x);
		Cookies.set('source', x);
		
		$.getJSON($SCRIPT_ROOT + '/traintable', {
       		a: $(this).text()
        	
      	}, function(data) {
        	$("#result").text(data.result);
      });
      return false;
	});
  });
