$(function() {
	
	$.getJSON($SCRIPT_ROOT + '/preferences', 
	function(data) {
		var array = data.result
		$("#result").html( '<span>' + array.join('</span><span>')+'</span>');
      	return false;
    });
    
    
});


