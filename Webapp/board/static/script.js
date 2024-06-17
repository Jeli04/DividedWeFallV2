document.addEventListener('DOMContentLoaded', function() {
    console.log("listening");
    var chartInstance = null;  // Keep a reference to the chart instance

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
            var outputBox = document.getElementById('outputBox');
            var pieChart = document.getElementById('pieChart');
            var errorMessage = document.getElementById('errorMessage');

            if (data.error) {
                outputBox.textContent = '';
                pieChart.style.display = 'none';
                errorMessage.style.display = 'block';
                errorMessage.textContent = 'There is an error with your link, or it may not be scrapable. Please try again.';
            } else {
                errorMessage.style.display = 'none';
                outputBox.textContent = '';
                pieChart.style.display = 'block';

                if (chartInstance) {
                    chartInstance.destroy();  // Destroy the existing chart instance
                }
                chartInstance = renderChart(data['Non-biased'], data['Biased']);  // Create a new chart instance
            }
        })
        .catch(error => {
            var outputBox = document.getElementById('outputBox');
            var pieChart = document.getElementById('pieChart');
            var errorMessage = document.getElementById('errorMessage');

            outputBox.textContent = '';
            pieChart.style.display = 'none';
            errorMessage.style.display = 'block';
            errorMessage.textContent = 'An error occurred: ' + error.message;
        });
    });

    function renderChart(nonBiased, biased) {
        var ctx = document.getElementById('pieChart').getContext('2d');
        return new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Non-biased', 'Biased'],
                datasets: [{
                    data: [nonBiased, biased],
                    backgroundColor: ['#4d9dff', '#ff4d4d']
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                var total = context.dataset.data.reduce((acc, value) => acc + value, 0);
                                var value = context.raw;
                                var percentage = (value / total * 100).toFixed(2) + '%';
                                return context.label + ': ' + percentage;
                            }
                        }
                    }
                }
            }
        });
    }
});
