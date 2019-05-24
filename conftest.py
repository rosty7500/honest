import pytest

@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(5)
    selenium.maximize_window()
    return selenium


@pytest.fixture(scope="module")
def base_url_live():
    base_url = "https://www.unibet.co.uk/blog"
    return base_url
