var goal_position = $('#id_goal_div_1').offset();
var gp = goal_position.left;


var player_move = function(){
    $.ajax({
        type: "GET",
        url: "/player/move/1",
        success: function(data){
            var elem_offset = $('.player').offset();
            elem_offset = elem_offset.left;
            var elem_left = $('.player').position();
            if (elem_offset >= gp - 20){
                location.replace("/game/end/");
            }
            $('.player').css('left', elem_left.left + 20);
            },
            error: function(data){
                console.log(data);
                alert('Something went wrong!');
            }
    })
};

function generate_random_int(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

$(document).ready(function(){
    $('#move').on('click', player_move);
    var light = $('.light');
    //var intervalID = window.setTimeout(green_to_red, 1000);
    var iter_rate = generate_random_int(1000, 500000);
    var intervalID = window.setTimeout(green_to_red, iter_rate);
    //red_to_green();
    function green_to_red() {
        $(light).removeClass('green');
        $(light).addClass('red');
    }
    function red_to_green() {
        $(light).removeClass('red');
        $(light).addClass('green');
    }

});
