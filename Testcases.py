'''
Created on May 11, 2019

@author: lakshmiarumugam
'''
import xlrd
import time
import logging
from selenium import webdriver

class Test_case1:  
    @classmethod
    def driver_test(self, browser, sheet2):
        sheet2.cell_value(0, 0)
        for rowcount, browserdata in enumerate(sheet2.col_values(0)):
            if browserdata == browser:
                driverloc = sheet2.cell_value(rowcount,1)                            
                break  
        if browser == "firefox":
            driver = webdriver.Firefox(executable_path=driverloc) 
            logging.info("Test running on firefox")   
        elif browser == "chrome":
            driver = webdriver.Chrome(executable_path=driverloc)
            logging.info("Test running on chrome")
        elif browser == "safari":
            driver = webdriver.Safari(executable_path=driverloc)
            logging.info("Test running on safari")
        return driver  
     
    @classmethod
    def execute_login_test(self, browser, env):   
        loc = ("/Users/lakshmiarumugam/Documents/testsupport.xlsx")
        wb = xlrd.open_workbook(loc) 
        sheet2 = wb.sheet_by_index(1) 
        driver = self.driver_test(browser, sheet2)
        sheet1 = wb.sheet_by_index(0)
        sheet1.cell_value(0, 0)
        rowcount1 = 0
        while rowcount1 < sheet1.nrows:
            envdata = (sheet1.cell_value(rowcount1, 0))                 
            if envdata == env:   
                logging.info("Test running on "+envdata + " environment")
                driver.get(sheet1.cell_value(rowcount1,1))
                driver.find_element_by_xpath("//input[@id = 'username']").send_keys(sheet1.cell_value(rowcount1,2))
                driver.find_element_by_xpath("//input[@id = 'password']").send_keys(sheet1.cell_value(rowcount1,3))
                driver.find_element_by_xpath("//button[@type = 'submit']").click();
                expectedmsg =  'The user or password is incorrect.'
                time.sleep(3)
                errormsg = driver.find_element_by_xpath("//span[(@class='warning')]").__getattribute__('text')
                if (expectedmsg == errormsg):
                    logging.info("Invalid login error occured")
                rowcount1 = rowcount1 + 1
                time.sleep(5)
            else:
                rowcount1 = rowcount1 + 1
        return