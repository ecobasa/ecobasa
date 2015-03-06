$(function() {
	if (registerAs == 'member') {
		EcobasaProfile.initMember();

		var sel='#slide-member-bus-ask .proceed a[href="#slide-member-bus-details"]';
		$(sel).click(function (ev) {
			$('#id_has_bus').val('on');
			ev.preventDefault();
		});
	} else if (registerAs == 'community') {
		EcobasaProfile.initCommunity();
	}

	$('.proceed a').click(function(ev) {
		$('.slide.show').removeClass('show').addClass('hide');
		var slide = $(this).attr('href');
		$(slide).removeClass('hide').addClass('show');
		window.scrollTo(0, 140);

		// FIXME: should be done more efficiently
		if (slide != '#slide-member-bus-details') {
			$('.navbar-nav li.active').removeClass('active');
			$('.navbar-nav a[href=' + slide + ']').parent().addClass('active');
		}

		ev.preventDefault();
	});


	$('.container .navbar-nav a').click(function(ev) {
		var slide = $(this).attr('href');
		$('.slide.show').removeClass('show').addClass('hide');
		$(slide).removeClass('hide').addClass('show');

		$('.navbar-nav li.active').removeClass('active');
		$(this).parent().addClass('active');

		ev.preventDefault();
	});
});
