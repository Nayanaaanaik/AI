import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
movies = {
    'title': [
        'Avatar',
        'Titanic',
        'The Avengers',
        'Iron Man',
        'Interstellar',
        'The Dark Knight'
    ],
    'genre': [
        'Action Adventure Sci-Fi',
        'Romance Drama',
        'Action Superhero',
        'Action Superhero',
        'Sci-Fi Drama',
        'Action Crime Drama'
    ]
}

# Create DataFrame
df = pd.DataFrame(movies)

# Convert text into numerical vectors
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genre'])

# Calculate similarity
similarity = cosine_similarity(count_matrix)

# Function to recommend movies
def recommend(movie_name):
    if movie_name not in df['title'].values:
        print("Movie not found!")
        return

    index = df[df['title'] == movie_name].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nMovies similar to '{movie_name}':\n")

    for i in scores[1:4]:
        print(df.iloc[i[0]]['title'])

# User Input
movie = input("Enter a movie name: ")
recommend(movie)