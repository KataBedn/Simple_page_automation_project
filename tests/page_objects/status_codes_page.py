import requests
from tests.helpers.support_functions import *


status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
code200 = '200siteAnchor'
code404 = '404siteAnchor'
code305 = '305siteAnchor'
code500 = '500siteAnchor'



def click_status_codes_tab(driver_instance):
    elem = driver_instance.find_element_by_id(status_codes_tab)
    elem.click()


def status_codes_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, status_codes_content)
    return elem.is_displayed()


def verify_code_200(driver_instance):
    elem = driver_instance.find_element_by_id(code200)
    url200 = elem.get_attribute("href")
    value = '200 OK'
    if value == requests.get(url200).text:
        return True
    else:
        return False


def verify_code_305(driver_instance):
    elem = driver_instance.find_element_by_id(code305)
    url200 = elem.get_attribute("href")
    value = '305 Use Proxy'
    if value == requests.get(url200).text:
        return True
    else:
        return False


def verify_code_404(driver_instance):
    elem = driver_instance.find_element_by_id(code404)
    url200 = elem.get_attribute("href")
    value = '404 Not Found'
    if value == requests.get(url200).text:
        return True
    else:
        return False


def verify_code_500(driver_instance):
    elem = driver_instance.find_element_by_id(code500)
    url200 = elem.get_attribute("href")
    value = '500 Internal Server Error'
    if value == requests.get(url200).text:
        return True
    else:
        return False