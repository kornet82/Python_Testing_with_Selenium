from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()

def open_chrome():
    driver.get('https://google.com')
    print("Page opened Online")

def mouse_click():
    '''find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")'''

    open_chrome()
    web_element = driver.find_element(By.CLASS_NAME, 'gb_q')
    web_element.click()
    time.sleep(5)
# mouse_click()

def mouse_click_and_hold():
    '''mouse_click_and_hold(web_element) is a method in which a mouse pointer is first moved to a
specific web element, and the same element is clicked using the left mouse button. Once
clicked, the element is not released, which results in holding it.'''
    open_chrome()
    button = driver.find_element(By.CLASS_NAME, 'gb_q')
    # Execute click-and-hold action on the element
    webdriver.ActionChains(driver).click_and_hold(button).perform()
    time.sleep(5)
# mouse_click_and_hold()

def mouse_context_click():
    '''mouse_context_click(web_element) is a function that moves the mouse pointer to a specific
web element, and then a context click is initiated on that element. A right mouse button
click is called a context click in ActionChains'''
    open_chrome()
    button = driver.find_element(By.CLASS_NAME, 'gb_q')
    # Execute click-and-hold action on the element
    webdriver.ActionChains(driver).context_click(button).perform()
    time.sleep(5)
# mouse_context_click()

def mouse_double_click():
    '''double_click(web_element) is a method in which a mouse pointer goes to the located
web element, and then the left mouse button is clicked twice (double-clicked)'''
    open_chrome()
    button = driver.find_element(By.CLASS_NAME, 'gb_q')
    webdriver.ActionChains(driver).double_click(button).perform()
    time.sleep(3)
# mouse_double_click()

def mouse_move_to_an_element():
    '''The mouse_move_to_element(web_element) function moves the mouse to a web element. It
is mainly focused on drop-down menus, where you can scroll or click after moving the
mouse over it'''
    driver.get('http://apress.com')
    main_menu = driver.find_element(By.LINK_TEXT, 'CATEGORIES')
    ActionChains(driver).move_to_element(main_menu).perform()
    time.sleep(3)
    # Wait for sub menu to be displayed
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Python')))
    sub_menu=driver.find_element(By.LINK_TEXT, 'Python')
    time.sleep(3)
    ActionChains(driver).click(sub_menu).perform()
    time.sleep(3)
# mouse_move_to_an_element()











