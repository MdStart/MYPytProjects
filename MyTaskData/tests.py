from django.test import TestCase
from .models import MyData
from django.utils import timezone
from django.core.urlresolvers import reverse


# models test
class MyTaskData(TestCase):

    def create_myData(self,device_name="only a test",magnification=22,field_of_view=10,range=20):
        return MyData.objects.create(device_name=device_name,magnification=magnification,field_of_view=field_of_view, range=range)

    def test_myData_creation(self):
        w = self.create_myData()
        self.assertTrue(isinstance(w, MyData))


    # views (uses reverse)
    def test_whatever_list_view(self):
        w = self.create_myData()
        url = reverse("MyTaskData.views.task_list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

