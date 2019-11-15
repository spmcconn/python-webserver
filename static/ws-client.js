$(function () {
    const ws = new WebSocket(`ws://${location.host}/ws`);

    ws.onopen = function () {
        console.log("Connected");
    }

    ws.onmessage = function (evt) {
        const response = JSON.parse(evt.data);
        console.log(response);

        $(`#list-${response.list}`).prepend(`<li class="list-group-item">${response.date}</li>`);

        if($(`#list-${response.list} .list-group-item`).length > 5) $(`#list-${response.list} .list-group-item:last-child`).remove();
    }

    ws.onclose = function () {
        console.log("Connected closed...");
    }

    $("#addison-btn").on("click", function() {
        ws.send("addison");
    });

    $("#andi-btn").on("click", function() {
        ws.send("andi");
    });

    $("#kitties-btn").on("click", function() {
        ws.send("kitties");
    });
});