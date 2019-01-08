import time, openpyxl, shutil, os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from colorama import Fore
from colorama import init
init()

'''This script logs to FLUX web and find flux jobs using reference.xlsx spreadsheet.
Then it will upload zip files from 05_toASG to correct FLUX task.
'''


dirpath = os.getcwd()
book = openpyxl.load_workbook('reference.xlsx')
sheet = book.active

opts = Options()
opts.set_headless()
assert opts.headless  # operating in headless mode
#browser = Chrome(options=opts)
browser = Chrome()

browser.get('https://flux.olas.net/vendors/tasks')
time.sleep(3)

login_name = browser.find_element_by_name("username")
login_name.send_keys('Kristyna.Vitekerova@jonckers.com')
login_name.submit()
login_pswd = browser.find_element_by_name("password")
login_pswd.send_keys('1V9lfsSU')
login_pswd.submit()
time.sleep(3)

#will set number of rows with content
row_number = 2 #second row in reference sheet
for row_number in range(row_number,100):
    if sheet.cell(row=row_number, column=1).value == None:
        break
    row_number += 1
row_number -= 2

pom = 2

for row in range(row_number):
    job_number = sheet.cell(row=pom, column=1).value

    browser.get('https://flux.olas.net/vendors/tasks')
    time.sleep(3)

    search_form = browser.find_element_by_id('vendortask_searchbox')
    search_form.send_keys(job_number)
    search_form.send_keys(Keys.ENTER)
    time.sleep(3)

    vendortask_table = browser.find_element_by_id('vendortask_table')
    scenario = vendortask_table.text.split(" ")[5].split(" ")[0]
    if str(scenario) == str(job_number): # it will check if job nummber from reference sheet has the same name as scenario name if not then it will print this job must be uploaded to FLUX manually. This check is needed because some job numbers hasthe same  number and This script is taking only first line of Flux table and if there is more  search results oher lines are ignored
        task_ID = vendortask_table.text.split("/")[2].split(" ")[0]
        job_url = "https://flux.olas.net/vendors/tasks/"+task_ID+"/edit"
        print(job_url)

        browser.get(job_url)
        time.sleep(3)

        delivery_field_button = browser.find_element_by_id('id_deliverable_set-0-file')
        delivery_field_button.send_keys(dirpath+f"\\05_toASG\\{job_number}.zip")
        time.sleep(5)
        print(f'{job_number}.zip file uploaded to FLUX')


        delivery_this_task_button = browser.find_element_by_xpath("//button[@type='submit' and @name='deliver']").click()
        print('Deliver button was pushed')
        time.sleep(3)
        deliver_final_button = browser.find_element_by_class_name('regular').click()
        time.sleep(3)
        print('Deliver FINAL button was pushed')
        print(Fore.YELLOW+f'{job_number}.zip sucessfully delivered to FLUX\n'+Fore.RESET)
    else:
        print(Fore.RED+f"!!!!!!!!!!!! {job_number} must be uploaded to FLUX manually !!!!!!!!!!!!"+Fore.RESET)

    pom += 1

time.sleep(2)
browser.close()


