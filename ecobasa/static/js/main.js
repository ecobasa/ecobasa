$(window).load( function() {
    if (window.location.hash.substring(0, 3) == "#m-") { // Deep Link to Modal
        // remove #m- from hash
        var modalName = window.location.hash.substring(3);
        $('#'+modalName+'-modal').modal('show');
    }
    $('.modal-trigger').click(function () {
    	var modalName = $(this).attr("href").substring(3);
    	$('#'+modalName+'-modal').modal('show');
    	});
});

$(document).ready(function() {
	// Cache the Window object
	$window = $(window);

    $('section[data-type="parallax"]').each(function(){
    	var windowsize = $window.width();
		var $bgobj = $(this); // assigning the object
		if (windowsize > 440) {
			$(window).scroll(function() {
			    var yPos = ($window.scrollTop() / $bgobj.data('speed')); 
			    
			    // Put together our final background position
			    var coords = yPos + 'px';

			    // Move the background
			    $bgobj.css({ top: coords });
			}); 
		}
    });

    $('div[data-type="parallax"]').each(function(){
      var $obj = $(this); // assigning the object
      
      $(window).scroll(function() {
            var yPos = ($window.scrollTop() / $obj.data('speed')); 
            var top = $obj.position().top;
            
            // Put together our final background position
            var coords = 20 + yPos + '%';

            // Move the background
            $obj.css({ bottom: coords });
        }); 
    });

    $('[data-toggle="tooltip"]').tooltip();
	// $('.email').tooltip();
	$('[data-toggle="popover"]').popover();
	
	$('#accordion .collapse').on('shown.bs.collapse', function () {
       $(this).parent().find('.glyphicon-chevron-right').removeClass('glyphicon-chevron-right').addClass('glyphicon-chevron-down');
    });
    $('#accordion .collapse').on('hidden.bs.collapse', function () {
    	$(this).parent().find('.glyphicon-chevron-down').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-right');
    });
    
	$.ecobasa = {

		// searchbar in top fixed navigation
		searchbar : function() {
			$('#searchbar').hover( function() {
				$(this).addClass('open');
				$(this).addClass('mouseover');
			}, function() {
				if (!$(this).find('input').is(':focus'))
					$(this).removeClass('expanded');
				$(this).removeClass('mouseover');
			});
			$('#searchbar').find('input').blur( function() {
				if(!$(this).parent().hasClass('mouseover'))
					$(this).parent().removeClass('expanded');
			});
			$('#searchbar').click( function() {
				$(this).addClass('open');
			});
		},
  
		fullcalendar : function() {
			// There are two kinds of calendar in cosinnus: big and small.
			// The .big-calendar fills the content and shows events.
			// Users can add events here.
			// The .small-calendar is for tooltips or small static date chooser.
			// both are based on jQuery fullcalendar. http://arshaw.com/fullcalendar/

			var localeSettings = {
				de: {
					firstDay: 1, // Monday
					buttonText: {
						today: "Heute",
						month: "Monat",
						week: "Woche",
						day: "Tag"
					},
					monthNames: ['Januar','Februar','März','April',
						'Mai','Juni','Juli','August',
						'September','Oktober','November','Dezember'],
					monthNamesShort: ['Jan','Feb','Mär','Apr','Mai',
						'Jun','Jul','Aug','Sept','Okt','Nov','Dez'],
					dayNames: ['Sonntag','Montag','Dienstag',
						'Mittwoch','Donnerstag','Freitag','Samstag'],
					dayNamesShort: ['So','Mo','Di','Mi','Do','Fr','Sa'],
					titleFormat: {
						month: 'MMMM yyyy',
						week: "d.[ MMMM][ yyyy]{ - d. MMMM yyyy}",
						day: 'dddd d. MMMM yyyy'
					},
					columnFormat: {
						month: 'ddd',
						week: 'ddd d',
						day: ''
					},
					axisFormat: 'H:mm', 
					timeFormat: {
						'': 'H:mm', 
						agenda: 'H:mm{ - H:mm}'
					}
				}
			};
			// LanguageCode injected by backend
			var currentLocaleSettings = localeSettings[LanguageCode];

			if ($('.big-calendar').length)
			$('.big-calendar').fullCalendar($.extend({
				header: {
					left: 'prev,next today',
					center: 'title',
					right: 'month,agendaWeek,agendaDay' // basicDay
				},
				defaultView: 'agendaWeek',

				// cosinnus_calendarEvents is a global var containing the events
				// set by the backend somewhere in the BODY.
				events: cosinnus_calendarEvents,
				select: function(startDate, endDate, allDay, jsEvent, view) {
					$(this.element)
						.closest('.big-calendar')
						.trigger('fullCalendarSelect',[startDate, endDate, allDay, jsEvent, view]);
				},
				eventClick: function(event, jsEvent, view) {
					$(this)
						.closest('.big-calendar')
						.trigger('fullCalendarEventClick',[event, jsEvent, view]);
				},
				selectable: true,
				selectHelper: true
			}, currentLocaleSettings));

			if ($('.small-calendar').length)
			$('.small-calendar').fullCalendar($.extend({
				header: {
					left: 'prev',
					center: 'title',
					right: 'next'
				},
				dayClick: function(date, allDay, jsEvent, view) {
					$(this).trigger('fullCalendarDayClick',[date,jsEvent]);
				},
				viewRender: function(date, cell) {
					// A day has to be rendered because of redraw or something
					$(cell).closest('.small-calendar').trigger('fullCalendarViewRender',[cell]);
				}

			}, currentLocaleSettings));
		},


		calendarBig : function() {
			// The big calendar fills the whole content area and contains the user's events.

			$('.big-calendar')
				.on("fullCalendarSelect", function(event, startDate, endDate, allDay, jsEvent, view) {
					// Dates have been selected. Now the user might want to add an event.
					var startDateDataAttr = startDate.getFullYear() + "-"
						+ ((startDate.getMonth()+1).toString().length === 2
							? (startDate.getMonth()+1)
							: "0" + (startDate.getMonth()+1)) + "-"
						+ (startDate.getDate().toString().length === 2
							? startDate.getDate()
							: "0" + startDate.getDate());

					var endDateDataAttr = endDate.getFullYear() + "-"
						+ ((endDate.getMonth()+1).toString().length === 2
							? (endDate.getMonth()+1)
							: "0" + (endDate.getMonth()+1)) + "-"
						+ (endDate.getDate().toString().length === 2
							? endDate.getDate()
							: "0" + endDate.getDate());

					// allDay is always true as times can not be selected.


					$('#calendarConfirmStartDate').val(startDateDataAttr);
					$('#calendarConfirmEndDate').val(endDateDataAttr);

					if (startDateDataAttr == endDateDataAttr) {
						// Event has one day
						$('#calendarConfirmEventOneday').show();
						$('#calendarConfirmEventMultiday').hide();

						moment.lang(moment.lang(),$.cosinnus.momentShort[moment.lang()]);
						eventDate = moment(startDateDataAttr);
						var eventDate = moment(eventDate).calendar();
						$('#calendarConfirmEventDate').text(eventDate);

						$('#confirmEventModal').modal('show');
					} else {
						// Event has multiple days
						$('#calendarConfirmEventOneday').hide();
						$('#calendarConfirmEventMultiday').show();

						// There is no time, so use momentShort.
						moment.lang(moment.lang(),$.cosinnus.momentShort[moment.lang()]);
						startDate = moment(startDateDataAttr);
						var startDate = moment(startDate).calendar();
						$('#calendarConfirmEventStart').text(startDate);

						endDate = moment(endDateDataAttr);
						var endDate = moment(endDate).calendar();
						$('#calendarConfirmEventEnd').text(endDate);

						$('#confirmEventModal').modal('show');
					}
			});

		},

		// When creating or editing an event the user has to select date and time.
		// Clicking one date input shows all calendars on the whole page.
		calendarDayTimeChooser : function() {
			// Hide calendar when clicking outside
			$(document).click(function(event) {
				var thisdaytimechooser = $(event.target).closest('.calendar-date-time-chooser');
				if(thisdaytimechooser.length) {
					// Don't hide any chooser
				} else {
					// hide all
					$('.calendar-date-time-chooser .small-calendar').slideUp();
				}
			});

			$('.calendar-date-time-chooser input.calendar-date-time-chooser-date')
				.click(function() {
				$('.calendar-date-time-chooser .small-calendar').slideDown();
			});

			$('.calendar-date-time-chooser i').click(function() {
				$('.calendar-date-time-chooser .small-calendar').slideDown();
			});

			$('.calendar-date-time-chooser .small-calendar').hide();


			// on every re-drawing of the calendar select the choosen date
			$('.calendar-date-time-chooser .small-calendar')
				.on("fullCalendarViewRender", function(event, cell) {
					// select choosen day

					var date = $(this)
						.closest('.calendar-date-time-chooser')
						.find('.calendar-date-time-chooser-hiddendate')
						.val();
					// "2014-04-28"
					if (date) $(this)
						.find('td[data-date='+date+']')
						.addClass('selected');
				})
				.trigger('fullCalendarViewRender')

				// when clicked on a day: use this!
				.on("fullCalendarDayClick", function(event, date, jsEvent) {
					var dayElement = jsEvent.currentTarget;
					if ($(dayElement).hasClass('fc-other-month')) return;

					var dateDataAttr = date.getFullYear() + "-"
						+ ((date.getMonth()+1).toString().length === 2
							? (date.getMonth()+1)
							: "0" + (date.getMonth()+1)) + "-"
						+ (date.getDate().toString().length === 2
							? date.getDate()
							: "0" + date.getDate());

					// unselect all and re-select later
					$(dayElement).parent().parent().find('td').removeClass('selected');
					$(dayElement).addClass('selected');


					// When date picked, update date in form
					$(this)
						.closest('.calendar-date-time-chooser')
						.find('.calendar-date-time-chooser-hiddendate')
						.val(dateDataAttr);

					// Update INPUT with human readable date
					moment.lang(moment.lang(),$.cosinnus.momentShort[moment.lang()]);
					var humanDateString = moment(dateDataAttr).calendar();
						$(this)
							.closest('.calendar-date-time-chooser')
							.find('.calendar-date-time-chooser-date')
							.val(humanDateString);
				});

			// Set INPUT with human readable date
			$('.calendar-date-time-chooser').each(function() {
				var dateDataAttr = $(this)
					.find('.calendar-date-time-chooser-hiddendate')
					.val();

				if (dateDataAttr) {
					moment.lang(moment.lang(),$.cosinnus.momentShort[moment.lang()]);
					var humanDateString = moment(dateDataAttr).calendar();
						$(this)
							.find('.calendar-date-time-chooser-date')
							.val(humanDateString);
				}
			});
		}
	};

	$.ecobasa.fullcalendar();
	$.ecobasa.calendarBig();
	$.ecobasa.calendarDayTimeChooser();
	$.ecobasa.searchbar();
});
