// const { string } = require("prop-types");

const Router = ReactRouterDOM.BrowserRouter;
const { useHistory, useParams, Redirect, Switch, Prompt, Link, Route } = ReactRouterDOM;

function Homepage() {
    const history = useHistory();
    const [username, setUsername] = React.useState('') 
    const [password, setPassword] = React.useState('')
    function checkData(data){
        if (typeof(data) == "number"){
            history.push("/users")
        }
    }
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
            .then(data => {
                checkData(data)
                console.log(data)});
        
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
                <form>
                    <h4 id="new-user-text">Are you a new user?</h4>
                    <input type="submit" value="Create account"></input>
                </form>
            </div>
        </div>
    );
}
// data is state
//wrap fetch in use effect
function Users(){
    const history = useHistory();
    // const [users, setUsers] = useState('')
    
    // useEffect(() => {fetch(`/users`, {
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         method: 'GET',
    //     })
    //     .then(res => res.json())
    //     .then(data => {
    //         console.log(data)});
    // }, []);
    return (
        <React.Fragment>
            <h1>All Users</h1>
            <p>Search through users by name, sport or location</p>
            <button onClick={() => history.push("/teams")}>Teams Page</button>

        </React.Fragment>
    );
}

function Teams(){
    return (
        <React.Fragment>
            <h1>All Teams</h1>
            <p>Search through teams by name, sport or location</p>
        </React.Fragment>
    )
}
function CreateTeam(){
    return (
        <React.Fragment>
            <h1>Create a Team</h1>
            <p>Use the form to create your own team</p>
        </React.Fragment>
    )
}
function Navbar(){
    return(
        <nav className="navbar navbar-dark bg-dark">
        <img className="logo" src="/static/imgs/redLogo.png"/>
        <Link to="/users">All Users</Link>
        <Link to="/teams">All Teams</Link>
        <Link to="/createteam">Create Team</Link>
        <Link to="/homepage">Logout</Link>
      </nav>
    )
}


function App() {
    return (    
        <React.Fragment>
            
                <Link to="/users">All Users</Link>
                <Link to="/teams">All Teams</Link>
                <Link to="/createteam">Create Team</Link>
                <Link to="/homepage">Logout</Link> 
            
            <h1>Page's Display:</h1>
            <Switch>
                <Route path="/homepage"> 
                    <Homepage></Homepage>
                </Route>
                <Route path="/users">
                    <Navbar></Navbar>
                    <Users></Users>
                </Route>
                <Route path="/teams">
                    <Navbar></Navbar>
                    <Teams></Teams>
                </Route>
                <Route path="/createteam">
                    <Navbar></Navbar>
                    <CreateTeam></CreateTeam>
                </Route>
            </Switch>
        </React.Fragment>
    );
}



ReactDOM.render(
    <Router>
        <App />
    </Router>, //component
    document.getElementById('app')//location to render component
);