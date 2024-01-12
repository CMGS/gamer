# coding: utf-8

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

from common import *

def buy():
    try:
        with uc.Chrome() as driver:
            driver.get(PRODUCT_URL)
            btn_selector = "a.featured-buy-link.link-btn.brand-green.cta-button.cta-link-large.c-fOVUQc.js-add-button"
            btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, btn_selector)))
            btn.click() # add to cart
            time.sleep(1)
            checkout_selector = "div.nv-button.js-checkout.cart__checkout-button"
            btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, checkout_selector)))
            btn.click() # checkout
            btn = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "btnCheckoutAsGuest"))) # wait queue
            btn.click() # as guest
            # fill form
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingName1")))
            text.send_keys(FIRST_NAME)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingName2")))
            text.send_keys(LAST_NAME)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingAddress1")))
            text.send_keys(ADDRESS_LINE_1 + " " + ADDRESS_LINE_2)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingCity")))
            text.send_keys(CITY)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingPostalCode")))
            text.send_keys(POSTAL)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingPhoneNumber")))
            text.send_keys(PHONE_NUMBER)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
            text.send_keys(EMAIL)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "verEmail")))
            text.send_keys(EMAIL)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ccNum")))
            text.send_keys(CARD_NUMBER)
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cardSecurityCode")))
            text.send_keys(CCV)
            select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingState")))
            Select(select).select_by_value(STATE)
            select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "expirationDateMonth")))
            Select(select).select_by_value(MONTH)
            select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "expirationDateYear")))
            Select(select).select_by_value(YEAR)
            print("form filled")
            # submit
            button_selector = "input.dr_button[value='Review Order']"
            btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, button_selector)))
            btn.click()
            print("review order")
            time.sleep(86400)
    except Exception as e:
        print("error", e)
        driver.quit()
