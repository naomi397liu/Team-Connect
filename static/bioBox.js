"use strict"

$('#bio').keyup(function() {
    var maxLength = 50;
    var value = $("#bio").val();
    var length = $("#bio").val().length;
    var length = maxLength-length;
    $("#charlength").text(length);
})