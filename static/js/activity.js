const button = document.querySelectorAll(".con")
console.log(button);


for(let i = 0; i<button.length; i++) {
    button[i].addEventListener("click", ()=> {
        for(let j = 0 ; j<button.length;j++) {
            button[j].classList.remove("is_on");
        }
        button[i].classList.add("is_on");
    })
}