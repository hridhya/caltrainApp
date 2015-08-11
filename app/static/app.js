$(function() {
	
	$.getJSON($SCRIPT_ROOT + '/preferences', 
	function(data) {
        $("#result").text(data.result);
      	return false;
    });
    
    
});
