function initMember() {
	$('#id_gender').select2();

	$('#id_country').select2({
		placeholder: "Select a Country",
		allowClear: true
	});

	$("#id_interests").select2({
		tags: tags.interests, tokenSeparators: [",", " "]
	});
	$("#id_skills").select2({
		tags: tags.skills, tokenSeparators: [",", " "]
	});
	$("#id_products").select2({
		tags: tags.products, tokenSeparators: [",", " "]
	});

	var sel='#slide-member-bus-ask .proceed a[href="#slide-member-bus-details"]';
	$(sel).click(function (ev) {
		$('#id_has_bus').val('on');
		ev.preventDefault();
	});
};


function initCommunity() {
		$('#id_contact_country').select2({
			placeholder: "Select a Country",
			allowClear: true
		});

		$("#id_offers_services").select2({
			tags: tags.offersServices, tokenSeparators: [",", " "]
		});
		$("#id_offers_skills").select2({
			tags: tags.offersSkills, tokenSeparators: [",", " "]
		});
		$("#id_offers_creations").select2({
			tags: tags.offersCreations, tokenSeparators: [",", " "]
		});
};


$(function() {
	if (registerAs == 'member') {
		initMember();
	} else if (registerAs == 'community') {
		initCommunity();
	}

	$('.proceed a').click(function(ev) {
		$('.slide.show').removeClass('show').addClass('hide');
		var slide = $(this).attr('href');
		$(slide).removeClass('hide').addClass('show');

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
