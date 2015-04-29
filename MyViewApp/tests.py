from django.test import TestCase

class TestCalls(TestCase):
    def test_call_view_denies_anonymous(self):
        response = self.client.get('/api/tasks/', follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/myPanel/addData/', follow=True)
        self.assertEqual(response.status_code, 200)

