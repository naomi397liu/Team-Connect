"use strict"



const alertFunction = (evt) => { 
    evt.preventDefault()
    let phone = $('#phone').val();

    $.get(`/add.json?phone=${phone}`, (data) => { 
        const btn = $('#add-player');
        const res = $(`<li id=${data[1]}><a href="/users/${data[1]}">${data[0]}</a></li>`); // "lucia" -> users/18
        let playerList = $('#player-list')
        
        if( data[2] === 'new player!'){
            $('#player-list').append(res);
            alert(`Welcome to the team, ${data[0]}!`);
            
        }else if (data[2] === 'already player!'){
            alert(`${data[2]} Removed: ${data[0]}`);
            $(`#${data[1]}`).remove();
            
        }
    });
}

$('#add').submit(alertFunction)
