
function updateTextInput(val) {
    document.getElementById("textInput").value = val;
    sendData(val)
}

function sendData(value) {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/sys_sounds", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('result').textContent = xhr.responseText;
        }
    };

    const data = JSON.stringify({ sounds_position: value });
    xhr.send(data);
    console.log(value)
    console.log(data)
}

console.log("================================")