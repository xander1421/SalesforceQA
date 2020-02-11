import time
from new_list_oport import opportunities #the list containing all the opportunities
from Screenshot import Screenshot_Clipping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

#####################################
ob = Screenshot_Clipping.Screenshot()
#####################################

class GetInfo:
    def __init__(self, opport_nr):
        self.opport_nr = opport_nr # send the opportunity that needs the data gathered

    def set_up(self):
        opts = ChromeOptions()
        opts.add_argument('--user-data-dir=C:\\Users\\USERNAME\\AppData\\Local\\Google\\Chrome\\User Data')
        opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(10)

        url = 'https://salesforce.com/home/home.jsp'
        self.driver.get(url)
        try:
            self.driver.find_element_by_id('Login').click() # click the login button
        except ElementNotInteractableException:
            print('have to use other option of login')
            self.driver.find_element_by_id('hint_00DD0000000r7o0005D0000002R0P3').click() # 
        except NoSuchElementException:
            print('was no need to login')
            pass

    def search_for_the_opportunity(self):
        self.driver.find_element_by_id('phSearchInput').send_keys(self.opport_nr) #send the opportunity name into the field   
        self.driver.find_element_by_id('phSearchButton').click()  #presses the serch button to get the opportunity
        self.driver.find_element_by_xpath('//*[@id="Opportunity_body"]/table/tbody/tr[2]/th/a').click()  #click on the opportinity that was found
    
    def take_opportunity_full_page_screenshot(self):
        opportunity_name_xpath = '/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div[1]/h2'
        opportunity_name= self.driver.find_element_by_xpath(opportunity_name_xpath).text # ge the opportunity name text
        img_url=ob.full_Screenshot(self.driver, save_path=r'images\\', image_name='{}.png'.format(opportunity_name)) # get entire page screenshot of the opportunity

    def get_Forecast_Data(self):
        try:
            self.opportunity_data = []
            for i in range(2, 10):
                Forecast_xpathROW = '/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[10]/div[1]/div/div[2]/table/tbody/tr['+ str(i) +']/td[2]/a'
                            # /html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[10]/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/a
                            # /html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[10]/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/a
                
                            # /html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[10]/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/a  
                get_forecast_name = self.driver.find_element_by_xpath(Forecast_xpathROW).text # get forecast name in text
                # open forecast in a new tab
                forecast_row_elem = self.driver.find_element_by_xpath(Forecast_xpathROW)
                ActionChains(self.driver).move_to_element(forecast_row_elem).key_down(Keys.CONTROL).click().perform() # actionChain that opens the Forecast in a new TAB in the browser
                self.opportunity_data.append(get_forecast_name) # attach the forecast name to the self.opportunity_data LIST
        except NoSuchElementException:
            print('no more rows in Forcast')
            print(self.opportunity_data)
            return self.opportunity_data

    def get_Quotes_Data(self):
            try:
                for i in range(2, 10):
                    Quotes_xpathROW = '/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[11]/div[1]/div/div[2]/table/tbody/tr['+ str(i) +']/th/a'
                                    ## classic salesforce
                                    # '/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[11]/div[1]/div/div[2]/table/tbody/tr[2]/th/a'
                                    # '/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[11]/div[1]/div/div[2]/table/tbody/tr[3]/th/a'
                                    ## lightning mode elements
                                    # /html/body/div[4]/div[1]/section/div/div/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/div/div/section/div/div/div/div[6]/article/div[2]/div/div/div/div/ul/li[1]/div[2]/h3/div/a
                                    # /html/body/div[4]/div[1]/section/div/div/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/div/div/section/div/div/div/div[6]/article/div[2]/div/div/div/div/ul/li[2]/div[2]/h3/div/a
                    get_quotes_name = self.driver.find_element_by_xpath(Quotes_xpathROW).text
                    self.opportunity_data.append(get_quotes_name)
                    # open forecast in a new tab
                    quotes_row_elem = self.driver.find_element_by_xpath(Quotes_xpathROW)
                    # self.driver.find_element_by_xpath(xpathROW).click()  #click on the opportinity that was found
                    ActionChains(self.driver).move_to_element(quotes_row_elem).key_down(Keys.CONTROL).click().perform() # actionChain that opens the Forecast in a new TAB in the browser

            except NoSuchElementException:
                print('no more rows in Quotes')

    # def move_to_tab(self):  # OLD VERSION OF THE MOVE_TO_TAB
    #     parent_handle = self.driver.current_window_handle
    #     handles = self.driver.window_handles
    #     size = len(handles)
    #     window1 = handles[0] # page that the browser opens with 
    #     window2 = handles[1] # second opened tab
    #     window3 = handles[2] # third opened tab
    #     window4 = handles[3] # forth opened tab
    #     print(size)
    #     #############
    #     self.driver.switch_to.window(window2)
    #     img_url=ob.full_Screenshot(self.driver, save_path=r'.', image_name='2.png') # last tab that was oppened
    #     self.driver.switch_to.window(window3)
    #     img_url=ob.full_Screenshot(self.driver, save_path=r'.', image_name='3.png')
    #     self.driver.switch_to.window(window4)
    #     img_url=ob.full_Screenshot(self.driver, save_path=r'.', image_name='4.png') # first tab that was oppened
###############################
###############################
    def move_to_tab2(self):
        self.parent_handle = self.driver.current_window_handle # handler for the parent chrome TAB(Opportunity TAB)
        handles = self.driver.window_handles
        size = len(handles)
        for i in range(1,size):
            window = handles[i] # TAB placeholder in the browser
            self.driver.switch_to.window(window) # move to the tab with the respective Handles[i]
            img_url=ob.full_Screenshot(self.driver, save_path=r'images\\', image_name='{}.png'.format(self.opportunity_data[-i])) # last tab that was oppened
        # print(size)

###############################
    def move_back_to_parent(self):
        self.driver.switch_to.window(self.parent_handle)
        print('Were back at the opportunity page')


if __name__ == "__main__":
    i = 2

    # length = len(opportunities)
    
    # # Iterating using while loop 
    # while i < length: # untill the list gets to the end it will comb over all of them
    a = GetInfo(opportunities[i])
    a.set_up()
    a.search_for_the_opportunity()
    a.take_opportunity_full_page_screenshot()
    a.get_Forecast_Data()
    a.get_Quotes_Data()
    print(opportunities[i])
    # a.move_to_tab()
    a.move_to_tab2()
    a.move_back_to_parent()
        # i += 1



