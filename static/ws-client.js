$(function () {
    const ws = new WebSocket(`ws://${location.host}/ws`);

    ws.onopen = function () {
        console.log("Connected");
    }

    ws.onmessage = function (evt) {
        // const message = JSON.parse(evt.data);
        console.log(evt.data);
    }

    ws.onclose = function () {
        console.log("Connected closed...");
    }

    $("#press-me-btn").on("click", function() {
        ws.send(JSON.stringify({ message: "Hello World", date: new Date() }));
    });
});