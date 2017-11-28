from selenium import webdriver

# This program is designed to open a web browser, go to twitter, parse a text file for a users username and password
# then log them into twitter click the tweet button and post the tweet.

# User must download chromedriver and below put the path to the chromedriver
driver = webdriver.Chrome('D:\\Documents\Miscellaneous\\Coding\\python web automation\\chromedriver.exe')
# This is used to stop the program if the web page takes too long to load
driver.set_page_load_timeout(30)
# Go to twitter.com and then clicks the login button
driver.get('https://twitter.com/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]').click()
# Parses a text file to grab a username and password. username is the first line in the text file and password is the
# second line in the file. It then stores the data into an array and then is grabbed and stored into its appropriate
# variable
file = open('input_data.txt', 'r')
data = []
for line in file:
    line = line.rstrip('\n')
    data.append(line)
file.close()
username = data[0]
password = data[1]
# Sends the username and password to twitter and then clicks the login button
driver.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]').click()
# Clicks the tweet button, sends a message (the actual tweet) and then clicks the tweet button to send the tweet
# once this has been completed the web browser then closes
driver.find_element_by_xpath('//*[@id="global-new-tweet-button"]/span').click()
driver.find_element_by_xpath('//*[@id="tweet-box-global"]').click()
driver.find_element_by_xpath('//*[@id="tweet-box-global"]').send_keys('#This is a test.......................................')
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[3]/div[2]/button/span[1]').click()
driver.implicitly_wait(20)
driver.quit()
