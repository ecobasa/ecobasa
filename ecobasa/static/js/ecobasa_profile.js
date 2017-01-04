EcobasaProfile = {
	initMember: function() {
		$('#id_gender').select2();

		$('#id_country').select2({
			placeholder: "Select a Country",
			allowClear: true
		});

		$("#id_interests").select2({
			tags: tags.interests, tokenSeparators: [","]
		});
		$("#id_wishlist").select2({
			tags: tags.wishlist, tokenSeparators: [","]
		});
		$("#id_skills").select2({
			tags: tags.skills, tokenSeparators: [","]
		});
		$("#id_services").select2({
			tags: tags.services, tokenSeparators: [","]
		});
		$("#id_products").select2({
			tags: tags.products, tokenSeparators: [","]
		});
	},

	initCommunity: function() {
		$('#id_contact_country').select2({
			placeholder: "Select a Country",
			allowClear: true
		});

		$("#id_offers_services").select2({
			tags: tags.offersServices, tokenSeparators: [","]
		});
		$("#id_offers_skills").select2({
			tags: tags.offersSkills, tokenSeparators: [","]
		});
		$("#id_offers_creations").select2({
			tags: tags.offersCreations, tokenSeparators: [","]
		});
		$("#id_offers_materials").select2({
			tags: tags.offersMaterials, tokenSeparators: [","]
		});
		$("#id_offers_tools").select2({
			tags: tags.offersTools, tokenSeparators: [","]
		});
		$("#id_wishlist_skills").select2({
			tags: tags.wishlistSkills, tokenSeparators: [","]
		});
		$("#id_wishlist_materials").select2({
			tags: tags.wishlistMaterials, tokenSeparators: [","]
		});
		$("#id_wishlist_tools").select2({
			tags: tags.wishlistTools, tokenSeparators: [","]
		});
	},

	initReference: function() {
		$("#id_products").select2({
			tags: tags.products, tokenSeparators: [","]
		});
		$("#id_services").select2({
			tags: tags.services, tokenSeparators: [","]
		});
		$("#id_skills").select2({
			tags: tags.skills, tokenSeparators: [","]
		});
	},
}
