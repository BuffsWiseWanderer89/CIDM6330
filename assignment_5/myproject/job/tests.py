from django.test import TestCase
from django.urls import reverse
from job.models import User
from ninja.testing import TestClient
from myproject.api import api

# Create your tests here.

class UserAPITests(TestCase):
    def setUp(self):
        self.client = TestClient(api)
        self.user = User.objects.create(
            username="johndoeadeer",
            user_id=999,
            role="admin",
            email="afemaledear@rayadropofgoldensun.com"
        )
    
    def test_trigger_welcome_email(self):
        response = self.client.post(f"/users/send-welcome/{self.user.id}"
        self.assertEqual(response.status_code, 200)
        self.assertIn("queued", response.json()["message"])

    def test_trigger_user_report(self):
        response = self.client.post(f"/users/generate-report")
        self.assertEqual(response.status_code, 200)
        self.assertIn("task_id", response.json())
                               