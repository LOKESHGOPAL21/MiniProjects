from flask import Flask, render_template, request, jsonify
import pandas as pd
import ast
import time
import sys
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Optional: Uncomment if your frontend is on a different domain
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)  # Uncomment if needed

# Load datasets
movies = pd.read_csv('tmdb_5000_credits.csv')
ratings = pd.read_csv('tmdb_5000_movies.csv')

# Merge datasets
merged_df = movies.merge(ratings, left_on='movie_id', right_on='id')
merged_df.drop(columns=['id', 'original_title'], inplace=True)

# Helper functions to extract structured information
def extract_top_cast(cast_str):
    try:
        cast = ast.literal_eval(cast_str)
        return [actor['name'] for actor in cast[:3]]
    except:
        return []

def extract_director(crew_str):
    try:
        crew = ast.literal_eval(crew_str)
        for person in crew:
            if person['job'] == 'Director':
                return person['name']
    except:
        return None

def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre['name'] for genre in genres]
    except:
        return []

def extract_keywords(kw_str):
    try:
        keywords = ast.literal_eval(kw_str)
        return [kw['name'] for kw in keywords]
    except:
        return []

# Apply feature extraction
merged_df['top_cast'] = merged_df['cast'].apply(extract_top_cast)
merged_df['director'] = merged_df['crew'].apply(extract_director)
merged_df['genre_names'] = merged_df['genres'].apply(extract_genres)
merged_df['keyword_list'] = merged_df['keywords'].apply(extract_keywords)

# Generate poster URL (static placeholder style)
def get_poster_url(movie_id):
    base_url = "https://image.tmdb.org/t/p/w500"
    return f"{base_url}/{movie_id}.jpg"

# Recommendation model v1 - CountVectorizer
def recommend_v1(movie_title):
    merged_df['tags'] = merged_df['genre_names'].astype(str) + ' ' + \
                        merged_df['top_cast'].astype(str) + ' ' + \
                        merged_df['director'].astype(str)

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(merged_df['tags'].values.astype('U')).toarray()

    similarity = cosine_similarity(vectors)
    similarity_sparse = csr_matrix(similarity)

    start_time = time.time()
    similarity_sparse = csr_matrix(similarity)
    conversion_time = time.time() - start_time

    dense_memory = sys.getsizeof(similarity)
    sparse_memory = similarity_sparse.data.nbytes + similarity_sparse.indptr.nbytes + similarity_sparse.indices.nbytes

    matched_movies = merged_df[merged_df['title_x'] == movie_title]
    if matched_movies.empty:
        raise ValueError(f"Movie '{movie_title}' not found in the database.")

    idx = matched_movies.index[0]
    distances = list(enumerate(similarity[idx]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i in sorted_movies:
        movie = merged_df.iloc[i[0]]
        recommendations.append({
            'title': movie['title_x'],
            'director': movie['director'],
            'cast': movie['top_cast'],
            'rating': movie['vote_average'],
            'poster': get_poster_url(movie['movie_id']),
        })

    return recommendations, conversion_time, dense_memory / 1024, sparse_memory / 1024

# Recommendation model v2 - TF-IDF Vectorizer with more features
def recommend_v2(movie_title):
    merged_df['tags'] = merged_df['genre_names'].astype(str) + ' ' + \
                        merged_df['top_cast'].astype(str) + ' ' + \
                        merged_df['director'].astype(str) + ' ' + \
                        merged_df['overview'].astype(str) + ' ' + \
                        merged_df['original_language'].astype(str)

    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    vectors = tfidf.fit_transform(merged_df['tags'].values.astype('U')).toarray()

    similarity = cosine_similarity(vectors)
    similarity_sparse = csr_matrix(similarity)

    start_time = time.time()
    similarity_sparse = csr_matrix(similarity)
    conversion_time = time.time() - start_time

    dense_memory = sys.getsizeof(similarity)
    sparse_memory = similarity_sparse.data.nbytes + similarity_sparse.indptr.nbytes + similarity_sparse.indices.nbytes

    matched_movies = merged_df[merged_df['title_x'] == movie_title]
    if matched_movies.empty:
        raise ValueError(f"Movie '{movie_title}' not found in the database.")

    idx = matched_movies.index[0]
    distances = list(enumerate(similarity[idx]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i in sorted_movies:
        movie = merged_df.iloc[i[0]]
        recommendations.append({
            'title': movie['title_x'],
            'director': movie['director'],
            'cast': movie['top_cast'],
            'rating': movie['vote_average'],
            'poster': get_poster_url(movie['movie_id']),
        })

    return recommendations, conversion_time, dense_memory / 1024, sparse_memory / 1024

# Model dispatcher
def get_recommendations(movie_title, model_type):
    if model_type == 'v1':
        return recommend_v1(movie_title)
    elif model_type == 'v2':
        return recommend_v2(movie_title)
    else:
        raise ValueError("Invalid model_type. Choose 'v1' or 'v2'.")

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    movie_title = data.get('movie_title')
    model_type = data.get('model_type')

    if not movie_title or not model_type:
        return jsonify({'error': 'Missing movie title or model type'}), 400

    # Check if the model_type is valid
    if model_type not in ['v1', 'v2']:
        return jsonify({'error': 'Invalid model_type. Choose "v1" or "v2".'}), 400

    try:
        recommendations, conv_time, dense_mem, sparse_mem = get_recommendations(movie_title, model_type)
        return jsonify({
            'recommendations': recommendations,
            'conversion_time': conv_time,
            'dense_memory': dense_mem,
            'sparse_memory': sparse_mem
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
