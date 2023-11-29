from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

chrome_options = webdriver.ChromeOptions()
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
]

def scrape(job_title):
    jobList=[]
    random_user_agent=random.choice(user_agents)
    chrome_options.arguments.clear()
    chrome_options.add_argument(f"user-agent={random_user_agent}")
    service= Service(exectuable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)
    driver.get("https://www.levels.fyi/jobs?from=subnav&jobId=99441083848499910")

    onBoardingExit=driver.find_element(By.CLASS_NAME,"onboarding-modal_closeButton__eUirx")
    ActionChains(driver).click(onBoardingExit).perform()
    input_element=driver.find_element(By.CLASS_NAME,"job-search-bar_searchBar__bQdyj")
    input_element.send_keys(job_title+Keys.ENTER)
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
        showMoreButton=driver.find_element(By.CLASS_NAME,"job-details-about_showMoreOrLess___1Ug_")
        ActionChains(driver).click(showMoreButton).perform()
        jobDescription=driver.find_element(By.CLASS_NAME,"job-details-about_content__1lN_1")
        jobList.append([jobDescription.text,h1_element.text,a_element.get_attribute('href')])
        driver.back()
    
    
    time.sleep(10)
    driver.quit()
    return jobList
