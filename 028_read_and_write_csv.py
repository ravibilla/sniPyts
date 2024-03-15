# Read and write csv files
import pandas as pd

data = {
    "Movie": ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Godfather Part II", "12 Angry Men"], 
    "Year": [1994, 1972, 2008, 1974, 1957], 
    "Duration": ["2h 22m", "2h 55m", "2h 32m", "3h 22m", "1h 36m"]
    }
data =pd.DataFrame(data)
data.to_csv("./files/movie_data.csv", index=False)

top_5_movies = pd.read_csv("./files/movie_data.csv")
top_5_movies.head()