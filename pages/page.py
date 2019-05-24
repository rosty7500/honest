from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):

    _url = None

    def __init__(self, base_url, selenium):
        self.base_url = base_url
        self.selenium = selenium

    def open(self):
        self.selenium.get(self.url)
        self.wait_for_page_to_load()
        return self

    @property
    def url(self):
        if self._url is not None:
            return self._url.format(base_url=self.base_url)
        return self.base_url

    def wait_for_page_to_load(self):
        return self

    def wait_for_element(self, element):
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located(element))

    def get_text(self, element):
        self.wait_for_element(element)
        return self.selenium.find_element(element).text



