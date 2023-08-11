

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