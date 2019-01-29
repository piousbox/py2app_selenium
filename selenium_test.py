
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging
logging.error("+++ python version")
logging.error(sys.version_info[0])

#
# variables
#
email = 'victor+%s@creditninja.com' % round(time.time())

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
    elem.send_keys(email)
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
from tkinter import Button, Canvas, END, Entry, Frame, Label, Listbox, Text, Tk, SUNKEN
root = Tk()
root.geometry('600x260')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

frame1 = Frame(root) # , background="Blue")
frame2 = Frame(root) # , background="Red")

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")

## select environment - label
root.text = Text(frame1, height=2, width=30)
root.text.insert(END, "Select Environment")
root.text.grid()
## select environment - select
root.listbox = Listbox(frame1)
root.listbox.insert(END, "Staging")
root.listbox.insert(END, "QA")
root.listbox.insert(END, "localhost:3000")
root.listbox.insert(END, "localhost:3003")
root.listbox.grid()
## button, go
b = Button(frame1, relief=SUNKEN, text="Run", command=btnCb, highlightbackground="gray", padx=10 ) # "#91ffe9"
b.grid(pady=10)

# label1 = Label(frame1,text='Label1')
# label1.grid()
root.routing_label = Label(frame2, text="Routing Number")
root.routing_label.grid(row=0, column=0)
root.routing_entry = Entry(frame2)
root.routing_entry.grid(row=0, column=1)
root.routing_entry.insert(END, '0740000103')

root.state_label = Label(frame2, text="State")
root.state_label.grid(row=1, column=0)
root.state_entry = Entry(frame2)
root.state_entry.insert(END, 'UT')
root.state_entry.grid(row=1, column=1)

root.ssn_label = Label(frame2, text="SSN")
root.ssn_label.grid(row=2, column=0, pady=(20, 0))
root.ssn_entry = Entry(frame2)
root.ssn_entry.grid(row=2, column=1, pady=(20, 0))
root.ssn_entry.insert(END, '1231231234')

root.firstname_label = Label(frame2, text="First Name")
root.firstname_label.grid(row=3, column=0)
root.firstname_entry = Entry(frame2)
root.firstname_entry.grid(row=3, column=1)
root.firstname_entry.insert(END, 'Alex')

root.lastname_label = Label(frame2, text="Last Name")
root.lastname_label.grid(row=4, column=0)
root.lastname_entry = Entry(frame2)
root.lastname_entry.grid(row=4, column=1)
root.lastname_entry.insert(END, 'Smith')

root.lastname_label = Label(frame2, text="Email")
root.lastname_label.grid(row=5, column=0)
root.lastname_entry = Entry(frame2)
root.lastname_entry.grid(row=5, column=1)
root.lastname_entry.insert(END, email)

root.mainloop()
