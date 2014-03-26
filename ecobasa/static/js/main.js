 $(document).ready(function() {
   if( ! $('#myCanvas').tagcanvas({
     textColour : '#000',
     outlineColour : '#da6137',
     outlineMethod : 'colour',
     outlineThickness : 1,
     pulsateTime : '1',
     stretchX : 5,
     imageScale : 0.6,
     maxSpeed : 0.03,
     depth : 0.5,
     zoom : 0.75,
     fadeIn: 2000
   })) {
     // TagCanvas failed to load
     $('#myCanvasContainer').hide();
   }
   // your other jQuery stuff here...
 });