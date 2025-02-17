import {get, add} from "./api.js";

const lookups = new Map([
    ["59f46bb90cffb0ed7c7e5db58bb300f3bcd714f51ae723ed91b06a3e13d4d5b6", "p@55w0rd"],
    ["008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601", "Password123"]
]);
const MAX_BSIZE = 10;
var isout_rst = true;

// Show nothing here in list view after page is loaded
$(document).ready(
    show(null) 
); 

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
        const lhash = $("#search-input").val();
        if(lookups.has(lhash)) {
            search({message: {
                    hash: fetchkey(lhash), 
                    phrase: lookups.get(lhash),
                },
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

function search(response) {
    if(response && response.success) {
        localize(response);
        show(
            item(response.message),
            true 
        ); // true = localized
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

        const message = response.message
        lookups.set(message.hash, message.phrase);
    }
}

function show(item) {
    const lsize = (lookups)? lookups.size: 0;
    cleardup( (item)? item.attr("id"): null);

    if(!item || lsize === 0) {
        // item == null is for output reset
        $(".lv-column").html(
            noitem()
        );
        isout_rst = true;
    }
    else
    if(isout_rst) {
        $(".lv-column").html(item); 
        isout_rst = false;
    }
    else {
        // assuming size >= 0 always
        $(".lv-column").prepend(item);
        isout_rst = false;
    }
}

function cleardup(id) {
    if(id) {
        const elem = $(`#${id}`);
        if(elem) {
            elem.remove();
        }
    }
}

function fetchkey(hkey) {
    for(const [key, value] of lookups) {
        if(key === hkey) {
            return key;
        }
    }
    return null;
}

function item(response) {
    const lstitem = $("<div>").addClass("list-item")
        .append(
            $("<p>").addClass("found-hash").text(response.hash)
        )
        .append(
            $("<p>").addClass("pass-phrase").text(response.phrase)
        )
        .attr("id", response.hash);

    return lstitem;
}

function noitem() {
    const notice = $("<div>").addClass("lv-nothing")
        .append(
            $("<img>", {
                src: "/static/images/planet.png",
                alt: "#"
            })
        )
        .append(
            $("<h2>").text("Nothing here!")
        )
        .append(
            $("<a>", {
                href: "https://www.flaticon.com/free-icons/empty-state",
                title: "empty state icons",
                css: {
                    "font-size": "x-small"
                },
                text: "by andinur - Flaticon"
            })
        );
    return notice;
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

// 3 - Empty Listview
/*
<div class="lv-nothing">
    <img src="{{ url_for('static', filename='images/planet.png')}}" alt="#">
    <h2>
        Nothing here!
    </h2>

    <!--<a href="https://www.flaticon.com/free-icons/empty-state" title="empty state icons">Empty state icons created by andinur - Flaticon</a>-->
    <a href="https://www.flaticon.com/free-icons/empty-state" title="empty state icons" style="font-size: x-small;">by andinur - Flaticon</a>
</div>
*/
