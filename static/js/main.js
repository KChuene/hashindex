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
        get(search);
    }
);

document.querySelector("#add-btn").addEventListener(
    "click", () => {
        add(addnew)
    }
);

window.addEventListener(
    "click", (event) => {
        const popup = document.querySelector(".popup");

        if(!popup.contains(event.target)) {
            popup.classList.remove("active");
        }
    }
);

async function search(result) {
    /* Sample: 
        {"success": bool, 
         "message": {
            "hash": str,
            "phrase": str
         }
        }
    */
    var row = document.querySelector(".row"); 
    var objvalid = isvalid(result);

    if(!(result && !objvalid)) {
        return;
    } 

    lstitem = item(result); 
    row.appendChild(lstitem);
}

function addnew() {
    var result = JSON.parse( addnew() );
    if(result && result.success) {
        alert(result.message);
        return;
    }

    alert("Failed!");
}

function item(content) {
    const listitem = document.createElement("div");
    listitem.classList.add("list-item");
    
    const hash = document.createElement("p");
    const phrase = document.createElement("p");

    hash.textContent = content.hash;
    phrase.classList.add("pass-phrase");
    phrase.textContent = content.phrase;

    listitem.appendChild(hash);
    listitem.append(phrase);
}

/*
<div class="list-item">
    <p>59f46bb90cffb0ed7c7e5db58bb300f3bcd714f51ae723ed91b06a3e13d4d5b6</p>
    <p class="pass-phrase">p@55w0rd</p>
</div>
*/
