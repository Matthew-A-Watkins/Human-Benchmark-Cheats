from selenium import webdriver
from time import sleep

# start the driver
driver = webdriver.Chrome()

# open webpage
driver.get('https://humanbenchmark.com/tests/typing')


ready = input("ready? ")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(10) # gives an implicit wait for 10 seconds

# find all letters
letters = driver.find_elements_by_class_name('incomplete')


# compile letters in string
finalString = ""
for letter in letters:
    letter = letter.text
    if letter == " " or letter == "":
        finalString = finalString + " "
    else:
        finalString = finalString + letter 

# init text box
TextBox = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div')

# buffer
sleep(1)

# output
TextBox.send_keys(finalString)
print(finalString)