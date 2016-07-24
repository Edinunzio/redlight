var abstractAjax = (function(url, info){
    $.ajax({
            type: "POST",
            url: url, //url: '/edit_distance/',
            data: info,
            dataType: 'json',
            success: function(data){
                console.log(data);
            },
            error: function(data){
                alert('An error has occurred');
            }
        })
});
var goal_position = $('#id_goal_div_1').offset();
var gp = goal_position.left;


var player_move = function(){
    $.ajax({
        type: "GET",
        url: "/player/move/1",
        success: function(data){
            var elem_offset = $('.player').offset();
            elem_offset = elem_offset.left;
            console.log(elem_offset);
            var elem_left = $('.player').position();
            console.log(gp);
            if (elem_offset >= gp){
                alert(gp);
                // game should end
            }
            $('.player').css('left', elem_left.left + 20);
            },
            error: function(data){
                console.log(data);
                alert('Something went wrong!');
            }
    })
};
$(document).ready(function(){
    $('#move').on('click', player_move);
});
