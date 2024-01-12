# coding: utf-8

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

from common import *

def buy(config:dict):
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
            text.send_keys(config.get('first_name'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingName2")))
            text.send_keys(config.get('last_name'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingAddress1")))
            text.send_keys(config.get('address_line'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingCity")))
            text.send_keys(config.get('city'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingPostalCode")))
            text.send_keys(config.get('postal'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingPhoneNumber")))
            text.send_keys(config.get('phone'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
            text.send_keys(config.get('email'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "verEmail")))
            text.send_keys(config.get('email'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ccNum")))
            text.send_keys(config.get('card'))
            text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cardSecurityCode")))
            text.send_keys(config.get('ccv'))
            select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingState")))
            Select(select).select_by_value(config.get('state'))
            select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "expirationDateMonth")))
            Select(select).select_by_value(config.get('month'))
            select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "expirationDateYear")))
            Select(select).select_by_value(config.get('year'))
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
