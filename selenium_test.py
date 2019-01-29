
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging
logging.error("+++ python version")
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
# from tkinter import *
root = tkinter.Tk()

## select environment
root.text = tkinter.Text(root.master, height=2, width=30)
root.text.insert(tkinter.END, "Select Environment")
root.text.grid(row=0, column=0)

root.listbox = tkinter.Listbox(root.master)
root.listbox.insert(tkinter.END, "Staging")
root.listbox.insert(tkinter.END, "QA")
root.listbox.grid(row=1, column=0)

root.routing_label = tkinter.Label(root.master, text="Routing Number")
root.routing_label.grid(row=0, column=1)
root.routing_entry = tkinter.Entry(root)
root.routing_entry.grid(row=1, column=2)
root.state_label = tkinter.Label(root.master, text="State")
root.state_label.grid(row=1, column=1)
root.state_entry = tkinter.Entry(root)
root.state_entry.grid(row=1, column=2)

# b = tkinter.Button(root, text="Run", command=btnCb)
# b.pack()

root.mainloop()
