// Inside script.js
document.addEventListener('DOMContentLoaded', function() {
    const analyzeButton = document.getElementById('analyzeButton');
    analyzeButton.addEventListener('click', function() {
        const urlInput = document.getElementById('urlInput').value;
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({url: urlInput}),
        })
        .then(response => response.json())
        .then(data => {
            // Update this part to display your scores appropriately
            document.getElementById('outputBox').textContent = 'Bias scores: ' + JSON.stringify(data.scores);
        })
        .catch(error => console.error('Error:', error));
    });
});
