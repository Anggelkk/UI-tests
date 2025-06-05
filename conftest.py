from ctypes import c_bool
from os import close

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    """

    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
