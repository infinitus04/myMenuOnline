    // Get references to the checkbox and the element to toggle


// let slogan_slides = document.getElementById("slogan");
// var i = 1;

// const  slogans = [' " Menus on the Move: Scan, Savor, Delight inEvery Bite! " ', ' " QR Codes, Deliciously: Explore Menus at Your Fingertips! "' , '" QR Menus: Scan, Explore, Savor the Experience! "', ' " Unleash Culinary Creativity \nwith Menu Magic! "', ];

// function changeSlogan() {
//     if(i>3){
//         i=0;



//     }


// slogan_slides.innerHTML = slogans[i];
// i++;

// };
const menu_design =document.getElementById("menu-design");

// const animatedImage1 = document.getElementById("menu1");
// const animatedImage2 = document.getElementById("menu2");
// const animatedImage3 = document.getElementById("menu3");
// const animatedImage4 = document.getElementById("menu4");
// const animatedImage5 = document.getElementById("menu5");
// const animatedImage6 = document.getElementById("menu6");
// const animatedImage7 = document.getElementById("menu7");


document.addEventListener("DOMContentLoaded", function () {


setTimeout(() => {

    const menu=menu_design.querySelectorAll("img")

    menu[0].style.transform = "translateY(0%)";
    menu[1].style.transform = "translateY(0%)";
    menu[2].style.transform = "translateX(0%)";
    menu[3].style.transform = "translateX(0%)";
    menu[4].style.opacity="1";
    menu[5].style.opacity="1";
    menu[6].style.opacity="1";

}, 100);


});

const sign_btn=document.getElementById("sign-btn")
const get_btn=document.getElementById("get-btn")

sign_btn.addEventListener("mouseenter",()=>{

    get_btn.style.backgroundColor="transparent";
    get_btn.style.border=" 2px solid rgb(5, 98, 173,0.3) "
})

sign_btn.addEventListener("mouseleave",()=>{

    get_btn.style.backgroundColor="rgb(6, 143, 255,0.2)";
    get_btn.style.border=" none"
})






