import unittest, time, requests, json
from unittest import TestCase

class TestLogin(TestCase):
    def setUp(self):
        self.ip = "http://127.0.0.1:5000"
        self.rs = requests.Session()
        self.startTime = time.time()

    def tearDown(self):
        self.rs.cookies.clear()
        self.rs.close()
        time_elapsed = time.time() - self.startTime
        print("completed in %.5f seconds" % (time_elapsed))

    def test_get_root(self):
        response = self.rs.get(self.ip)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("HELLO WORLD" in response.text, True)

    def test_get_without_credentials(self): 
        response = self.rs.get(self.ip + "/login")
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Complete the fields above." in response.text, True)

    def test_post_with_valid_credentials(self): 
        data = {"username": "hello", "password": "hello"}
        response = self.rs.post(self.ip + "/login", data=data) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual("You have successfully logged in!" in response.text, True)

    def test_post_with_invalid_credentials(self):
        data = {"username": "hello", "password": "hell"}
        response = self.rs.post(self.ip + "/login", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("The username/password could not be found. Please try again." in response.text, True)

    def test_post_with_empty_credentials(self):
        data = {"username": "", "password": ""}
        response = self.rs.post(self.ip + "/login", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Some fields are missing. Please try again." in response.text, True)

    def test_post_with_missing_username(self):
        data = {"password": "hello"}
        response = self.rs.post(self.ip + "/login", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Invalid request. Please try again." in response.text, True)

    def test_post_with_missing_password(self):
        data = {"username": "hello"}
        response = self.rs.post(self.ip + "/login", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Invalid request. Please try again." in response.text, True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
