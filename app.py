from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "864c293f"

@app.route('/api/movies', methods=['GET'])
def get_movies():
    # Fetch popular movies matching 'marvel' from OMDb
    url = f"http://www.omdbapi.com/?s=marvel&type=movie&apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        movies = []
        for movie in data.get('Search', [])[:10]:
            movies.append({
                'id': movie.get('imdbID'),
                'title': movie.get('Title'),
                'overview': f"Release Year: {movie.get('Year')}",
                'poster_path': movie.get('Poster'),
                'vote_average': 'N/A'
            })
        return jsonify({"status": "success", "movies": movies})
    else:
        return jsonify({"status": "error", "message": "Failed to fetch movies"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)