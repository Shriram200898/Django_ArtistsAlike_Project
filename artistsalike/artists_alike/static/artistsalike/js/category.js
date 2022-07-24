
$(function() {
            $("#O_Category".change(function(){
                var select=$("#O_Category option:selected").text();
                $("#Price").val(select);
            })
        })
