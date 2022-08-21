from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import *

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
#get the title of the page
class todo(BasePage):
    def is_title_matching(self):
        return 'TODO' in self.driver.title

    #create new todo , by entering the new id , its task and click on create button
    def createNewTodo(self):
         wait = WebDriverWait(self.driver, 60)
         wait.until(EC.visibility_of_element_located((By.XPATH, todoPage.IdTextField))).send_keys('10')

         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('ten')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
     #delete todo , by entering the id and click on delete button
    def deleteExistingTodo(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.DeleteMark).click()
    
    #update  todo , by entering the id and its task and click on update button
    def upadateTodo(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('1')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('DoaaSaber')
         self.driver.find_element(By.XPATH, todoPage.UpdateButton).click()
    
     #get todo , by entering the id and click on get button
    def getbyID(self):
        wait = WebDriverWait(self.driver, 60)
        self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('1')
        self.driver.find_element(By.XPATH, todoPage.GetButton).click()
    
     #get todo , by entering un-existing id and click on get button
    def getUnExisting(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('16')
         self.driver.find_element(By.XPATH, todoPage.GetButton).click()
    
    #create new todo , by entering the new id and click on create button
    def createNewTodoWithouttask(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('56')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
     #delete todo , by entering un-existing id and click on delete button
    def deleteUnExisting(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('98')
         self.driver.find_element(By.XPATH, todoPage.DeleteButton).click()
    
    #update  todo , by entering un-existing id and its task and click on update button
    def upadateUnExistingTodo(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('115')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('DoaaSaber')
         self.driver.find_element(By.XPATH, todoPage.UpdateButton).click()
      
     #create new todo , by entering the new id(begain with character) , its task and click on create button
    def createwithChar(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('hello')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('world')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
     #create new todo , by entering the existing id ,its task and click on create button
    def createWithExistingID(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.IdTextField).send_keys('1')
         self.driver.find_element(By.XPATH, todoPage.TaskTextField).send_keys('Amira')
         self.driver.find_element(By.XPATH, todoPage.CreateButton).click()
    
    #click on the checkbox to toggle the "done" 
    def convertCheckBox(self):
         wait = WebDriverWait(self.driver, 60)
         self.driver.find_element(By.XPATH, todoPage.CheckMark).click()
    