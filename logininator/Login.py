from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\tmorton\\AppData\\Local\\Google\\Chrome\\User")

url = 'https://login.salesforce.com'

driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get(url)

# Login to salesforce
time.sleep(3)
login = driver.find_element(By.ID, "Login")
login.click()

# Switch to timeco
time.sleep(1)
driver.switch_to.new_window('tab')

url = 'link2'
driver.get(url)

# login
time.sleep(2)
login = driver.find_element(By.ID, "ctl00_main__btnLogin")
login.click()