from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#url = 'https://github.com/'
url = 'http://13.232.197.187'

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

#Navigate to website pointed by URL
driver.get(url)

#Extract the top heading from github.com
#text = driver.find_element_by_class_name('h000-mktg').text
#text = driver.find_element_by_class_name('HeaderMenu-summary').textContent
#text = driver.find_element_by_class_name('HeaderMenu-link').text
aboutusElement=driver.find_element_by_id('About Us')
driver.find_element_by_id('About Us').click()
strFirstParagraph = driver.find_element_by_id('PID-ab2-pg').text
strSecondParagraph = driver.find_element_by_xpath('/html/body/p[2]').text


#print(text)
print(aboutusElement)
print('First Paragraph')
print(strFirstParagraph)
print('Second Paragraph')
print(strSecondParagraph)
