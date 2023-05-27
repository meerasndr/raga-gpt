function sendData() {
    const raganum = parseInt(document.getElementById("raganum").value);    
    const data = {
        raganum: raganum,
    };
    
    fetch(`http://0.0.0.0:8000/${raganum}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const resultDiv = document.getElementById("result");
        console.log(result)
        resultDiv.innerHTML = ""
        const ragalist = result.message;
        ragalist.forEach((element, index) => {
            setTimeout(() => {
                resultDiv.innerHTML += `${index + 1}. ${element}<br>`;
            }, index * 10000);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
