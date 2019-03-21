//This is where the magic happens

function onClick(){
//Switches from a basic login prompt to Duo Auth

}

function registerListener(){
    //Register an event listener to the button, which will trigger onClick
}

function showSuccess() {
//if GET == Success then: 
return (
    <div>
        <h2>Success!</h2>
        <p>You were successfully authenticated!</p>
    </div>
)
}

function showFailure() {
//GET != Success then: 
return (
    <div>
        <h2>Authentication Failed</h2>
        <p>We were unable to authenticate you at this time</p>
    </div>
)
}

//TODO: Figure out how to do the calls/responses, Register event handler, finish onClick Function
