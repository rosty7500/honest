from pages.page import Page

class Base(Page):
    _notification_locator = ""

    @property
    def notification(self):
        return self.selenium.find_element(*self._notification_locator).text

