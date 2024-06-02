import unittest
import requests

class TestAcceptance(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'

    def test_index(self):
        response = requests.get(f'{self.BASE_URL}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('JSONPlaceholder App', response.text)

    def test_posts(self):
        response = requests.get(f'{self.BASE_URL}/posts')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Posts', response.text)

    def test_comments(self):
        response = requests.get(f'{self.BASE_URL}/comments')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Comments', response.text)

    def test_albums(self):
        response = requests.get(f'{self.BASE_URL}/albums')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Albums', response.text)

    def test_photos(self):
        response = requests.get(f'{self.BASE_URL}/photos')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Photos', response.text)

    def test_nonexistent_page(self):
        response = requests.get(f'{self.BASE_URL}/nonexistent-page')
        self.assertEqual(response.status_code, 500)
        self.assertIn('An error occurred', response.text)

if __name__ == '__main__':
    unittest.main()
