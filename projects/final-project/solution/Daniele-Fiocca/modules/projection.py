import json


def load_projections():
    projections = json.load(open("projections.json"))
    return projections


def display_projections():
    movie = load_projections()
    for i, movie in enumerate(movie, start=1):
        print(
            f"\n{i}. Title: {movie['title']}\nTime: {movie['time']}\nTheater: {movie['theater']}\nAvailable seats: {movie['available_seats']} "
        )


def save_projections(projections):
    with open("projections.json", "w") as f:
        json.dump(projections, f, indent=2)
