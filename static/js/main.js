import {get} from "./api.js";

document.querySelector("#show-popup-btn").addEventListener(
    "click", (event) => {
        event.stopPropagation();
        document.querySelector(".popup").classList.add("active");
    }
);

document.querySelector(".popup .close-btn").addEventListener(
    "click", () => {
        document.querySelector(".popup").classList.remove("active");
    }
);

document.querySelector("#search-btn").addEventListener(
    "click", () => {
        get(listview);
    }
);

document.querySelector("#add-btn").addEventListener(
    "click", null
);

window.addEventListener(
    "click", (event) => {
        const popup = document.querySelector(".popup");

        if(!popup.contains(event.target)) {
            popup.classList.remove("active");
        }
    }
);

async function listview(result) {
    var row = document.querySelector(".row"); 
    var items = result || [];

    items.forEach(elem => {
        const column = document.createElement("div");
        column.classList.add("column");
        column.textContent = elem;
        
        row.appendChild(column);
    });
}

function addnew() {
    var result = JSON.parse( addnew() );
    if(result && result.success) {
        alert(result.message);
        return;
    }

    alert("Failed!");
}
