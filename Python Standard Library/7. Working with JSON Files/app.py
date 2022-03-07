import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1993},
# ]

# data = json.dumps(movies)

data = Path(
    "D:\DEV\CWM Python\Python Standard Library\\7. Working with JSON Files\movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
