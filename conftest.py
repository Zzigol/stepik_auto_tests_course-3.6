import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#python -m pytest --language=es test_items.py
#python -m pytest --language=fr test_items.py
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    choised_language = request.config.getoption('language')

    if browser_name == 'chrome':
        print("\nnow starting your chrome browser for tests...")
        options = Options()
        if choised_language:
            options.add_experimental_option('prefs', {'intl.accept_languages': choised_language})
        else:
            raise pytest.UsageError("--choose your language again")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(15)
    elif browser_name == "firefox":
        print("\nnow starting your firefox browser for tests...")
        fp = webdriver.FirefoxProfile()
        if choised_language:
            fp.set_preference("intl.accept_languages",  choised_language)
        else:
            raise pytest.UsageError("--choose your language again")
        browser = webdriver.Firefox(executable_path=r"C:/geckodriver/geckodriver.exe", firefox_profile=fp)
        browser.implicitly_wait(15)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox ONLY!!!")

    yield browser
    print("\nand... quit browser now")
    browser.quit()