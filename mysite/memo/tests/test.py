from django.test import TestCase,Client
from memo.models import Memo,Tips
import json

# Create your tests here.

class MyTest(TestCase):
    fixtures = ['app']
    def setUp(self):
        m = Memo.objects.get_or_create(memo_text="fugaaaa")
        print(m)

    def test_a(self):
        print("test a")
        c = Client()
        response = c.get('/memo/api/memos/', {} )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        

