$('[data-navsearch]').on('click', 'a', function() {
	$(this).parent('[data-navsearch]').toggleClass('open');
});