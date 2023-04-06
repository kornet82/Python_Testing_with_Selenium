#Importing selenium libraries in python
from selenium import webdriver

#Opening web Firefox browser using webdriver
driver=webdriver.Firefox()

#Adding URL to open in browser
driver.get('http://www.apress.com')

#Finding Element of search bar
search=driver.find_element('name','query')

#Searching book name as string/query in search bar
search.send_keys('Python Testing with Selenium')

#Submit string to search bar
search.submit()

# Close Firefox browser
driver.quit()

# if __name__=="__main__":




