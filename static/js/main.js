import {get, add} from "./api.js";


$("#show-popup-btn").on(
    "click", (event) => {
        event.stopPropagation();

        $(".popup").addClass("active");
    }
);

$(".popup .close-btn").on(
    "click", () => {

        $(".popup").removeClass("active");
    }
);

$("#search-btn").on(
    "click", () => {

        get($("#search-input").val(), search);
    }
);

$("#add-btn").on(
    "click", () => {
        const data = {
            hash: $("#hash-input").val(),
            phrase: $("#phrase-input").val(),
            htype: $("#htype-select").val()
        };

        add(data, addnew);
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

function search(response) {
    if(response && response.success) {
        $(".lv-column").append(
            item(response.message)
        );
    }
}

function addnew(response) {
    
    if(response) {
        if(response.success) {
            alert(response.message);
            return;
        }

        alert(response.message);
    }
}

function item(response) {
    const lstitem = $("<div>").addClass("list-item")
        .append(
            $("<p>").text(response.hash)
        )
        .append(
            $("<p>").addClass("pass-phrase").text(response.phrase)
        );

    return lstitem;
}

// SAMPLES
// 1 - get Response
    /* Sample: 
        {"success": bool, 
         "message": {
            "hash": str,
            "phrase": str
         }
        }
    */

// 2 - List Item
/*
<div class="list-item">
    <p>59f46bb90cffb0ed7c7e5db58bb300f3bcd714f51ae723ed91b06a3e13d4d5b6</p>
    <p class="pass-phrase">p@55w0rd</p>
</div>
*/
