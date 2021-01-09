import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, add_remove_page, basic_auth_page, logged_in_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkbox_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.input_content_displayed(self.driver))


    def test5_inputs_correct_input(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_displayed(self.driver))
        dropdown_page.choose_option(self.driver)

    def test8_add_element(self):
        add_remove_page.click_add_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_and_remove_content_displayed(self.driver))
        add_remove_page.add_new_element(self.driver)


    def test9_remove_element(self):
        add_remove_page.click_add_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_and_remove_content_displayed(self.driver))
        add_remove_page.add_new_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))


    def test10_log_in_with_correct_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_displayed(self.driver))
        basic_auth_page.send_correct_credentials_to_input(self.driver)
        basic_auth_page.press_login(self.driver)
        self.assertTrue(logged_in_page.logged_in_message_displayed(self.driver))


    def test11_log_in_with_incorrect_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_displayed(self.driver))
        basic_auth_page.send_incorrect_credentials_to_input(self.driver)
        basic_auth_page.press_login(self.driver)
        basic_auth_page.invalid_credentials_message_displayed(self.driver)


if __name__ == '__main__':
    unittest.main()

