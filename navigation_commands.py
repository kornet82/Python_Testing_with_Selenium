from selenium import webdriver
import time

driver = webdriver.Chrome()

def open_chrome():
    driver.get('https://google.com')
    print("Page opened Online")

def back_command():
    '''The back() function is used to navigate to a previously visited page in the same
browser tab'''
    open_chrome()
    time.sleep(3)
    driver.get('https://ya.ru')
    time.sleep(3)
    driver.back()
    time.sleep(3)
    print('Moved to the previous page')
# back_command()


def forward_command():
    '''This function helps to click on forward button of web browser which eventually goes to
next page if available'''
    open_chrome()
    time.sleep(3)
    driver.get('https://ya.ru')
    time.sleep(3)
    driver.forward()
    time.sleep(3)
    driver.get('https://mail.ru')
    driver.back()
    time.sleep(3)
    print('Moved to the previous page')
# forward_command()


def click_refresh_button():
    '''The click_refresh_button() function reloads the current page in the web browser.'''
    open_chrome()
    print('The page will be refreshed')
    driver.refresh()
    time.sleep(3)
    print('The page refreshed')
# click_refresh_button()

