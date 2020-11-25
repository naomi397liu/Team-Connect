"use strict"



function alertFunction(evt){ 
    $.get('/add.json', (data) => { //data = [new_player, user_id, x]
        
        const btn = $('#add-player');
        const res = $(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`); // "lucia" -> users/18
        let playerList = $('#player-list')
        
        if( data[2] === 'new player!'){
            
            $('#player-list').append(res);
            alert(`Welcome to the team, ${data[0]}!`);
            console.log('playerList for new player', playerList);
            

        }else if (data[2] === 'already player!'){
            alert(`${data[2]} Removed: ${data[0]}`);
    
            location.reload(); 
            
           
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