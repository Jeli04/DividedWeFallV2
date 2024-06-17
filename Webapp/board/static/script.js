document.addEventListener('DOMContentLoaded', function() {
    console.log("listening")
    // URL listener
    document.getElementById('analyzeButton').addEventListener('click', function() {
        console.log('URL submitted:');
        var url = document.getElementById("urlInput").value;
        fetch('/inference', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({urlInput: url})
        })
        .then(response => response.json())  // Parse the response as JSON
        .then(data => {
            if (data.error) {
                document.getElementById('outputBox').textContent = 'Error: ' + data.error;
            } else {
                document.getElementById('outputBox').textContent = 'Bias scores: Non-biased: ' + data['Non-biased'] + ', Biased: ' + data['Biased'];
            }
        })
        .catch(error => {
            document.getElementById('outputBox').textContent = 'An error occurred: ' + error.message;
        });
    });
});
