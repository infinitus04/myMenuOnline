

logOut= () => {
   var valuecheck =  confirm("Do you want Logout ? ")

   if(valuecheck){
       window.open('/client/logout/');

   }
   else{
    // window.open();
    // alert("nothing")
    console.log("nothig")
   }
}

var myDiv = document.getElementById('myNotification');

  

setTimeout(function() {
    if (myDiv) {
        myDiv.classList.add('fade-in');
        setTimeout(function() {
            myDiv.classList.remove('fade-in');
            myDiv.classList.add('fade-out');
            setTimeout(function() {
                myDiv.remove();
            }, 100); // Wait for the fade-out animation to complete before removing the div
        }, 3000); // Wait for 4 seconds for the div to fade-in before starting fade-out
    }
}, 0000); // 1 second delay