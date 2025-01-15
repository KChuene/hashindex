const api = "/api";

export function get(data, handler) {
    const url = `${api}?hash=${data}`;
    request("GET", url, null, handler);
}

export function add(data, handler) {
    request("POST", api, data, handler);
}

function request(method, url, data, handler) {
    var xhr = new XMLHttpRequest();

    xhr.open(method, url, true);
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