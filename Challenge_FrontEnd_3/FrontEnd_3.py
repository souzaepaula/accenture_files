#QA Automation Challenge FrontEnd 3 
#Rodrigo de Paula
#Oct 2024

#Libs 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

# %%
#Creating drive connection 
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

# %%
#Accessing the URL: https://demoqa.com/
driver.get('https://demoqa.com/')

# %%
#Acessing the Elements page
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]/div")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Acessing Web Tables section 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[4]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Adding new user
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='addNewRecordButton']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Filling user form
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='firstName']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('José')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='lastName']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('da Silva')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userEmail']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('jose.silva@gmail.com')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='age']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('38')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='salary']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('1412')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='department']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('Salles')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='submit']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Editing user form
time.sleep(2)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='edit-record-4']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='firstName']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.clear()
element.send_keys('João')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='lastName']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.clear()
element.send_keys('Ribeiro')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userEmail']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.clear()
element.send_keys('joao.ribeiro@hotmail.com')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='age']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.clear()
element.send_keys('40')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='salary']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.clear()
element.send_keys('2000')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='department']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.clear()
element.send_keys('Ecommerce')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='submit']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Deleting the user 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='delete-record-4']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()


