$(document).ready(function(){
   $("#dropdownMenuLink").click(function(){
      $(".dropdown-menu").toggle();
     
   });
  });

// login or signin

const formOpenBtn = document.querySelector("#form-open"),
home = document.querySelector(".home"),
formcontainer = document.querySelector(".form_container"),
formclose = document.querySelector(".form_close");
// signupBtn = document.querySelector("#signup"),

formOpenBtn.addEventListener("click",() => home.classList.add("show"))
formclose.addEventListener("click",() => home.classList.remove("show"))



// login or login
const formOpenBtn1 = document.querySelector("#form-open1"),
home1 = document.querySelector(".home1"),
formcontainer1 = document.querySelector(".form_container1"),
formclose1 = document.querySelector(".form_close1");
// signupBtn = document.querySelector("#signup"),

formOpenBtn1.addEventListener("click",() => home1.classList.add("show"))
formclose1.addEventListener("click",() => home1.classList.remove("show"))

