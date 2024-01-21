async function sendHttpRequest() {
    document.getElementById('loadingMessage').style.display = 'block';
    document.body.style.overflow = 'hidden';

    var data = {
        "text": document.getElementById('inputText').value
    }

    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    await fetch("http://127.0.0.1:8000/summarize/bert", requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(responseData => {
            document.getElementById('bertText').value = responseData;
        })
        .catch(error => {
            document.getElementById('bertText').value = `Fetch error: ${error}`;
        })

    await fetch("http://127.0.0.1:8000/summarize/destilbert", requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(responseData => {
            document.getElementById('destilbertText').value = responseData;
        })
        .catch(error => {
            document.getElementById('destilbertText').value = `Fetch error: ${error}`;
        })

    await fetch("http://127.0.0.1:8000/summarize/t5", requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(responseData => {
            document.getElementById('t5_smallText').value = responseData;
        })
        .catch(error => {
            document.getElementById('t5_smallText').value = `Fetch error: ${error}`;
        })
    document.getElementById('loadingMessage').style.display = 'none';
}