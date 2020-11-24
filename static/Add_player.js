"use strict"

// TODO: make sure that the same user cannot add themselves multiple times
// or maybe just allow a user to remove themself
// function alertFunction(evt){

$('#add-player').on('click', (evt) => {
    const btn = $(evt.target);

    $.get('/add.json', (data) => {
        if(btn.html() === 'Join Team' && x === 'new player!'){
            const res = $(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`);
            $('#player-list').append(res);
            alert(`Welcome to the team, ${data[0]}!`); 
            btn.html('Leave Team');
        }else (btn.html() === 'Leave Team' && x === 'removed player!')
        {
            alert(`You've been removed from the team!`)
            // const res = $(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`)
            // index = $('#player-list').indexOf(res)
            // $('#player-list').pop(index)
            btn.html('Join Team')
        }
    });
    
});

