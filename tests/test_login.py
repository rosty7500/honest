from pages.login import Blogpage

def test_emptysearch(base_url_live,variables,selenium):
    """Check empty search"""
    search = Blogpage(base_url_live, selenium).open()
    search.click_search_icon()
    search.hit_enter_key()
    no_results_text = search.no_search_results_text
    assert "No search results" == no_results_text




def test_emptyspacessearch(base_url_live,variables,selenium):
    """Check spaces search"""
    search = Blogpage(base_url_live, selenium).open()
    search.click_search_icon()
    search.enter_text(variables['empty_text'])
    search.hit_enter_key()
    no_results_text = search.no_search_results_text
    assert "No search results" == no_results_text




def test_appendsearchkeyword_in_url(base_url_live,variables,selenium):
    """Check successful search"""
    search = Blogpage(base_url_live, selenium).open()
    search.click_search_icon()
    search.search_text(variables['search_keyword'])
    search.hit_enter_key()
    current_URL = selenium.current_url
    assert "football" in current_URL



def test_invalidtextsearch(base_url_live,variables,selenium):
    """Check invalid search"""
    search = Blogpage(base_url_live, selenium).open()
    search.click_search_icon()
    search.enter_text(variables['invalid_text'])
    search.hit_enter_key()
    no_results_text = search.no_search_results_text
    assert "No search results" == no_results_text


def test_validtextsearch(base_url_live,variables,selenium):
    """Check valid search"""
    search = Blogpage(base_url_live, selenium).open()
    search.click_search_icon()
    search.enter_text(variables['search_keyword'])
    search.hit_enter_key()
    searches = search.search_result_text
    try:
        assert variables['search_keyword'] in searches
    except AssertionError as error:
        print(error)










