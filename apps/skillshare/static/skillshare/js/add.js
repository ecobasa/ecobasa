$(function(){
	var skillname = $('select#id_name');
	var owners = $('select#id_owner');
	var initial_owner = owners.val();
	skillname.combobox();
	skillname.change(function() {

		owners.prop('disabled', true);
		var skill = $(this).val();
		if (skill != '') skill += '/'; // even add slash for null value

		$.get(URL_AVAILABLE_OWNERS + skill, function(data) {
			owners.find('option').remove();
			owners.append('<option value="">---------</option>');
			for (i = 0; i < data['available_owners'].length; i++) {
				var owner = data['available_owners'][i];
				owners.append('<option value="' + owner['pk'] + '">' + owner['username'] + '</option>');
			}
			// set to previously selected owner or default option if owner not in list
			owners.val(initial_owner);
			if (owners.val() != initial_owner) {
				owners.val('');
			}
			owners.prop('disabled', false);
		});
	});
});
