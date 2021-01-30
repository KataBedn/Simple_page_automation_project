from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element(driver_instance, xpath):
   elem = driver_instance.find_element_by_xpath(xpath)
   hover = ActionChains(driver_instance).move_to_element(elem)
   hover.perform()


def wait_for_visibility_of_element(driver_instance, id, time_to_wait=10):
   try:
       elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
   except TimeoutException:
       elem = False
   return elem


def wait_for_visibility_of_element_xpath(driver_instance, xpath, time_to_wait=10):
   try:
       elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
   except TimeoutException:
       elem = False
   return elem


def wait_for_visibility_of_element_css(driver_instance, CSS_SELECTOR, time_to_wait=10):
   try:
       elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))
   except TimeoutException:
       elem = False
   return elem


def wait_for_invisibility_of_element(inv_driver_instance, id, time_to_wait=8):
   inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.ID, id)))
   return inv_elem


def wait_for_invisibility_of_element_by_xpath(inv_driver_instance, xpath, time_to_wait=8):
   inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
   return inv_elem

def wait_for_visibility_of_alert(driver_instance, time_to_wait=3):
   elem = WebDriverWait(driver_instance, time_to_wait).until(EC.alert_is_present())
   return elem