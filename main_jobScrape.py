# MAIN - JOBSCRAPE 

import time 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd
import numpy as np

import requests, bs4
import urllib.request
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import firefox_jobscrape as f_scrape

driver=webdriver.Firefox(executable_path='/Applications/geckodriver')

email = 'filip.birkfeldt@gmail.com'
password = 'teeMUmX7kFZP4ym'
glassdoor = 'https://www.glassdoor.com/member/home/index.htm'
linkedin = 'https://www.linkedin.com/jobs/search/?keywords=data%20scientist'
glassdoor_data = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data+&locT=N&locId=223&jobType=&context=Jobs&sc.keyword=data+&dropdown=0'

specific_job = 'data'
specific_location = 'sweden'

# Hämtar sidan glassdoor 
f_scrape.get_glassdoor(driver, glassdoor, email, password)
# time.sleep(2)
# Söker efter jobb & plats
f_scrape.reach_specific(driver, glassdoor_data)
#Hämta job-annonser 
job_vector=[]
job_vector = f_scrape.get_job_on_page(driver, job_vector)
#Antal kolumner som behövs: 
number_cols = f_scrape.col_nbr(job_vector)

print('max.längd', number_cols)
print(job_vector)

#Skapar pandas-DataFrame 
df_jobb = f_scrape.create_dataframe(number_cols, job_vector)

"""
nex_el = driver.find_element_by_class_name('next')
time.sleep(10)

policy_element=driver.find_element_by_id("onetrust-policy-text")
policy_element.click()

#driver.find_element_by_class_name("SVGInline-svg modal_closeIcon-svg")
 

# print(policy_element)
# nex_el.click()


#Stänger ner chrome
time.sleep(3)
driver.close()

"""





