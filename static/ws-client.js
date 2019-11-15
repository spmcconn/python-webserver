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

        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour12: true, hour: "numeric", minute: "numeric" };
        const date = new Date(response.date * 1000).toLocaleString("en-US", options);

        $(`#list-${response.list}`).prepend(`<li class="list-group-item">${date}</li>`);
    }

    ws.onclose = function () {
        console.log("Connected closed...");
    }
});