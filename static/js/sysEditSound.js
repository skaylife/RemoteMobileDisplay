
// function updateTextInput(val) {
//     document.getElementById("textInput").value = val;
//     sendData(val)
// }

// function sendData(value) {
//     const xhr = new XMLHttpRequest();
//     xhr.open("POST", "/sys_sounds", true);
//     xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

//     xhr.onreadystatechange = function() {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             document.getElementById('result').textContent = xhr.responseText;
//         }
//     };

//     const data = JSON.stringify({ sounds_position: value });
//     xhr.send(data);
//     console.log(value)
//     console.log(data)
// }

// function updateTextInput(val) {
//     document.getElementById('textInput').value = val;
//     sendValueToServer(val);
// }

function updateTextInput(value) {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/sys_sounds", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('positionHtml').textContent = xhr.responseText;
        }
    };

    xhr.send("sounds_position=" + value);
}

console.log("================================")