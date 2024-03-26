document.addEventListener('DOMContentLoaded', function() {
    // url listener
    //! come back to this
    const analyzeButton = document.getElementById('analyzeButton');
    if (analyzeButton) {
        analyzeButton.addEventListener('click', function() {
            const urlInput = document.getElementById('urlInput').value;
            console.log('URL submitted:', urlInput);
            
        });
    }
});
