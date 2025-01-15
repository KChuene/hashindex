const api = "/api";

export function get(handler) {
    request("GET", null, handler);
}

export function add(data, handler) {
    request("POST", data, handler);
}

function request(method, data, handler) {
    var xhr = new XMLHttpRequest();

    xhr.open(method, api, true);
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
    xhr.send((data != null) ? JSON.stringify(data) : null);
}