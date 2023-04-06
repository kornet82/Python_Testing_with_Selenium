from selenium import webdriver


def open_close_browser():
    '''The open_close_browser function closes a currently open window using the Selenium driver. It does
not affect the other windows that are opened. The execution process remains active'''
    driver = webdriver.Firefox()
    driver.get('https://google.com')
    print("Browser Window opened")
    # Close function
    driver.close()
    print("Browser Window closed")
# open_close_browser()


def open_quit_browser():
    '''The quit() function closes all the open windows. It also terminates the execution
process of the driver.'''
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    print("Browser Window opened")
    # Quit function
    driver.quit()
    print("Terminates process")
# open_quit_browser()

def open_page_offline():
    '''Open web page offline'''
    driver = webdriver.Chrome()
    driver.get('file:///C:/File/Path/file_name.html')
    print("Page opened Offline ")
    driver.quit()
    print("Terminates process")
# open_page_offline()

def maximize_browser():
    '''The maximize_browser function in Selenium maximizes the current web browser. Testers use it to
test the responsiveness of a web page. It is used by the browser when it is not opened in a
maximized state.'''
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    print("Page opened Online")
    driver.maximize_window()
    print("Browser is maximised")
    driver.quit()
    print("Terminates process")
# maximize_browser()

def fullscreen_browser():
    '''The fullscreen function sets the browser to fullscreen mode. The title, URL, address
bar, tabs, and so forth, are not visible on the web page visible when in fullscreen.'''
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    print("Page opened Online")
    driver.fullscreen_window()
    print("Browser is fullscreen now")
    driver.implicitly_wait(10)
    driver.quit()
    print("Terminates process")
# fullscreen_browser()


