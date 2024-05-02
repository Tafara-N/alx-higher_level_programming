#!/usr/bin/node

// Script toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header

$('div#toggle_header').click(function () {
  $('header').ToggleClass('red');
});
