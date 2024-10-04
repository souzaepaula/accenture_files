#QA Automation Challenge FrontEnd 4
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
#Acessing the Widgets page
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[4]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Acessing Progress Bar section 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[4]/div/ul/li[5]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Start Button 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='startStopButton']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Progress Bar monitoring
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div")))
driver.execute_script("arguments[0].scrollIntoView();", element)

#Stop function 
def stop():
    while True:
        var = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div").text.replace("%", "")
        var = int(var)
        if var == 25:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='startStopButton']")))
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            print("The progress bar is {}".format(var))
            break        

time.sleep(0.5)  
stop()

# %%
#Restart function 
def restart():
    while True:
        var_restart = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div").text.replace("%", "")
        var_restart = int(var_restart)

        if var_restart >= 25:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='startStopButton']")))
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            break 

time.sleep(5)
restart()

# %%
#reset function 
def reset():
    while True:
        var_reset = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div").text.replace("%", "")
        var_reset = int(var_reset)

        if var_reset == 100:
            time.sleep(2)
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='resetButton']")))
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            break 
reset()


