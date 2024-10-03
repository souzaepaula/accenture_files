#QA Automation Challenge FrontEnd 2 
#Rodrigo de Paula
#Oct 2024

#Libs 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# %%
#Creating drive connection 
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

# %%
#Accessing the URL: https://demoqa.com/
driver.get('https://demoqa.com/')

# %%
#Acessing the Alerts, Frame & Windows page
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[3]/div")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Accessing the Browser Windows page
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/ul/li[1]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Accessing the New Window
main_window = driver.current_window_handle
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='windowButton']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
new_window = element
new_window.click()
#Switchin to new window 
wait = WebDriverWait(driver, 10)
new_window = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='windowButton']")))
driver.execute_script("arguments[0].scrollIntoView();", new_window)

all_windows = driver.window_handles

for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

# %%
#Checking the new window's message 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading")))
driver.execute_script("arguments[0].scrollIntoView();", element)

correct_phrase = 'This is a sample page'

try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading")))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    text_page = element.text 
    if correct_phrase in text_page:
        print('Correct phrase found! You are on the correct page')
    else:
        print('Correct phrase not found! Please, check!')
except Exception as e:
    print(f"Erro ao tentar encontrar a frase: {e}")

#Closing the new window after message validation
driver.close()


