# yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyes
# Main class for Filips Web-scraping tool :) 

# https://github.com/FilipBirkfeldt/job_search
# command+shift+P 

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

from Sortera_data import sortera

# GLASSDOOR
def get_glassdoor(driver, html, email, password): 

    print('---------------------------------------------START AV SCRIPTET------------------------------------------------------------------')
    driver.get(html)
    email_box = driver.find_element_by_id('userEmail')
    email_box.send_keys(email)
    
    password_box = driver.find_element_by_id('userPassword')
    password_box.send_keys(password)

    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[3]/form/div[3]/div[1]/button').click()

# det specifika jobbet som man vill söka efter
def search_specific(driver, type_of_job, location): 
    driver.find_elements_by_id('sc.keyword').send_keys(type_of_job)
    driver.find_element_by_id('sc.location').send_keys(location)

def reach_specific(driver, glassdoor_data): 
    driver.get(glassdoor_data)

# kommentar
# kommentar

def get_job_on_page(driver, job_vector): 
    '''
    for i in range(1,number_pages):
        #Loopar igenom & hämtar info från page 1
        try: 
            next_button = driver.find_element_by_xpath('//*[@id="FooterPageNav"]/div/ul/li[7]/a')
        except: 
            break
        next_button.click() 
    '''
    for i in range(1, 31):
        # x_path = '//*[@id="MainCol"]/div[1]/ul/li[i]'
        i = str(i)
        x_path='//*[@id="MainCol"]/div[1]/ul/li['+(i)+(']')
        company_name = driver.find_element_by_xpath(x_path)
        job_info = company_name.text
        job_v1 = [job_info]
        job_v1 = job_v1[0].split('\n')
        job_vector.append(job_v1)
    return job_vector

# Funktion som tar fram hur många kolumner som behövs i DataFrame: 
def col_nbr(lst):
    maxList = max(lst, key=lambda i:len(i))
    maxLength = len(maxList)
    return maxLength


# test11

# FUNKTION SOM SKAPAR PANDAS DATAFRAME
def create_dataframe(number_of_cols, job_vector): 
    df_jobb = pd.DataFrame
    if number_of_cols == 5:
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    elif number_of_cols==6: 
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch', 'fill_out_1']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    elif number_of_cols==7: 
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch', 'fill_out_1', 'fill_out_2']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    elif number_of_cols==7: 
        columns = ['Comp', 'Title', 'Location', 'status', 'Fresch', 'fill_out_1', 'fill_out_2']
        df_jobb = pd.DataFrame(data=job_vector, columns=columns)
    else: 
        print('fel i create_dataframe... ')
    return df_jobb

""" df_jobb = create_dataframe(job_vector)
print(df_jobb) 

nex_el = driver.find_element_by_class_name('next')
time.sleep(10)

policy_element=driver.find_element_by_id("onetrust-policy-text")
policy_element.click()

#driver.find_element_by_class_name("SVGInline-svg modal_closeIcon-svg")
 

print(policy_element)
nex_el.click()


#Stänger ner chrome
time.sleep(3)
driver.close()

# sök i ordningen: ID, class, name 
 """