from unittest import TestCase, main as main_test
from fastapi.testclient import TestClient
from app import app


class TestBackend(TestCase):
    
    def setUp(self) -> None:
        self.app = TestClient(app)
    
    def test_url_parse_endpoint(self):
        response = self.app.get("/get_site/python")
        self.assertEqual(response.status_code, 200)
    
    def test_url_parse_answer(self):
        data = {
            "Developer": "Python Software Foundation",
            "OS": "\nTier 1: 64-bit Linux, macOS; 64- and 32-bit Windows 10+[5]\nTier 2: E.g. 32-bit WebAssembly (WASI)\nTier 3: 64-bit FreeBSD, iOS; e.g. Raspberry Pi OSUnofficial (or has been known to work): Other Unix-like/BSD variants and e.g. Android 5.0+ (official from Python 3.13 planned[6]) and a few other platforms[7][8][9]\n",
            "License": "Python Software Foundation License"
        }
        response = self.app.get("/get_site/python")
        self.assertEqual(response.json(), data)



if __name__ == "__main__":
    main_test()