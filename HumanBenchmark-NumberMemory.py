from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# start the driver
driver = webdriver.Chrome()

# open webpage
driver.get('https://humanbenchmark.com/tests/number-memory')

driver.maximize_window() # For maximizing window
driver.implicitly_wait(10) # gives an implicit wait for 10 seconds

# allow for input of variable amount of levels while also allowing the ability to sign in
lvls = int(input("Amount of levels "))

# click start button
start = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button')

start.click()

for i in range(lvls-1):

    # increase by 1 to increase the precision of the delay
    i+=1
    
    driver.implicitly_wait(2) # buffer

    # declare number for current iteration
    number = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[1]')

    currentNumber = number.text

    driver.implicitly_wait(i*2)

    # write currentNumber in the text box
    print("writing {}\n".format(currentNumber))
    textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[2]/input')
    textbox.send_keys(currentNumber)

    driver.implicitly_wait(1)

    # click submit
    print("Pressing Submit\n")
    submit = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/form/div[3]/button')
    submit.click()

    # click next
    driver.implicitly_wait(2) # buffer
    print("clicking Next\n")
    next = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/button')
    next.click()

