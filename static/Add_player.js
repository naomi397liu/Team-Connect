"use strict"

// TODO: make sure that the same user cannot add themselves multiple times
// or maybe just allow a user to remove themself
// function alertFunction(evt){

$('#add-player').on('click', (evt) => {
    const btn = $(evt.target);

    $.get('/add.json', (data) => {
        if(btn.html() === 'Join Team'){
            const res = $(`<li><a href="/users/${data[1]}">${data[0]}</a></li>`);
            $('#player-list').append(res);
            alert(`Welcome to the team, ${data[0]}!`); 
            btn.html('Leave Team');
        }else if (btn.html() === 'Leave Team'){
            // btn.html('Leave Team')
            alert(`${data[2]}`)
        }
    });
    
});

