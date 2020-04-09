from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Insta:
    def __init__(self,username,passsword):
        self.username = username
        self.password = passsword
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?hl=en')
        time.sleep(3)
        user = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        print(user)
        user.clear()
        password.clear()
        user.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(8)
        bot.find_element_by_class_name('HoLwm').click()
        time.sleep(3)
        
       
    def openAccountpage(self,accountname):
        bot = self.bot
        bot.find_element_by_link_text(f'{accountname}').click()
       
    def unfollower(self,accountname):
        bot = self.bot
        self.openAccountpage(accountname)
        time.sleep(8)
        links = bot.find_elements_by_class_name('Y8-fY ')
        links[2].click()
        time.sleep(3)
        followings = bot.find_elements_by_class_name('Pkbci')
        for i in range(len(followings)):
            followings[i].click()
            time.sleep(3)
            bot.find_element_by_class_name('-Cab_').click()
            time.sleep(2)
        
        
    def __main__():
        accountname = input('enter account username\n')       
        password = input('enter account password\n')
        ob = Insta(accountname,password)  
        ob.login()
        ob.unfollower(accountname)



