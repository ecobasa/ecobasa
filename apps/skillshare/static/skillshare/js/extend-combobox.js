/*
	extend-combobox.js

	Extends bootstrap-combobox
 */
$(function() {
	var extensions = {
		// modified blur function to keep inpt value if no match in source list
		blur: function (e) {
			var that = this
			this.focused = false
			var val = this.$element.val()
			if (!this.selected && val !== '' ) {
				this.$element.val(val)
				this.$source.val(val).trigger('change')
				this.$target.val(val).trigger('change')
			}
			if (!this.mousedover && this.shown) setTimeout(function () { that.hide() }, 200)
		}
	}
	$.extend(true, $.fn.combobox.Constructor.prototype, extensions);
});
