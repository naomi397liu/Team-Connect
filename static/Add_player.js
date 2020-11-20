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
    
};

