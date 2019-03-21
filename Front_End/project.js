//This is where the magic happens

function onClick(){
//Switches from a basic login prompt to Duo Auth
    document.getElementByID();
    //Get duo, hidden to visible
    document.getElementsByClassName();
    //Get login, visible to hidden
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

function mainContainer() {
    return (
       <div class="mainContainer">
            This is where a login prompt will be
            <div class="login">
              {loginContainer}
                <p>this will initially be hidden, will use DOM elements to toggle show and hidden
                between this and the login prompt, and to trigger a switch b/n success/failure screens</p>
           </div>
            <div class="duo">
         {duoAuthenticationContainer}
           </div>
             <div class="authenticated">
              
             </div>
       </div>
           )
}

function duoAuthenticationContainer() {
    
}

function loginContainer() {
    
}

//TODO: Figure out how to do the calls/responses, Register event handler, finish onClick Function
