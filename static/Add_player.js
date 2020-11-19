"use strict"

function alertFunction(evt){
    $.get('/add.json', (data) => {
        const res = $(`<li>${data}</li>`);
        $('#player-list').append(res);
        // $('#new-player').html(res);
        alert(`You have been you have been added to the team!`);
    });
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

