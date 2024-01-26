import unittest
from django.test import Client


class QRCodePhoneGeneratorTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        body = {"type": "phone", "country_code": "55", "phone": "51999326264"}
        response = self.client.post("/qr-code-generator/", body)
        # # Issue a GET request.
        # response = self.client.get("/customer/details/")
        #
        # # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        #
        # # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context["customers"]), 5)
