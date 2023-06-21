from pages.swag_labs import SwagLabs

def test_link(browser):

    demo_page =Swag_Labs(browser)
    demo_page.visit()
    demo_page.find_pass_field()
    demo_page.find_name_field()


    assert demo_page.find_pass_field()
    assert demo_page.exist_icon()
    assert demo_page.find_name_field()