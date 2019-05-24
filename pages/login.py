
from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.common.keys import Keys


class Blogpage(Base):
    _url = '{base_url}'

    _search_icon = (By.CSS_SELECTOR, '#social-content-hub > div > div.A_aSfFe9DgOoNMeA0FBso > div > div > div:nth-child(3)')
    _search_field = (By.XPATH, '//div[@id="social-content-hub"]/div/div/div/div/div[3]/div/div/a/div[2]/span/input')
    _nosearch_results_text = (By.XPATH, '//h1[@class="_3j1YMd3zjL1xNt87XF8hqO"]')
    _search_result_paragraph_text = (By.XPATH, '//div[@id="social-content-hub"]/div/div[2]/div/div[2]/div/div[2]/a[1]/div/div/p')



    def click_search_icon(self):
        self.selenium.find_element(*self._search_icon).click()

    def hit_enter_key(self):
        self.selenium.find_element(*self._search_field).send_keys(Keys.ENTER)

    def enter_text(self, value):
        self.selenium.find_element(*self._search_field).send_keys(value)

    def search_text(self, value):
        self.selenium.find_element(*self._search_field).send_keys(value)

    @property
    def no_search_results_text(self):
        self.wait_for_element(self._nosearch_results_text)
        return self.selenium.find_element(*self._nosearch_results_text).text

    @property
    def search_result_text(self):
        self.wait_for_element(self._search_result_paragraph_text)
        return self.selenium.find_element(*self._search_result_paragraph_text).text

