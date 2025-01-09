import "./api.js";

document.querySelector("#add-btn").addEventListener(
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
    "click", get
)

window.addEventListener(
    "click", (event) => {
        popup = document.querySelector(".popup");

        if(!popup.contains(event.target)) {
            popup.classList.remove("active");
        }
    }
);

function listview() {
    const row = document.querySelector(".row"); 

    items = ["banana", "apple", "mango"];
    items.forEach(elem => {
        const column = document.createElement("div");
        column.classList.add("column");
        column.textContent = elem;
        
        row.appendChild(column);
    });
}
