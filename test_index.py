from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        service = Service(r"C:\Users\shaqu\Desktop\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def test_title(self):
        self.driver.get("http://localhost:9000")
        self.assertEqual(self.driver.title, "Hola Mundo")

    def test_heading(self):
        self.driver.get("http://localhost:9000")
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(heading.text, "Hola Mundo")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
