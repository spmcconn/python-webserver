$(function () {
    const ws = new WebSocket(`ws://${location.host}/ws`);

    ws.onopen = function () {
        console.log("Connected");
    }

    ws.onmessage = function (evt) {
        const response = JSON.parse(evt.data);
        console.log(response);

        let date = new Date(response.date).toLocaleString();

        $(`#list-${response.list}`).prepend(`<li class="list-group-item">${date}</li>`);
    }

    ws.onclose = function () {
        console.log("Connected closed...");
    }
});