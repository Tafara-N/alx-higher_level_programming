#!/usr/bin/node

// Script fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and
// displays the value of hello from that fetch in the HTML tag DIV#hello

$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('DIV#hello').append(data.hello);
    }
  });
});
