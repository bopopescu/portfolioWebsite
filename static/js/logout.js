//logout.js
$(document).ready(function() {
    $("#form_logout").submit(function(event)
    {
        event.preventDefault();
        var url = '/api/v1/logout';
        console.log(url);

    $.ajax(
        {
            type: "POST",
            contentType: "application/json; charset=UTF-8",
            url: url,
            data: '',
            success : function(data)
            {
                window.location.replace("/");
            },
            error : function(response)
            {
                console.log(response);
            }
        });
    });

        event.preventDefault();


    });
