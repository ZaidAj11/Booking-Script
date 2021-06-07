from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# If chrome isn't in default locationn you set it using options. File path is where chrome is saved
options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

# Set up chrome driver
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\\Windows\\chromedriver.exe')

# Go to site
driver.get('https://www.flyefit.ie')

# Member log in
enter = driver.find_element_by_xpath('//*[@id="menu-item-195"]')
enter.click()

# Maximizes the window
driver.maximize_window()

# Inputs email
email = driver.find_element_by_xpath('//*[@id="email_address"]')
# Insert email inside quotation
email.send_keys('')

# Inputs password - make sure its set to the one below
password = driver.find_element_by_xpath('//*[@id="password"]')
# Insert password inside quotation
password.send_keys('')

login = driver.find_element_by_xpath('/html/body/section/div[2]/form/button')
login.click()


book_nav = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[3]')
book_nav.click()

# Confirms
day_drop = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[3]/div/div/div[2]/b')
day_drop.click()
select = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[2]/div/form/div/div[3]/div/div/div[3]/div/ul/li[2]')
select.click()

# Clicks slot - second div from back is which time slot u open
book_time_slot = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/section/div[4]/div/div[7]/a/div[3]/p[2]')
book_time_slot.click()

# Confirms
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="book_class"]'))).click()

