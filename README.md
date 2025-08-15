# Movie Recommender System

This project is a content-based movie recommender system that suggests movies similar to a user-selected title. It uses movie metadata and natural language processing techniques to compute similarity between movies, helping users discover new films based on their interests.

## Features

- Content-based recommendations using movie overviews, genres, and cast
- Fast similarity search with precomputed vectors
- Interactive web interface built with Streamlit
- Utilizes TMDB 5000 Movies and Credits datasets

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd movie_recommender
   ```

2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv movie_venv
   movie_venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the App

Start the Streamlit app with:
```sh
streamlit run app.py
```

The app will open in your browser. Select a movie to get recommendations.

## Project Structure

- `app.py` — Streamlit web app
- `movie_recommender_system.ipynb` — Data processing and model notebook
- `movies.pkl`, `movies_dict.pkl`, `similarity.pkl` — Preprocessed data and similarity matrix
- `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv` — Raw datasets
- `requirements.txt` — Python dependencies

## License

For educational purposes only.