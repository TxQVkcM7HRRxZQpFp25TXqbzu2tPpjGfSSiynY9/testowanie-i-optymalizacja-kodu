from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Funkcja do pobierania danych z API JSONPlaceholder
def get_data(endpoint, limit=None):
    params = {'_limit': limit} if limit else {}
    response = requests.get(f'https://jsonplaceholder.typicode.com/{endpoint}', params=params)
    return response.json()

# Obsługa błędów
@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error('An error occurred: %s', e)
    return 'An error occurred. Please try again later.', 500

# Strona główna
@app.route('/')
def index():
    return render_template('index.html')

# Podstrona z postami
@app.route('/posts')
def posts():
    # Pobierz parametry GET
    min_chars = request.args.get('min_chars')
    max_chars = request.args.get('max_chars')

    posts_data = get_data('posts')

    # Jeśli są podane parametry min_chars i max_chars, przefiltruj posty
    if min_chars and max_chars:
        posts_data = [post for post in posts_data if len(post['body']) >= int(min_chars) and len(post['body']) <= int(max_chars)]

    return render_template('posts.html', posts=posts_data)

@app.route('/comments')
def comments():
    # Pobierz parametr limit zapytania GET
    limit = request.args.get('limit', default=None, type=int)

    # Pobierz dane z API JSONPlaceholder, uwzględniając limit
    comments_data = get_data('comments', limit=limit)

    # Ustaw domyślną wartość limitu, jeśli nie została podana
    limit = limit

    return render_template('comments.html', comments=comments_data, limit=limit)


@app.route('/albums')
def albums():
    albums_data = get_data('albums')
    return render_template('albums.html', albums=albums_data)

@app.route('/photos')
def photos():
    photos_data = get_data('photos')
    return render_template('photos.html', photos=photos_data)

if __name__ == '__main__':
    app.run(debug=True)
