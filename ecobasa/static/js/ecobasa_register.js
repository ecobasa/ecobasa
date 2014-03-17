$(function() {
  $('#id_gender').select2();

  $('#id_country').select2({
    placeholder: "Select a Country",
    allowClear: true
  });


  $('#slide-register-member').click(function(ev) {
    $('#form-register-member #id_register_as').val('member');
    $('#slide-register-as').removeClass('show').addClass('hide');
    $('#navbar-member').removeClass('hide').addClass('show');
    $('#slide-member-personal').removeClass('hide').addClass('show');

    ev.preventDefault();
  });

  $('#slide-register-community').click(function(ev) {
    $('#form-register-community #id_register_as').val('community');
    $('#slide-register-as').removeClass('show').addClass('hide');
    $('#navbar-community').removeClass('hide').addClass('show');
    $('#slide-community-contact').removeClass('hide').addClass('show');

    ev.preventDefault();
  });


  $('#slide-member-bus-ask .proceed a[href="#slide-member-bus-details"').click(function (ev) {
    $('#id_has_bus').val('on');

    ev.preventDefault();
  });


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

  $('.navbar-nav a').click(function(ev) {
    var slide = $(this).attr('href');
    $('.slide.show').removeClass('show').addClass('hide');
    $(slide).removeClass('hide').addClass('show');

    $('.navbar-nav li.active').removeClass('active');
    $(this).parent().addClass('active');

    ev.preventDefault();
  });
});
