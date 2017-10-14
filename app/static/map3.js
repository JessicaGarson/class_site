$(document).ready(function(){
$( "button" ).each(function( index ) {
  var num1 = Math.random() * 2500;
  var num2 = Math.random() * 2500;
  var num3 = Math.random() * 2500;
  var num4 = Math.random() * 2500;
$( this ).css( {'left': num1, 'top': num2, 'right': num3, 'bottom': num4} ) });
});
