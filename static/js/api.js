const api = "/api";

function get() {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", api, true);
    xhr.onreadystatechange = () => {
        if(xhr.readyState == XMLHttpRequest.DONE) {
            const status = xhr.status;

            if(status === 0 || (200 <= status && status < 400)) {
                return JSON.parse(xhr.responseText);
            }
            
            return [];
        }
    };
    xhr.send();
}

function add(data) {
    var xhr = new XMLHttpRequest();

    xhr.open("POST", api, true);
    xhr.onreadystatechange = () => {
        if(xhr.readyState == XMLHttpRequest.DONE) {
            const status = xhr.status;

            if(status === 0 || (200 <= status && status < 400)) {
                return JSON.parse(xhr.responseText);
            }

            return {};
        }
    };
    xhr.send(JSON.stringify(data));
}