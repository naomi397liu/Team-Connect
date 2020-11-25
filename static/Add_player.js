"use strict"

// TODO: make sure that the same user cannot add themselves multiple times
// or maybe just allow a user to remove themself

function myFunction(){
    $.get('/button.json', (data) => {
        alert(`${data}`); //data[0] = username, data[1] = user_id data[2]=x
        // if (data[2] === 'new player!'){
        //     const btn = $('#add-player');
        //     btn.html('Join Team');
        // }else{
        //     const btn = $('#add-player');
        //     btn.html('Leave Team');
        // }

    });
}

function alertFunction(evt){ 
    $.get('/add.json', (data) => {
        if( data[2] === 'new player!'){
            const res = $(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`);
            $('#player-list').appendChild(res);
            alert(`Welcome to the team, ${data[0]}!`);
            const btn = $('#add-player');
            btn.html('Leave Team');
        }else if (data[2] === 'already player!'){
            alert(`${data[2]}`)
            // const btn = $('#add-player');
            // const playerList = $('#player-list')
            // const index = playerList.pop($(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`));
            // alert(`index of player: ${index}, ${data[2]}`)
        }
    });
}

// function alertFunction(evt){ 
//     $.get('/add.json', (data) => {
//         console.log(`got data: ${data}`);
//         if( data[2] === 'new player!'){
//             const res = $(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`);
//             $('#player-list').append(res);
//             alert(`Welcome to the team, ${data[0]}!`); 
//         }else if (data[2] === 'already player!'){
//             alert(`${data[2]}`)
//         }
//     });
// }