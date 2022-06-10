from django.test import TestCase,Client
from .models import Memo,Tips
import json

# Create your tests here.

class MyTest(TestCase):
    fixtures = ['app']
    def setUp(self):
        m = Memo.objects.get_or_create(memo_text="fugaaaa")
        print(m)

    def test_a(self):
        c = Client()
        response = c.get('/memo/api/memos/', 
                         {},
                         HTTP_ACCEPT='application/json')

        print(response)
        print(json.loads(response.content))

