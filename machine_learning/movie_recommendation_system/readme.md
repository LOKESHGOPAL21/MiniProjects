Here is a detailed and well-structured README for your GitHub repository:

---

# Movie Recommendation System

Welcome to the Movie Recommendation System repository! This system is designed to provide movie recommendations based on a given movie title. It offers two model options for generating recommendations: CountVectorizer and TF-IDF, which help determine similarities between movies based on their metadata.

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)

  * [Frontend](#frontend)
  * [Backend](#backend)
* [API Endpoints](#api-endpoints)
* [Performance Metrics](#performance-metrics)
* [Contributing](#contributing)
* [License](#license)

---

## Project Overview

This repository contains both the frontend and backend code for a movie recommendation system. The backend is built using **Flask** (Python), and the frontend is developed with **HTML**, **CSS**, and **JavaScript**.

The system uses a content-based filtering approach to recommend movies by analyzing their metadata. The user can input the name of a movie and choose between two recommendation models: CountVectorizer or TF-IDF. The system will return a list of recommended movies, including details such as the movie's title, director, cast, rating, and poster.

---

## Features

* **Movie Recommendations**: Enter a movie title to receive personalized movie suggestions.
* **Model Options**: Choose between two models: `v1` (CountVectorizer) or `v2` (TF-IDF).
* **Performance Metrics**: View the time taken for the recommendation process and memory usage (dense and sparse).
* **Responsive Design**: The frontend is designed to be mobile-friendly and provides a smooth user experience.

---

## Technologies Used

* **Backend**:

  * Flask (Python)
  * JSON for data exchange

* **Frontend**:

  * HTML5
  * CSS3
  * JavaScript (Vanilla)
  * Fetch API for asynchronous communication with the server

---

## Installation

Follow the steps below to set up the project locally.

### Prerequisites

Before running the project, ensure you have the following installed:

* Python (>=3.7)
* pip (Python package installer)

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Set Up the Backend (Flask)

Navigate to the backend directory and set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Install Frontend Dependencies

Ensure the frontend files (HTML, CSS, and JS) are in the appropriate directory (`static/` for stylesheets and scripts). The frontend does not require additional installation steps if you're using the provided static files.

---

## Usage

### Frontend

The frontend is built using plain HTML, CSS, and JavaScript. The main file is `index.html`, which provides the form where users can input a movie title and select a model type (CountVectorizer or TF-IDF).

#### How to Use the Frontend:

1. Open `index.html` in a web browser.
2. Enter a movie title in the input field.
3. Select the desired model type (`v1` or `v2`).
4. Click the "Get Recommendations" button to submit the form.

The page will show a list of recommended movies along with their details such as director, cast, rating, and a poster.

### Backend

To run the backend, navigate to the project root directory and start the Flask development server:

```bash
python app.py
```

The backend will run on `http://localhost:5000`, and the frontend will make API calls to the `/recommend` endpoint to get movie recommendations.

---

## API Endpoints

### `/recommend` (POST)

This endpoint accepts a POST request with the following JSON body:

```json
{
  "movie_title": "Movie Title",
  "model_type": "v1" or "v2"
}
```

* **movie\_title** (string): The title of the movie for which you want recommendations.
* **model\_type** (string): Choose between `v1` (CountVectorizer) or `v2` (TF-IDF).

#### Response:

The response will be a JSON object containing movie recommendations along with performance metrics:

```json
{
  "recommendations": [
    {
      "title": "Movie Title",
      "director": "Director Name",
      "cast": ["Actor 1", "Actor 2"],
      "rating": "IMDB Rating",
      "poster": "URL to Movie Poster"
    },
    ...
  ],
  "conversion_time": 0.234567,
  "dense_memory": 512.34,
  "sparse_memory": 123.45
}
```

* **recommendations**: List of recommended movies.
* **conversion\_time**: The time taken to generate the recommendations (in seconds).
* **dense\_memory**: Memory usage (in KB) for the dense matrix.
* **sparse\_memory**: Memory usage (in KB) for the sparse matrix.

#### Errors:

If there is an issue with the request (e.g., missing or invalid data), the response will be an error message:

```json
{
  "error": "Invalid model_type. Choose 'v1' or 'v2'."
}
```

---

## Performance Metrics

* **Conversion Time**: Time taken to generate movie recommendations based on the selected model.
* **Memory Usage**: The amount of memory used by the system during the recommendation process. The memory usage is categorized into dense and sparse memory.




Feel free to adjust this README according to your specific project and repository details. This structure should help other developers quickly understand your project and how to set it up and contribute to it.
