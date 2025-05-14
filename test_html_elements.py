from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest

class TestTasks(unittest.TestCase):
    BASE_URL = "http://10.48.10.107"  # your Flask app URL

    def setUp(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_tasks_present(self):
        driver = self.driver
        driver.get(self.BASE_URL)

        # Verify Test Task 0–4 appear in the page source
        for i in range(10):
            test_task = f"Test Task {i}"
            with self.subTest(task=test_task):
                self.assertIn(
                    test_task,
                    driver.page_source,
                    f"Expected to find '{test_task}' in the page"
                )
        print("All 5 test tasks were found on the page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

