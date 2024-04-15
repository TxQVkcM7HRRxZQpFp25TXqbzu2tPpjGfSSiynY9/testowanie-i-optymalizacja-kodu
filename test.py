import unittest
from app import app

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
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
