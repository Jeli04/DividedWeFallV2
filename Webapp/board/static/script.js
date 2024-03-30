document.addEventListener('DOMContentLoaded', function() {
    console.log("listening")
    // url listener
    //! come back to this
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
        .then(data => {
            document.getElementById("outputBox").innerText = data.result;
        });
    });
});

