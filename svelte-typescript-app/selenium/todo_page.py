from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import *

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class todo(BasePage):
     #case1 
    def is_title_matching(self):
        return 'TODO' in self.driver.title
    
    #case2
    def createNewTodo(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('10')

         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('ten')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
    
    #case3
    def deleteExistingTodo(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.DeleteMark).click()
    
    
    #case4
    def upadateTodo(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('1')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('DoaaSaber')
         self.driver.find_element(By.XPATH, todoPage.UpdateButton).click()
    
    #case5
    def getbyID(self):
        wait = WebDriverWait(self.driver, 60)
        self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('1')
        self.driver.find_element(By.XPATH, todoPage.GetButton).click()
    
    #case6
    def getUnExisting(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('16')
         self.driver.find_element(By.XPATH, todoPage.GetButton).click()
    
    
    #case7
    def createNewTodoWithouttask(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('56')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
    
    #case8
    def deleteUnExisting(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('98')
         self.driver.find_element(By.XPATH, todoPage.DeleteButton).click()
    

     #case9
    def upadateUnExistingTodo(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('115')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('DoaaSaber')
         self.driver.find_element(By.XPATH, todoPage.UpdateButton).click()
    
     #case10
    def createwithChar(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('hello')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('world')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
     #case11
    def createWithExistingID(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('1')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('Amira')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
     #case12
    def convertCheckBox(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.CheckMark).click()
    