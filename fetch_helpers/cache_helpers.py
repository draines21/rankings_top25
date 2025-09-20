import os, json

def load_or_fetch(filename, fetch_func):
    if os.path.exists(filename):
        with open(filename) as f:
            return json.load(f)
    data = fetch_func()
    with open(filename, "w") as f:
        json.dump(data, f)
    return data