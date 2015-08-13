$(function() {
	$("#mylist li").click(function() {
		var x = $(this).text();
		Cookies.set('source', x);
		
		$.getJSON($SCRIPT_ROOT + '/traintable', {
       		a: $(this).text()
        	
      	}, function(data) {
      		var array = data.result
        	$("#result").html( '<span>' + array.join('</span><span>')+'</span>');
      });
      return false;
	});
  });
