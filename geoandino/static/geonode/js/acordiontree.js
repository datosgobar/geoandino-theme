$('[data-accordiontree]').on('click', 'button', function() {

	var accTreeSelf = $(this).siblings('ul');
	var accTreeOtherUl = $(this).parent().siblings().find('ul');
	var accTreeOtherBtn = $(this).parent().siblings().find('button');

    if($(accTreeOtherUl).css('display')=='block'){
        $(accTreeOtherUl).slideUp();
        $(accTreeOtherBtn).removeClass('opened');
    }

    $(accTreeSelf).slideToggle();
    $(this).toggleClass('opened');

});