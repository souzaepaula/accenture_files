#QA Automation Challenge FrontEnd 5
#Rodrigo de Paula
#Oct 2024

#Libs 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
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
#Acessing the Interactions page
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[5]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Acessing sortable section  
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[5]/div/ul/li[1]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Finding elements on the page 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='demo-tab-list']")))
driver.execute_script("arguments[0].scrollIntoView();", element)

# %%
#Element index 

time.sleep(2)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='demo-tab-list']")))
driver.execute_script("arguments[0].scrollIntoView();", element) 

elemento_drag = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
elemento_drop = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[1]")   
  
actions = ActionChains(driver)
actions.drag_and_drop(elemento_drag, elemento_drop).perform()
time.sleep(2) 

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='demo-tab-list']")))
driver.execute_script("arguments[0].scrollIntoView();", element)

elemento_drag = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
elemento_drop = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[2]")   

actions = ActionChains(driver)
actions.drag_and_drop(elemento_drag, elemento_drop).perform()
time.sleep(2) 

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='demo-tab-list']")))
driver.execute_script("arguments[0].scrollIntoView();", element)

elemento_drag = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
elemento_drop = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[3]")   

actions = ActionChains(driver)
actions.drag_and_drop(elemento_drag, elemento_drop).perform()
time.sleep(2)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='demo-tab-list']")))
driver.execute_script("arguments[0].scrollIntoView();", element)

elemento_drag = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
elemento_drop = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[4]")   

actions = ActionChains(driver)
actions.drag_and_drop(elemento_drag, elemento_drop).perform()
time.sleep(2)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='demo-tab-list']")))
driver.execute_script("arguments[0].scrollIntoView();", element)

elemento_drag = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
elemento_drop = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[5]")   

actions = ActionChains(driver)
actions.drag_and_drop(elemento_drag, elemento_drop).perform()
time.sleep(2)


