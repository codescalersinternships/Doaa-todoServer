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
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.TaskTextField))).send_keys('ten')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.CreateButton))).click()
    
    
    #case3
    def deleteExistingTodo(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.DeleteMark))).click()
    
    
    #case4
    def upadateTodo(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('1')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.TaskTextField))).send_keys('DoaaSaber')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.UpdateButton))).click()
    
    #case5
    def getbyID(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('1')
        wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.GetButton))).click()
    
    #case6
    def getUnExisting(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('16')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.GetButton))).click()
    
    
    #case7
    def createNewTodoWithouttask(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('56')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.CreateButton))).click()
    
    
    #case8
    def deleteUnExisting(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('98')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.DeleteButton))).click()
    

     #case9
    def upadateUnExistingTodo(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('115')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.TaskTextField))).send_keys('DoaaSaber')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.UpdateButton))).click()
    
     #case10
    def createwithChar(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('hello')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.TaskTextField))).send_keys('world')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.CreateButton))).click()
    
     #case11
    def createWithExistingID(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('1')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.TaskTextField))).send_keys('Amira')
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.CreateButton))).click()
    
     #case12
    def convertCheckBox(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.CheckMark))).click()
    