import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "APjFqb")))
search_input.send_keys("netflix")
search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jZ2SBf")))
search_button.click()
driver.find_element(By.XPATH, "(//a[@jsname='qOiK6e'])[1]").click()
login_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sign In")))
login_link.click()
mail = driver.find_element(By.ID, "id_userLoginId")
# Give the login mail id
mail.send_keys("email")
password = driver.find_element(By.XPATH, "//input[@type='password']")
# Give the login password
password.send_keys("password")
submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
submit.click()
time.sleep(2)
profile = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//div[@class='profile-icon'])[1]")))
profile.click()
movie_duration_element = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='duration']")))
movie_duration = movie_duration_element.text
print("Movie Duration:", movie_duration)
time.sleep(5)

