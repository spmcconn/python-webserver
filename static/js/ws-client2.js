$(function () {
    const ws = new WebSocket(`ws://${location.host}:81/ws`);

    ws.onopen = function () {
        console.log("Connected");
    }

    ws.onmessage = function (evt) {
        const response = JSON.parse(evt.data);

        $(`#list-${response.list}`).prepend(`<li class="list-group-item">${response.date}</li>`);

        if($(`#list-${response.list} .list-group-item`).length > 5) $(`#list-${response.list} .list-group-item:last-child`).remove();
    }

    ws.onclose = function () {
        console.log("Connected closed...");
    }

    $("#nick-btn").on("click", function() {
        ws.send("nick");
    });
});