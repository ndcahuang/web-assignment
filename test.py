import unittest, json, time
from main import app

class TestAuth(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.startTime = time.time()

    def tearDown(self):
        elapsed = time.time() - self.startTime
        print("completed %s in %.5f seconds" % (self.id(), elapsed))

    def test_get_root(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertIn(b"HELLO WORLD", response.data)

    def test_get_page(self):
        response = self.client.get("/login")
        self.assertEqual(200, response.status_code)
        self.assertIn(b"STATE", response.data)
        self.assertIn(b"Complete the fields", response.data)
        self.assertIn(b"<label for=\"username\">", response.data)
        self.assertIn(b"<label for=\"password\">", response.data)
        self.assertIn(b"<input type=\"text\" class=\"form-control\" id=\"username\" name=\"username\"", response.data)
        self.assertIn(b"><input type=\"password\" class=\"form-control\" id=\"password\" name=\"password\"", response.data)
        self.assertIn(b"<button type=\"submit\" class=\"btn btn-primary\">SUBMIT</button>", response.data)

    def test_post_with_correct_data(self):
        response = self.client.post("/login", data=dict(username="admin", password="admin"))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"STATE", response.data)
        self.assertIn(b"successfully", response.data)
        self.assertIn(b"<label for=\"username\">", response.data)
        self.assertIn(b"<label for=\"password\">", response.data)
        self.assertIn(b"<input type=\"text\" class=\"form-control\" id=\"username\" name=\"username\"", response.data)
        self.assertIn(b"><input type=\"password\" class=\"form-control\" id=\"password\" name=\"password\"", response.data)
        self.assertIn(b"<button type=\"submit\" class=\"btn btn-primary\">SUBMIT</button>", response.data)

    def test_post_with_incorrect_data(self):
        response = self.client.post("/login", data=dict(username="hello", password="Hello"))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"STATE", response.data)
        self.assertIn(b"could not", response.data)
        self.assertIn(b"<label for=\"username\">", response.data)
        self.assertIn(b"<label for=\"password\">", response.data)
        self.assertIn(b"<input type=\"text\" class=\"form-control\" id=\"username\" name=\"username\"", response.data)
        self.assertIn(b"><input type=\"password\" class=\"form-control\" id=\"password\" name=\"password\"", response.data)
        self.assertIn(b"<button type=\"submit\" class=\"btn btn-primary\">SUBMIT</button>", response.data)

    def test_post_with_empty_data(self):
        response = self.client.post("/login", data=dict(username="", password=""))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"STATE", response.data)
        self.assertIn(b"Some fields are missing.", response.data)
        self.assertIn(b"<label for=\"username\">", response.data)
        self.assertIn(b"<label for=\"password\">", response.data)
        self.assertIn(b"<input type=\"text\" class=\"form-control\" id=\"username\" name=\"username\"", response.data)
        self.assertIn(b"><input type=\"password\" class=\"form-control\" id=\"password\" name=\"password\"", response.data)
        self.assertIn(b"<button type=\"submit\" class=\"btn btn-primary\">SUBMIT</button>", response.data)

    def test_post_with_insufficient_data(self):
        response = self.client.post("/login")
        self.assertEqual(200, response.status_code)
        self.assertIn(b"STATE", response.data)
        self.assertIn(b"Invalid", response.data)
        self.assertIn(b"<label for=\"username\">", response.data)
        self.assertIn(b"<label for=\"password\">", response.data)
        self.assertIn(b"<input type=\"text\" class=\"form-control\" id=\"username\" name=\"username\"", response.data)
        self.assertIn(b"><input type=\"password\" class=\"form-control\" id=\"password\" name=\"password\"", response.data)
        self.assertIn(b"<button type=\"submit\" class=\"btn btn-primary\">SUBMIT</button>", response.data)

    def test_post_with_insufficient_username(self):
        response = self.client.post("/login", data=dict(password="admin"))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"STATE", response.data)
        self.assertIn(b"Invalid", response.data)
        self.assertIn(b"<label for=\"username\">", response.data)
        self.assertIn(b"<label for=\"password\">", response.data)
        self.assertIn(b"<input type=\"text\" class=\"form-control\" id=\"username\" name=\"username\"", response.data)
        self.assertIn(b"><input type=\"password\" class=\"form-control\" id=\"password\" name=\"password\"", response.data)
        self.assertIn(b"<button type=\"submit\" class=\"btn btn-primary\">SUBMIT</button>", response.data)

    def test_post_with_insufficient_password(self):
        response = self.client.post("/login", data=dict(username="admin"))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"STATE", response.data)
        self.assertIn(b"Invalid", response.data)
        self.assertIn(b"<label for=\"username\">", response.data)
        self.assertIn(b"<label for=\"password\">", response.data)
        self.assertIn(b"<input type=\"text\" class=\"form-control\" id=\"username\" name=\"username\"", response.data)
        self.assertIn(b"><input type=\"password\" class=\"form-control\" id=\"password\" name=\"password\"", response.data)
        self.assertIn(b"<button type=\"submit\" class=\"btn btn-primary\">SUBMIT</button>", response.data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
