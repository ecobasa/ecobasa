 $(document).ready(function() {
   if( ! $('#myCanvas').tagcanvas({
     textColour : '#000',
     outlineThickness : 1,
     stretchX : 3,
     imageScale : 0.6,
     maxSpeed : 0.03,
     depth : 0.75
   })) {
     // TagCanvas failed to load
     $('#myCanvasContainer').hide();
   }
   // your other jQuery stuff here...
 });