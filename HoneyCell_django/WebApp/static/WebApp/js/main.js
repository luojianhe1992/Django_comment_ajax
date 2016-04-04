/**
 * Created by jianheluo on 4/3/16.
 */

$('#comment_form').on('submit', function(event){
    event.preventDefault();

    console.log("Call the ajax function.");

    $.ajax({
        url : '/add_comment_ajax/',
        type : 'POST',
        data : {
            message_id: $('#message_id').val(),
            comment_text: $('#comment_text').val(),
                },

        success : function(json){
            console.log("Success receive json data.");
            $('#comment_text').val('');
            $('#comment_list').append('<li style="color: deepskyblue">' + json.user + ': ' + json.comment_text + '</li>');
        }
    });
});





function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});