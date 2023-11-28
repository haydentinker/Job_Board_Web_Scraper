from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


service= Service(exectuable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.levels.fyi/jobs?from=subnav&jobId=99441083848499910")

onBoardingExit=driver.find_element(By.CLASS_NAME,"onboarding-modal_closeButton__eUirx")
ActionChains(driver).click(onBoardingExit).perform()
input_element=driver.find_element(By.CLASS_NAME,"job-search-bar_searchBar__bQdyj")
input_element.send_keys("software engineer jobs remote"+Keys.ENTER)
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"company-jobs-preview-card_jobDescriptionRow__4Uh_q"))
)
jobs=driver.find_elements(By.CLASS_NAME,"company-jobs-preview-card_companyJobContainer___zVGi")
for i in range(len(jobs)):

    job=driver.find_elements(By.CLASS_NAME,"company-jobs-preview-card_companyJobContainer___zVGi")[i]

    ActionChains(driver).click(job).perform()

    time.sleep(random.randint(5,15))
    job_element = driver.find_element(By.CLASS_NAME,"job-details-header_jobTitleRow__mAQC0")
    h1_element = job_element.find_element(By.XPATH, ".//h1")
    a_element = job_element.find_element(By.XPATH, ".//a")
    print(h1_element.text)
    print(a_element.get_attribute('href'))
    driver.back()
   
   
time.sleep(10)
driver.quit()

#"job-details-about_markdownText__MUjx2 job-details-about_showAll__WuPop job-details-about_plainTextDescription__9p3D6"


