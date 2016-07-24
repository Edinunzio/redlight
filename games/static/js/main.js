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
                alert('An error has occured');
            }
        })
});


//var winner = abstractAjax('/winner/', {"winner": "Player 1"});