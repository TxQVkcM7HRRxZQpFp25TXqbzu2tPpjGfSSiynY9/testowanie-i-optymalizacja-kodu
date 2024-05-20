from flask import Flask, render_template, request
import requests
from memory_profiler import profile
import cProfile
import io
import pstats
from pstats import SortKey
import logging

app = Flask(__name__)


# Funkcja do pobierania danych z API JSONPlaceholder z profilowaniem pamięci
@profile
def get_data(endpoint, limit=None):
    params = {'_limit': limit} if limit else {}
    response = requests.get(f'https://jsonplaceholder.typicode.com/{endpoint}', params=params)
    return response.json()


# Obsługa błędów
@app.errorhandler(Exception)
@profile
def handle_error(e):
    app.logger.error('An error occurred: %s', e)
    return 'An error occurred. Please try again later.', 500


# Strona główna
@app.route('/')
@profile
def index():
    return render_template('index.html')


# Podstrona z postami
@app.route('/posts')
@profile
def posts():
    # Pobierz parametry GET
    min_chars = request.args.get('min_chars')
    max_chars = request.args.get('max_chars')

    posts_data = get_data('posts')

    # Jeśli są podane parametry min_chars i max_chars, przefiltruj posty
    if min_chars and max_chars:
        posts_data = [post for post in posts_data if
                      len(post['body']) >= int(min_chars) and len(post['body']) <= int(max_chars)]

    return render_template('posts.html', posts=posts_data)


# Podstrona z komentarzami
@app.route('/comments')
@profile
def comments():
    # Pobierz parametr limit zapytania GET
    limit = request.args.get('limit', default=None, type=int)

    # Pobierz dane z API JSONPlaceholder, uwzględniając limit
    comments_data = get_data('comments', limit=limit)

    return render_template('comments.html', comments=comments_data, limit=limit)


# Podstrona z albumami
@app.route('/albums')
@profile
def albums():
    albums_data = get_data('albums')
    return render_template('albums.html', albums=albums_data)


# Podstrona ze zdjęciami
@app.route('/photos')
@profile
def photos():
    photos_data = get_data('photos')
    return render_template('photos.html', photos=photos_data)


if __name__ == '__main__':
    # Ustawienia logowania
    logging.basicConfig(level=logging.DEBUG)

    # Uruchomienie profilowania CPU
    profiler = cProfile.Profile()
    profiler.enable()

    try:
        app.run(debug=True)
    finally:
        profiler.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        with open('profiling_results.txt', 'w') as f:
            f.write(s.getvalue())
