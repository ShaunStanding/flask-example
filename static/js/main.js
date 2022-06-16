


let = myName = "Shaun"  /* mutable variable*/
const myLastName = "Standing" /* immutable variable */


if (myName === "Shaun") {
    console.log(`hello {myName}`)
} else {
    console.log("You're not Shaun!")
}


function reallyGoodFunction (num1, num2){   /* function example */
    let result = num1 + num2;
    return result;
}

function taskHider () {
    let element = document.getElementById("task-box")
    element.classList.toggle("hidden")
}

function darkMode () {
    let element = document.getElementById("base-body")
    element.classList.toggle("dark-mode")
}

function displayDate () {
    document.getElementById("date").innerHTML = Date()
}