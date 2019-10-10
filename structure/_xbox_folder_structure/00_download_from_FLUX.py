import time, openpyxl, shutil, os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

'''This script will connect to FLUX page using Selenium.
It will enter login and password.
Then it will conect to Excel sheet and reads FLUX ID.
Then it will use these FLUX IDs to find a job.
It will read minimal/maximal adjuset and number uf markets based on lines of table.
Then it will download xliffs.zip file, rename it accordind to FLUX ID and move ro project folder '''

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
login_name.send_keys('XXX.XXX@jonckers.com')
login_name.submit()
login_pswd = browser.find_element_by_name("password")
login_pswd.send_keys('XXX')
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

xbox_25 = True
for row in range(row_number):
    job_number = sheet.cell(row=pom, column=1).value

    browser.get('https://flux.olas.net/vendors/tasks')
    time.sleep(3)

    search_form = browser.find_element_by_id('vendortask_searchbox')
    search_form.send_keys(job_number)
    search_form.send_keys(Keys.ENTER)
    time.sleep(3)

    vendortask_table = browser.find_element_by_id('vendortask_table')
    task_ID = vendortask_table.text.split("/")[2].split(" ")[0]
    job_url = "https://flux.olas.net/vendors/tasks/"+task_ID+"/edit"
    print(job_url)

    browser.get(job_url)

    adjusted_table = browser.find_element_by_class_name('model_list').text
    if "(zh-cn)" in adjusted_table: 
        xbox_25 = False
        print("zh-CN present in task. 26-markets tamplate will be used")
    adjusted_table_list = adjusted_table.splitlines()
    list_of_adjusted = []
    for x in adjusted_table_list[1:]:
        list_of_adjusted.append(float(x.split(" ")[-1]))
    markets = len(adjusted_table_list) - 1
    minimal_adjusted = round(min(list_of_adjusted))
    maximal_adjusted = round(max(list_of_adjusted))
    print(f"{pom-1}.\tJob ID: {job_number}; Markets: {markets}; Minimal adjusted: {minimal_adjusted}; Maximal adjusted: {maximal_adjusted}" )

    sheet.cell(row=pom, column=4).value = markets
    sheet.cell(row=pom, column=5).value = minimal_adjusted

    xliff_link = browser.find_element_by_partial_link_text("xliffs.zip")
    xliff_link.click()
    time.sleep(3)

    shutil.move(f"c:\\Users\\SlavP\\Downloads\\xliffs.zip", dirpath+f"\\00_source\\{job_number}.zip")
    pom += 1
    
if xbox_25:
    os.remove("01_CreateProject___XBOX_26.cmd")
else:
    os.remove("01_CreateProject___XBOX_25.cmd")


book.save('reference.xlsx')
print("Table saved. DONE")
browser.close()


