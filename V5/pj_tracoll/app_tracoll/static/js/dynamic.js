function setAsFinished(id) {
    const xhttp = new XMLHttpRequest();

    xhttp.onload = function () {
        const response = JSON.parse(this.responseText);
        console.log(response);
        const spanElement = document.getElementById("span-" + id);
        const paraElement = document.getElementById("para-" + id);

        spanElement.innerHTML = response.new_button;
        paraElement.innerHTML = response.new_status;
        paraElement.className = response.new_style;
    };

    xhttp.open("GET", "/set_text_as_finished/" + id);
    xhttp.send();
}
