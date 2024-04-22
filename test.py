import unittest
from unittest.mock import patch
from app import app
from app import get_data

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # Testy dla strony głównej
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'JSONPlaceholder App', response.data)

    # Testy dla strony z postami
    def test_posts(self):
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Posts', response.data)

    # Testy dla strony z komentarzami
    def test_comments(self):
        response = self.app.get('/comments')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comments', response.data)

    # Testy dla strony z albumami
    def test_albums(self):
        response = self.app.get('/albums')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Albums', response.data)

    # Testy dla strony z zdjęciami
    def test_photos(self):
        response = self.app.get('/photos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Photos', response.data)

    # Testowanie obsługi błędów
    def test_error_handling(self):
        response = self.app.get('/nonexistent-page')
        self.assertEqual(response.status_code, 500)

class TestContract(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_contract(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'JSONPlaceholder App', response.data)

    def test_posts_contract(self):
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Posts', response.data)
        self.assertIn(b'id', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'id'
        self.assertIn(b'title', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'title'

    def test_comments_contract(self):
        response = self.app.get('/comments')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comments', response.data)
        self.assertIn(b'id', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'id'
        self.assertIn(b'name', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'name'
        self.assertIn(b'body', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'body'

    def test_albums_contract(self):
        response = self.app.get('/albums')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Albums', response.data)
        self.assertIn(b'id', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'id'
        self.assertIn(b'title', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'title'

    def test_photos_contract(self):
        response = self.app.get('/photos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Photos', response.data)
        self.assertIn(b'id', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'id'
        self.assertIn(b'title', response.data)  # Sprawdzenie, czy odpowiedź zawiera pole 'title'

    @patch('app.requests.get')
    def test_get_data_contract(self, mock_get):
        # Ustawienie zwracanej wartości dla mockowanego zapytania HTTP
        mock_get.return_value.json.return_value = [{'id': 1, 'title': 'Test Post'}]

        # Wywołanie testowanej funkcji
        data = get_data('posts')

        # Sprawdzenie, czy funkcja zwraca oczekiwane dane
        self.assertEqual(data, [{'id': 1, 'title': 'Test Post'}])

        # Sprawdzenie, czy zapytanie do zewnętrznego serwisu zostało wykonane z odpowiednimi parametrami
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts', params={})


if __name__ == '__main__':
    unittest.main()
