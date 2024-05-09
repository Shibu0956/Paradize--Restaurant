const formOpenBtn = document.querySelector("#form-open"),
home = document.querySelector(".home"),
formcontainer = document.querySelector(".form_container"),
formclose = document.querySelector(".form_close");
// signupBtn = document.querySelector("#signup"),

formOpenBtn.addEventListener("click",() => home.classList.add("show"))
formclose.addEventListener("click",() => home.classList.remove("show"))