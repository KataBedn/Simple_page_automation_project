import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, add_remove_page, basic_auth_page, logged_in_page, date_picker_page, drag_and_drop_page, form_page, iframe_page, key_presses_page, status_codes_page
from selenium.webdriver import ActionChains

from tests.page_objects.form_page import first_name, firstname_value, last_name, lastname_value


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
        self.assertTrue(dropdown_page.choose_option(self.driver))

    def test8_add_element(self):
        add_remove_page.click_add_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_and_remove_content_displayed(self.driver))
        add_remove_page.add_new_element(self.driver)
        self.assertTrue(add_remove_page.element_visible(self.driver))


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
        self.assertTrue(basic_auth_page.invalid_credentials_message_displayed(self.driver))


    # def test12_pick_correct_date(self):
    #     date_picker_page.click_date_picker_tab(self.driver)
    #     self.assertTrue(date_picker_page.date_picker_content_displayed(self.driver))
    #     self.assertTrue(date_picker_page.insert_correct_data(self.driver))
    #
    #
    # def test13_pick_incorrect_date(self):
    #     date_picker_page.click_date_picker_tab(self.driver)
    #     self.assertTrue(date_picker_page.date_picker_content_displayed(self.driver))
    #     date_picker_page.insert_incorrect_data(self.driver)


    def test14_input_form_information(self):
        form_page.click_form_page_tab(self.driver)
        self.assertTrue(form_page.form_page_displayed(self.driver))
        form_page.send_correct_keys_to_first_name(self.driver, firstname_value, first_name)
        form_page.send_correct_keys_to_last_name(self.driver, lastname_value, last_name)
        form_page.press_submit(self.driver)
        self.assertTrue(form_page.accept_alert_visible(self.driver))


    def test15_iframe(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_displayed(self.driver))
        self.assertTrue(iframe_page.press_button_1(self.driver))



    def test16_iframe(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_displayed(self.driver))
        self.assertTrue(iframe_page.press_button_2(self.driver))


    def test17_keypresses(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_displayed(self.driver))
        self.assertTrue(key_presses_page.enter_and_verify_key(self.driver))


    def test18_status_code_200(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_displayed(self.driver))
        status_codes_page.verify_code_200(self.driver)


    def test19_status_code_305(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_displayed(self.driver))
        status_codes_page.verify_code_305(self.driver)


    def test20_status_code_404(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_displayed(self.driver))
        status_codes_page.verify_code_404(self.driver)


    def test21_status_code_500(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_displayed(self.driver))
        status_codes_page.verify_code_500(self.driver)



    # def test22_drag_a_over_b_and_drop(self):
    #     drag_and_drop_page.click_drag_and_drop_tab(self.driver)
    #     self.assertTrue(drag_and_drop_page.drag_and_drop_content_displayed(self.driver))
    #     self.assertTrue(drag_and_drop_page.drag_element_a_over_b(self.driver))



if __name__ == '__main__':
    unittest.main()

