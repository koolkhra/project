from django.test import TestCase, Client
from django.urls import reverse

class SaveLocationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_save_location(self):
        response = self.client.get(reverse('save_location'), {
            'lat': '35.6895',
            'long': '139.6917',
            'user_agent': 'Mozilla/5.0',
        }, REMOTE_ADDR='127.0.0.1')

        self.assertEqual(response.status_code, 200)
        with open('location.txt', 'r') as file:
            content = file.read()
            self.assertIn('lat: 35.6895', content)
            self.assertIn('long: 139.6917', content)
            self.assertIn('user_agent: Mozilla/5.0', content)
            self.assertIn('ip: 127.0.0.1', content)
