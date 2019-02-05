
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging
logging.error("+++ python version")
logging.error(sys.version_info[0])

import names

#
# variables
#
email = 'victor+%s@creditninja.com' % round(time.time())
state = 'Utah'
firstName = names.get_first_name()
lastName = names.get_last_name()
ssn = round(time.time())

#
# driver
#
def btnCb():

    driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
    driver.get('http://localhost:3003')

    #
    # page 1
    #
    elem = driver.find_element_by_css_selector("#loan_application_wizard_first_name")
    elem.send_keys(firstName)
    elem = driver.find_element_by_css_selector("#loan_application_wizard_last_name")
    elem.send_keys(lastName)
    elem = driver.find_element_by_css_selector("#loan_application_wizard_email")
    elem.send_keys(email)
    elem = driver.find_element_by_css_selector("#loan_application_wizard_mobile_phone")
    elem.send_keys("4155551234")
    # elem.send_keys(Keys.ENTER)
    elem.submit()

    #
    # page 2
    #
    # personal info
    a = '''
      find( "" ).find( :xpath, 'option[2]' ).select_option
      find("", match: :first).click
      fill_in "loan_application_wizard[ssn]", with: @ssn
      fill_in "loan_application_wizard[ssn_confirmation]", with: @ssn
      find(".loan_application_wizard_active_military label.label-radio.no", match: :first ).click
    '''
    elem = driver.find_element_by_css_selector("#loan_application_wizard_date_of_birth_2i")
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == 'May':
            option.click()
            break
    elem = driver.find_element_by_css_selector("#loan_application_wizard_date_of_birth_3i")
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == '15':
            option.click()
            break
    elem = driver.find_element_by_css_selector("#loan_application_wizard_date_of_birth_1i")
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == '1990':
            option.click()
            break
    elem = driver.find_element_by_css_selector('input[name="loan_application_wizard[street_address]"]')
    elem.send_keys("222 2 2222")
    elem = driver.find_element_by_css_selector('input[name="loan_application_wizard[city]"]')
    elem.send_keys("Chicago")
    elem = driver.find_element_by_css_selector('#loan_application_wizard_state')
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == state:
            option.click()
            break
    elem = driver.find_element_by_css_selector('input[name="loan_application_wizard[zip_code]"]')
    elem.send_keys("11223")
    elem = driver.find_element_by_css_selector('#loan_application_wizard_period_at_residence')
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == '1-3 months':
            option.click()
            break
    elem = driver.find_element_by_css_selector('.label-radio+ .label-radio')
    elem.click()
    elem = driver.find_element_by_css_selector('#social-security-number')
    elem.send_keys(ssn)
    elem = driver.find_element_by_css_selector('#social-security-number_confirmation')
    elem.send_keys(ssn)
    elem = driver.find_element_by_css_selector('.no .checkmark')
    elem.click()

    #
    # income
    #
    elem = driver.find_element_by_css_selector('#loan_application_wizard_income_source')
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == 'Employment':
            option.click()
            break
    elem = driver.find_element_by_css_selector('#loan_application_wizard_employer')
    elem.send_keys("My Employer")
    elem = driver.find_element_by_css_selector('#loan_application_wizard_work_phone')
    elem.send_keys("1235551234")
    elem = driver.find_element_by_css_selector('.loan_application_wizard_income_type label:nth-child(2)')
    elem.click()
    elem = driver.find_element_by_css_selector('#loan_application_wizard_pay_period')
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == 'Monthly':
            option.click()
            break
    elem = driver.find_element_by_css_selector('#loan_application_wizard_monthly_income')
    elem.send_keys("2000")
    elem = driver.find_element_by_css_selector('#loan_application_wizard_first_pay_date')
    elem.click()
    elem = driver.find_element_by_css_selector('.prev')
    elem.click()
    elem = driver.find_elements_by_xpath("//td[contains(text(), '5')]")[0]
    elem.click()
    elem = driver.find_element_by_css_selector('#loan_application_wizard_second_pay_date')
    elem.click()
    elem = driver.find_element_by_css_selector('.prev')
    elem.click()
    elem = driver.find_elements_by_xpath("//td[contains(text(), '15')]")[0]
    elem.click()
    elem = driver.find_element_by_css_selector('#loan_application_wizard_pay_date_after_next')
    elem.click()
    elem = driver.find_element_by_css_selector('.prev')
    elem.click()
    elem = driver.find_elements_by_xpath("//td[contains(text(), '27')]")[0]
    elem.click()
    elem = driver.find_element_by_css_selector('.btn-large')
    elem.click()


    #
    # page 3, bank info
    #
    elem = driver.find_element_by_css_selector("#loan_application_wizard_loan_amount")
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == '$1,000':
            option.click()
            break
    elem = driver.find_element_by_css_selector("input[name='loan_application_wizard[bank_routing_number]']")
    elem.send_keys('0740000103')
    elem = driver.find_element_by_css_selector("input[name='loan_application_wizard[bank_routing_number_confirmation]']")
    elem.send_keys('0740000103')
    elem = driver.find_element_by_css_selector("input[name='loan_application_wizard[bank_account_number]']")
    elem.send_keys("549399676")
    elem = driver.find_element_by_css_selector("input[name='loan_application_wizard[bank_account_number_confirmation]']")
    elem.send_keys("549399676")
    elem = driver.find_element_by_css_selector('.btn-large')
    elem.click()

    #
    # page 4, create password
    #
    elem = driver.find_element_by_css_selector("#password")
    elem.send_keys("test1234")
    elem = driver.find_element_by_css_selector("input[name='loan_application_wizard[password_confirmation]']")
    elem.send_keys("test1234")
    elem = driver.find_element_by_css_selector('.btn-large')
    elem.click()

    #
    # page 5, conditional agreement
    #
    elem = driver.find_element_by_css_selector('#submit-agreement')
    elem.click()

    #
    # ibv wizard
    #
    elem = driver.find_element_by_css_selector('#ibv-main-button')
    elem.click()
    elem = driver.find_element_by_css_selector('.ibv-continue')
    elem.click()
    driver.switch_to.frame(driver.find_element_by_css_selector("#q-frame-1549401876104"))
    elem = driver.find_element_by_css_selector('input[name="username"]')
    elem.send_keys("anything")
    elem = driver.find_element_by_css_selector('input[name="password"]')
    elem.send_keys("anything")
    elem = driver.find_element_by_css_selector('button[type="submit"]')
    elem.click()

    #
    # page 6, approved
    #
    elem = driver.find_element_by_css_selector('#view-payday-button')
    elem.click()

    #
    # page 7, agreement signatures
    #
    elem = driver.find_element_by_css_selector('#agreement_signature_0')
    elem.click()
    elem = driver.find_element_by_css_selector('#agreement_signature_1')
    elem.click()
    elem = driver.find_element_by_css_selector('#submit-agreement')
    elem.click()

    #
    # sleep at the end
    #
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
root.state_entry.insert(END, state)
root.state_entry.grid(row=1, column=1)

root.ssn_label = Label(frame2, text="SSN")
root.ssn_label.grid(row=2, column=0, pady=(20, 0))
root.ssn_entry = Entry(frame2)
root.ssn_entry.grid(row=2, column=1, pady=(20, 0))
root.ssn_entry.insert(END, ssn)

root.firstname_label = Label(frame2, text="First Name")
root.firstname_label.grid(row=3, column=0)
root.firstname_entry = Entry(frame2)
root.firstname_entry.grid(row=3, column=1)
root.firstname_entry.insert(END, firstName)

root.lastname_label = Label(frame2, text="Last Name")
root.lastname_label.grid(row=4, column=0)
root.lastname_entry = Entry(frame2)
root.lastname_entry.grid(row=4, column=1)
root.lastname_entry.insert(END, lastName)

root.lastname_label = Label(frame2, text="Email")
root.lastname_label.grid(row=5, column=0)
root.lastname_entry = Entry(frame2)
root.lastname_entry.grid(row=5, column=1)
root.lastname_entry.insert(END, email)

root.mainloop()
