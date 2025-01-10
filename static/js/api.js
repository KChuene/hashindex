const api = "/api";

export function get(handler) {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", api, true);
    xhr.onreadystatechange = () => {
        var jsonre = null;
        if(xhr.readyState == XMLHttpRequest.DONE) {
            const status = xhr.status;

            if(status === 0 || (200 <= status && status < 400)) {
                jsonre = JSON.parse(xhr.responseText);
            }
        }

        handler(jsonre);
    };
    xhr.send();
}

export function add(data, handler) {
    var xhr = new XMLHttpRequest();

    xhr.open("POST", api, true);
    xhr.onreadystatechange = () => {
        var jsonre = null;
        if(xhr.readyState == XMLHttpRequest.DONE) {
            const status = xhr.status;

            if(status === 0 || (200 <= status && status < 400)) {
                jsonre = JSON.parse(xhr.responseText);
            }
        }

        handler(jsonre);
    };
    xhr.send(JSON.stringify(data));
}