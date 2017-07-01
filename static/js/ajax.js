$(document).ready(function(){

var frm = document.getElementById("speachForm");

      ajaxform = function(e) { frm.submit(function (e) {

        e.preventDefault();

        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            async: true,
            success: function (data) {
                alert(data);
            },
            error: function (data) {
                alert(data);
            },
        });

    });

  };

})