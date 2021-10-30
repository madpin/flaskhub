import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def _get_drive():
    options = webdriver.ChromeOptions()
    options.headless = True
    # options.add_argument("window-size=800x600")
    options.add_argument("window-size=1800x900")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage') 
    # options.add_argument('--disable-dev-shm-usage') # Not used 
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)
    return driver

def get_listing(url):
    driver = _get_drive()

    driver.get(url)
    # body = driver.find_element_by_tag_name('body')
    # body.screenshot('/data/screenshot00.png')

    # driver.save_screenshot('/data/screenshot0.png')
    driver.execute_script("CookieConsent.acceptAll();")
    time.sleep(1)
    # driver.save_screenshot('/data/screenshot1.png')
    # body2 = driver.find_element_by_tag_name('body')
    # body2.screenshot('/data/screenshot12.png')
    # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    # time.sleep(1)
    # driver.save_screenshot('/data/screenshot2.png')
    # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    # time.sleep(1)
    # driver.save_screenshot('/data/screenshot3.png')
    # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    # time.sleep(1)
    # driver.save_screenshot('/data/screenshot4.png')
    # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    # time.sleep(1)
    # driver.save_screenshot('/data/screenshot5.png')
    # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    # time.sleep(1)
    # driver.save_screenshot('/data/screenshot6.png')

    print(driver.get_window_size())
    print(driver.get_window_position())
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    print(driver.get_window_position())
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    # for t in range(10):
    #     driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    # for t in range(10):
    #     time.sleep(1)
    #     driver.find_element_by_css_selector('.additional_data').click()
    # src = driver.page_source
    # print(src)
    # parser = BeautifulSoup(src, "html.parser")


    element = driver.find_element_by_id("__NEXT_DATA__")
    print(element)
    # print(element.text)
    # print(element.text)
    print()
    d = json.loads(element.get_attribute('innerHTML'))
    with open('/data/data.json', 'w') as f:
        f.write(json.dumps(d, sort_keys=True, indent=4))

    # print(d)
    # print(element.innerHTML) # Error

    driver.close()