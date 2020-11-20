"use strict"

// TODO: make sure that the same user cannot add themselves multiple times
// or maybe just allow a user to remove themself
function alertFunction(evt){
    $.get('/add.json', (data) => {
        if( data[2] === 'new player!'){
            const res = $(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`);
            $('#player-list').append(res);
            alert(`Welcome to the team, ${data[0]}!`); 
        }else if (data[2] === 'already player!'){
            alert(`${data[2]}`)
        }
    });
    // Keeps going into else!! ie data[2] is always false, but it is adding to the team


    // $('#add-player').on('click', (evt) => {
    //     const btn = $(evt.target);
      
    //     if (btn.html() === 'Join Team') {
    //       btn.html('Leave Team');
    //     } else {
    //       btn.html('Join Team');
    //     }
    //   });
};

// function addPlayer(evt) {
//     evt.preventDefault();
//     session['current_user']
//     const formInputs = {
//         'qty': $('#qty-field').val(),
//         'melon_type': $('#melon-type-field').val()
//     };
//     $.post('/order-melons.json', formInputs, (res)=> {
        
//         if (res['code'] === 'ERROR') {
//             $('#order-status').addClass('order-error');
//         }

//         $("#order-status").text(res['code']);
//         $("#order-status").text(res['msg']);
//     })
// }


// $("#add-player").on('submit', addPlayer);

// $.ajax({
//     type: "POST",
//     url: "../templates/crud.py",
//     data: { num: session['current_user']}
//   }).done(get_player_by_id( o ) {
//      // do something
//   });

// $.ajax({
//     type: "POST",
//     url: "../templates/crud.py",
//     data: { user: session['current_user'], team: team}
//   }).done(create_teams_player( o ) {
//      // do something
//   });

