import unittest
import hashlib
from app import hash_password

class TestApp(unittest.TestCase):
    def test_hash_password(self):
        password = "test123"
        expected_hash = hashlib.sha256(password.encode()).hexdigest()
        self.assertEqual(hash_password(password), expected_hash)

    def test_hash_password_empty(self):
        password = ""
        expected_hash = hashlib.sha256(password.encode()).hexdigest()
        self.assertEqual(hash_password(password), expected_hash)

if __name__ == '__main__':
    unittest.main()
