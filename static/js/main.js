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
        const lookup = $("#search-input").val();
        if(lookups.has(hash)) {
            search({
                hash: lookup, 
                phrase: lookups.get(hash),
                success: true
            });
            return;
        }

        get($("#search-input").val(), search);
        reset("search");
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

$("#hash-input").on("focus", function() { 
    $(this).val("")
});
$("#phrase-input").on("focus", function() { 
    $(this).val("")
});

window.addEventListener(
    "click", (event) => {
        const popup = document.querySelector(".popup");

        if(!popup.contains(event.target)) {
            popup.classList.remove("active");
            reset("addin");
        }
        reset("addout");
    }
);

const lookups = new Map();
const MAX_BSIZE = 10;

function search(response) {
    if(response && response.success) {
        localize(response);

        $(".lv-column").append(
            item(response.message)
        );
    }
}

function addnew(response) {
    if(response) {
        if(response.success) {
            $("#add-response").text(response.message);
            return;
        }

        $("#add-response").text(response.message);
    }
}

function localize(response) {
    if(response) {
        // Delete & Add anew if exists
        if(lookups.has(response.hash)) {
            lookups.delete(response.hash); 
        } 
        else 
        if(lookups.size >= MAX_BSIZE) {
            lookups.delete(
                lookups.keys().next().value
            );
        }
        lookups.set(response.hash, response.phrase);
    }
}

function item(response) {
    const lstitem = $("<div>").addClass("list-item")
        .append(
            $("<p>").addClass("found-hash").text(response.hash)
        )
        .append(
            $("<p>").addClass("pass-phrase").text(response.phrase)
        );

    return lstitem;
}

function reset(field) {
    const handler = {
        search: () => $("#search-input").val(null),
        addin: () => {
            $("#hash-input").val("");
            $("#phrase-input").val("");
        },
        addout: () => {
            $("#add-response").text("")
        }
    };

    if(handler[field]) { 
        handler[field](); 
    }
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
