$(document).ready(function(){
$( "button" ).each(function( index ) {
  var num1 = Math.random();
  var num2 = Math.random();
  var num3 = Math.random();
  var num4 = Math.random();
$( this ).css( {'left': num1, 'top': num2, 'right': num3, 'bottom': num4} ) });
});
