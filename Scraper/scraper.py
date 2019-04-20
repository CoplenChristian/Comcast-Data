from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from NumberCheck import NumberCheck
import re

def ComcastLogin(user, password):
    usernameStr = user
    passwordStr = password

    browser = webdriver.Chrome()
    browser.get(('https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fauth.xfinity.com%252Foauth%252Fcallback%26client_id%3Dmy-xfinity%26state%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252F%2523%252F%253FCMP%253DILC_signin_myxfinity_re%26response%3D1&client_id=my-xfinity&reqId=d1ef0ba4-cab0-45d6-96b6-a20c52554897'))

    username = browser.find_element_by_id('user')
    username.send_keys(usernameStr)
    password = browser.find_element_by_id('passwd')
    password.send_keys(passwordStr)
    submit = browser.find_element_by_id('sign_in')
    submit.click()

    browser.implicitly_wait(10)

    executed = False

    while executed == False:
        try:
            manage = browser.find_element_by_partial_link_text('Manage Internet')
            manage.click()
            print("Attempted.")
            executed = True
        except:
            print("Did not work.")
            break

    time.sleep(5)
    if browser.current_url == "https://customer.xfinity.com/#/services/internet":
        data = browser.page_source

    months = re.findall('(?<=<b>).+?(?=</b>)', data, re.DOTALL)

    usage = []

    for item in months:
        check = NumberCheck(item)
        if check == True:
            usage.append(item)

    months_clean = [month for month in months if 'Norton' not in month]
    #unused for now
    months_clean2 = [month for month in months_clean if month not in usage]



    used = str(int(months_clean[1].replace("GB", "")) - int(months_clean[0].replace("GB", "")))

    print("You have used " + used, "gigabytes of data so far this month. You still have " + str(months_clean[0].replace("GB", " ")) + "gigabytes of data remaining.")


        
