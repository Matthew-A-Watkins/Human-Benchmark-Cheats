from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# open driver
driver = webdriver.Chrome()

# open website
driver.get("https://humanbenchmark.com/tests/verbal-memory")


driver.maximize_window() # For maximizing window
driver.implicitly_wait(10) # gives an implicit wait for 20 seconds

# uncomment to give yourself time to sign in
# input("Ready?")

# init start button

start = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[4]/button')

start.click()
sleep(0.01)

# init the new word button
newWordButton = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[2]')

# init the old word button
oldWordButton = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[3]/button[1]')

# init the word list
wordList = list()

# prompt user for how far they'd like to go
Lvls = int(input("How far would you like to go? "))

for i in range(Lvls):
    # the current word is set to element
    element = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div/div[2]/div')

    word = element.text

    # check if the word is preexisting
    if word in wordList:
        print("old word: {}\n".format(word))
        oldWordButton.click()
        sleep(0.0001)

    # add to word list if not and click the new word button
    else:
        print("new word: {}\n".format(word))
        newWordButton.click()
        wordList.append(word)
        sleep(0.0001)