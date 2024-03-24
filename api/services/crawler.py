from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import time
from api.utils.common import Common

class Crawler:
    def __init__(self):
        self.base_url = 'https://www.instagram.com'
        self.common = Common()

    def search_images(self, keyword):
        search_url = f'{self.base_url}/explore/tags/{keyword}/'

        # Start the seasion using Chrome driver (any driver can be used here)
        driver = webdriver.Chrome()
        driver.get(search_url)
        
        # Wait for 5 seconds to load the page's content
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        image_elements = soup.find_all('img')

        image_urls = [img['src'] for img in image_elements if img.has_attr('src') and self.common.validate_image_url(img['src'])]
        image_urls = image_urls[:5]  # Limit to maximum 5 image URLs

        driver.quit()
        return image_urls        
