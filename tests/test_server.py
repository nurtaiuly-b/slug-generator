import sys, os, threading, unittest, urllib.request, urllib.error, urllib.parse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from server import make_server


class TestService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = make_server(0)
        cls.port = cls.srv.server_address[1]
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()

    def get(self, path):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{self.port}{path}") as r:
                return r.status, r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            e.close()
            return e.code, ""

    def test_healthz_is_ok(self):
        status, body = self.get("/healthz")
        self.assertEqual(status, 200)
        self.assertTrue(body.strip())

    def test_slug_english(self):
        q = urllib.parse.quote("Hello World!")
        self.assertEqual(self.get(f"/slug?text={q}"), (200, "hello-world"))

    def test_slug_cyrillic(self):
        q = urllib.parse.quote("Актау Город")
        self.assertEqual(self.get(f"/slug?text={q}"), (200, "aktau-gorod"))

    def test_slug_empty_is_400(self):
        self.assertEqual(self.get("/slug?text=")[0], 400)