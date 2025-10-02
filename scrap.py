# import requests as re
# from bs4 import BeautifulSoup



# res = re.get("https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job?mobile=false&width=1920&height=500&bga=true&needsRedirect=false&jan1offset=330&jun1offset=330")
# soup = BeautifulSoup(res.content, "html.parser")
# print(res.status_code)
# content = soup.find('div', class_="iCIMS_MainWrapper iCIMS_JobPage iCIMS_Desktop ")
# print(soup.prettify())

#selenium method as content is loading dynamically

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# url="https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job?mobile=false&width=1920&height=500&bga=true&needsRedirect=false&jan1offset=330&jun1offset=330"

# options=webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")
# driver=webdriver.Chrome(options=options)
# driver.get(url)
# wait=WebDriverWait(driver,20)
# iframe=wait.until(EC.presence_of_element_located((By.ID,"icims_content_iframe")))
# driver.switch_to.frame(iframe)
# time.sleep(3)


# print(driver.find_element(By.TAG_NAME,"body").text)

# input("Press Enter to close...")
# driver.quit()



# a function for same 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def scrape_iframe_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        iframe = wait.until(EC.presence_of_element_located((By.ID, "icims_content_iframe")))
        driver.switch_to.frame(iframe)
        time.sleep(3)  
        job_title = driver.find_element(By.CSS_SELECTOR, "h1, .iCIMS_Header h2").text
        description = driver.find_element(By.CSS_SELECTOR, ".iCIMS_InfoMsg, .iCIMS_Expandable_Text").text
        body = driver.find_element(By.TAG_NAME, "body")
        print(job_title, description, body.text)
    
    finally:
        input("Press Enter to close...")
        driver.quit()

url = "https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job?mobile=false&width=1920&height=500&bga=true&needsRedirect=false&jan1offset=330&jun1offset=330"
scrape_iframe_content(url)
