$(function () {
    const days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ];

    const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

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