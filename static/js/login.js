//login.js
$(document).ready(function() {
    $("#login_form").submit(function(event)
    {
        event.preventDefault();
        var url = '/api/v1/login';
        console.log(url);

    $.ajax(
        {
            type: "POST",
            contentType: "application/json; charset=UTF-8",
            data: JSON.stringify({
                "username": document.getElementById("login_username_input").value,
                "password": document.getElementById("login_password_input").value
            }),
            url: url,
            success : function(data)
            {
                var queryString = window.location.href.indexOf('url=');
                if (queryString == -1)
                {
                    window.location.replace("/al8sevu5/p3/")
                }
                else
                {
                    var newURL = window.location.href.split('url=')[1];
                    console.log(newURL);
                    window.location.replace("/" + newURL);
                }
            },
            error : function(response)
            {
                console.log(response);
                var parsedString = JSON.parse(response.responseText);
                var errorMess = parsedString['errors'];
                var HTMLobject = document.getElementById("error");

                while (HTMLobject.childNodes.length > 0)
                {
                    HTMLobject.removeChild(HTMLobject.lastChild);
                }

                for (var i in errorMess)
                {
                    var p = document.createElement("p");
                    var node = document.createTextNode(errorMess[i]['message']);

                    p.setAttribute("class", "error");
                    p.appendChild(node);
                    HTMLobject.appendChild(p);
                }
            }
        });
    });

        event.preventDefault();
    });
