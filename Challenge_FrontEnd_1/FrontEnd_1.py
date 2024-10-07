#QA Automation Challenge FrontEnd 1 
#Rodrigo de Paula
#Oct 2024

#Libs 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
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
#Acessing the Forms page
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[2]/div/div[3]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Acessing Practice Form section 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[2]/div')))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Filling up the form 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='firstName']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#First Name
driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys('José')

#Last Name
driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys('Silva')

#User e-mail
driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys('jose.silva@gmail.com')

# %%
#Gender checkbox
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Mobile Number 
driver.find_element(By.XPATH, "//*[@id='userNumber']").send_keys('1998971234')

# %%
#Date of Birth
#Click before
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='dateOfBirthInput']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
#Month selection
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('Jan')
#Year selection
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('2002')
#Day selection
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[7]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('5')
#Click after
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[7]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()


# %%
#Subject 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='subjectsContainer']/div/div[1]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
#Computer Science option choosen 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='subjectsInput']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('Computer Science')
element.send_keys(Keys.ENTER)
#Physics option choosen 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='subjectsInput']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys('Physics')
element.send_keys(Keys.ENTER)

# %%
#Hobbies checkbox
#Sport selected 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]/label")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
#Reading Selected 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[2]/label")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Select Picture 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div/input[@type='file']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys("C:/Users/souza/source/repos/QA_Automation_Accenture/Challenge_FrontEnd_1/QA_Automation_File.txt")

# %%
#Current Address
driver.find_element(By.XPATH, "//*[@id='currentAddress']").send_keys('Beautfull  Avenue, 5632 \nDowntown')

# %%
#State choose option 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='state']/div/div[1]/div[1]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

#Click on NCR
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='NCR']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#click on Gurgaon
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='city']/div/div[1]")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Gurgaon']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Click on submit 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='submit']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Checking the correct Form Page
correct_phrase = 'Thanks for submitting the form'

try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='example-modal-sizes-title-lg']")))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    text_page = element.text 
    if correct_phrase in text_page:
        print('Correct phrase found! You are on the correct page')
    else:
        print('Correct phrase not found! Please, check!')
except Exception as e:
    print(f"Erro ao tentar encontrar a frase: {e}")

# %%
#Submit close button 
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='closeLargeModal']")))
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# %%
#Chrome closing 
driver.quit()


