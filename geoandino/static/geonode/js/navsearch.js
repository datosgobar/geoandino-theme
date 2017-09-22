$('[data-navsearch]').on('click', 'a', function() {

	var container = $(this).parent('[data-navsearch]');

	$(container).toggleClass('open');
	$(container).find('form').toggle("slide", {direction:"right"}, 300);

	if($(container).hasClass('open')){
		$(container).find('input').val("");
	}

});
