$(function() {
	$("#mylist li").click(function() {
		var x = $(this).text();
		Cookies.set('source', x);
		
		$.getJSON($SCRIPT_ROOT + '/traintable', {
       		a: $(this).text()}, function(data) {
			$("#result0").text(data.result[0]);
			$("#result1").text(data.result[1]);
			$("#result2").text(data.result[2]);
			$("#result3").text(data.result[3]);
			$("#result4").text(data.result[4]);
          });
	});
  });
