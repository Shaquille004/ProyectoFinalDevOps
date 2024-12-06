import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def test_title(self):
        self.driver.get("http://localhost:9000")
        self.assertEqual(self.driver.title, "Hola Mundo")

    def test_heading(self):
        self.driver.get("http://localhost:9000")
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(heading.text.strip(), "Hola Mundo")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

