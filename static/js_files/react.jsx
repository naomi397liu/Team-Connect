
function Homepage() {
    const [username, setUsername] = React.useState('') 
    const [password, setPassword] = React.useState('')
    
    function login(event){
        event.preventDefault()
        let data = {username: username, password: password}; //key is the STR username and value is the value of username
        fetch(`/login`, {
                headers: {
                    'Content-Type': 'application/json'
                },
                method: 'POST',
                body: JSON.stringify(data)
            })
            .then(res => res.json())
            .then(data => console.log(data));
    }
 
    function OpenCreateUser(){

    }

    return(
        <div>
            <h1>Welcome to Team Connect!</h1> <img id="logo" src="/static/imgs/redLogo.png"></img>
        
            <div id='login'>
                <h2>Sign In</h2>
    
                <form onSubmit={(e) => login(e)}>
                    <h4>Already have an account?</h4>
                    <input type="text" name="username" placeholder="Username" onChange={(e) => setUsername(e.target.value)}></input><br/>
                    <input type="password" name="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)}></input><br/><br/>
                    <input type="submit" value="Login" onChange={(e) => update(e.target.value)}></input><br/>
                </form>
                <form onSubmit={OpenCreateUser}>
                    <h4 id="new-user-text">Are you a new user?</h4>
                    <input type="submit" value="Create account"></input>
                </form>
            </div>
        </div>
    );
}


function App() {
    return (    
    <Homepage></Homepage>
    );
}


ReactDOM.render(
    <App />, //component
    document.getElementById('app')//location to render component
);