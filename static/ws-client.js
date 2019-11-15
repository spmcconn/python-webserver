$(function () {
    const ws = new WebSocket(`ws://${location.host}/ws`);

    ws.onopen = function () {
        console.log("Connected");
    }

    ws.onmessage = function (evt) {
        const response = JSON.parse(evt.data);
        console.log(response);

        $(`#list-${response.list}`).prepend(`<li class="list-group-item">${response.date}</li>`);
    }

    ws.onclose = function () {
        console.log("Connected closed...");
    }
});