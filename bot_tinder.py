from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from password import username, password
import time
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com/')
        
        #fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        cookies_xpath = '/html/body/div[1]/div/div[2]/div/div/div[1]/button'
        fb_xpath = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button'
        more_options_xpath = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button'
        fb2_xpath = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button'

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, cookies_xpath)))

        cookies_btn = self.driver.find_element_by_xpath(cookies_xpath)
        cookies_btn.click()

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, fb_xpath)))
            fb_btn = self.driver.find_element_by_xpath(fb_xpath)
        except:
            more_options_btn = self.driver.find_element_by_xpath(more_options_xpath)
            more_options_btn.click()

            fb_btn2 = self.driver.find_element_by_xpath(fb2_xpath)
            fb_btn2.click()
        else:
            fb_btn.click()
    
        base_window = self.driver.window_handles[0]
        fb_page = self.driver.window_handles[1]
        popup_fb = self.driver.switch_to_window(fb_page)

        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_password = self.driver.find_element_by_xpath('//*[@id="pass"]')

        fb_email.send_keys(username)
        fb_password.send_keys(password)

        fb_login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_login_btn.click()
        
        self.driver.implicitly_wait(15)

        self.driver.switch_to_window(base_window)

    def location(self):
        location_xpath = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
        location_btn = self.driver.find_element_by_xpath(location_xpath)
        location_btn.click()

        notification_xpath = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]'
        notification_btn = self.driver.find_element_by_xpath(notification_xpath)
        notification_btn.click()

    def swap(self):
        like_xpath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
        dislike_xpath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, like_xpath)))
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, dislike_xpath)))

        like_btn = self.driver.find_element_by_xpath(like_xpath)
        dislike_btn = self.driver.find_element_by_xpath(dislike_xpath)

        self.driver.implicitly_wait(5)

        i = 0
        
        random.seed()

        while(i < 100):
            if(random.randint(1,2) == 1):
                dislike_btn.click()
            else:
                like_btn.click()

            i += 1
            time.sleep(1)