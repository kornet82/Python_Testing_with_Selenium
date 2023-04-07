from selenium import webdriver
import time

driver = webdriver.Chrome()
def open_chrome():
    driver.get('https://google.com')
    print("Page opened Online")


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


def setting_the_browser_position():
    '''The setting_the_browser_position method sets the browser position along the x and y axes.
The position of x and y starts at (0,0) from the top-right corner of the screen'''
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    print("Page opened Online")
    driver.set_window_position(x=500, y=400)
    print("Browser is at x=500, y=400")
    time.sleep(3)
    driver.quit()
    print("Terminates process")


# setting_the_browser_position()


def setting_the_size_using_coordinates():
    '''This method sets the browser with position and dimensions. The position concerns the x
and y coordinates, whereas dimensions are with height and width.'''
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    print("Page opened Online")
    driver.set_window_rect(x=50, y=40, width=450, height=200)
    print("Browser is at x=50, y=40")
    time.sleep(3)
    driver.quit()
    print("Terminates process")
# setting_the_size_using_coordinates()

def getting_the_browser_position():
    '''In some test cases, the browser position is required to perform actions based on it. The
get method returns the position of the browser window with respect to x and y positions
in a Python dictionary.'''
    open_chrome()
    window_pos=driver.get_window_position()
    print(window_pos)
# getting_the_browser_position()


def getting_the_window_size():
    '''The height and width of the browser window are returned in a Python dictionary when
this function is used.'''
    open_chrome()
    window_size = driver.get_window_size()
    print(window_size)
# getting_the_window_size()


