from pages.base_page import BasePage


def test_link(browser):

    demo_page = BasePage(browser)
    demo_page.visit()
    demo_page.find_name_field()
    assert demo_page.find_pass_field()
    assert demo_page.exist_icon()
    assert demo_page.find_name_field()