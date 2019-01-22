
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging
logging.error("+++ pythong version")
logging.error(sys.version_info[0])

#
# driver
#
def btnCb():

    driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://qa.creditninja.com')

    elem = driver.find_element_by_css_selector("#loan_application_wizard_first_name")
    elem.send_keys("firstName")
    elem = driver.find_element_by_css_selector("#loan_application_wizard_last_name")
    elem.send_keys("lastName")
    elem = driver.find_element_by_css_selector("#loan_application_wizard_email")
    elem.send_keys("my@email.com")
    elem = driver.find_element_by_css_selector("#loan_application_wizard_mobile_phone")
    elem.send_keys("4155551234")
    # elem.send_keys(Keys.ENTER)
    elem.submit()

    time.sleep(60 * 60) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!
    driver.quit()


#
# tkinter
#
import tkinter
top = tkinter.Tk()

text = tkinter.Text(top, height=2, width=30)
text.pack()
text.insert(tkinter.END, "Select Environment")

listbox = tkinter.Listbox(top)
listbox.pack()
listbox.insert(tkinter.END, "Staging")
listbox.insert(tkinter.END, "QA")
listbox.insert(tkinter.END, "localhost:3003")

b = tkinter.Button(top, text="Ok", command=btnCb)
b.pack()
top.mainloop()
