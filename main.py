import time
import unittest
from selenium import webdriver

# Store path to Chrome driver
pathToBrowserDriver = './chromedriver'


class PromotionModalTest(unittest.TestCase):

    def setUp(self):
        self.chrome_driver = webdriver.Chrome(pathToBrowserDriver)
        # Setting default screen size
        self.chrome_driver.set_window_position(0, 0)
        self.chrome_driver.set_window_size(1024, 768)
        self.chrome_driver.get("https://gruzovichkof.ru/akcii")

    def test_promo_item_click(self):
        # Search promotion value
        default_promotion_value = 'С НАМИ ВЫГОДНЕЕ!'
        # Click on promotion label
        self.chrome_driver.find_element_by_link_text(default_promotion_value).click()
        time.sleep(3)
        if self.chrome_driver.find_element_by_class_name('MuiDialog-paper'):
            print('Modal opened')

    def tearDown(self):
        self.chrome_driver.close()


if __name__ == "__main__":
    unittest.main()
