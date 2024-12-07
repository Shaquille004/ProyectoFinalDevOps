import unittest

class TestIndexPage(unittest.TestCase):
    def test_header(self):
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("<h1>Hola Mundo</h1>", content, "El encabezado no contiene 'Hola Mundo'")

if __name__ == "__main__":
    unittest.main()
