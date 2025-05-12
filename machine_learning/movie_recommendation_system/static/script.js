document.getElementById('recommendation-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const movieTitle = document.getElementById('movie-title').value;
    const modelType = document.getElementById('model-type').value;

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            movie_title: movieTitle,
            model_type: modelType,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Display recommendations
        const recommendationsList = document.getElementById('recommendations-list');
        recommendationsList.innerHTML = '';  // Clear previous results

        data.recommendations.forEach(item => {
            const listItem = document.createElement('li');
            listItem.innerHTML = ` 
                <strong>${item.title}</strong><br>
                Director: ${item.director}<br>
                Cast: ${item.cast.join(', ')}<br>
                Rating: ${item.rating}<br>
                <img src="${item.poster}" alt="Poster" style="width: 100px; height: auto;">
            `;
            recommendationsList.appendChild(listItem);
        });

        // Display performance metrics
        document.getElementById('conversion-time').innerText = data.conversion_time.toFixed(6);
        document.getElementById('dense-memory').innerText = data.dense_memory.toFixed(2);
        document.getElementById('sparse-memory').innerText = data.sparse_memory.toFixed(2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
