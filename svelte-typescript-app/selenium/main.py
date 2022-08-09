import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import todo_page

class todoPage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3001/")
        self.driver.maximize_window()
        print('SETUP')

        
    
    def test_todo_page_title(self):
        todo_title = todo_page.todo(self.driver)
        print(self.driver.title)
        assert todo_title.is_title_matching()

    def testCreateNewTodo(self):
        todo_page.todo(self.driver).createNewTodo()

    def testDeleteExistingTodo(self):
        todo_page.todo(self.driver).deleteExistingTodo()  
    
    def testUpadateTodo(self):
        todo_page.todo(self.driver).upadateTodo() 

    def testGetbyID(self):
        todo_page.todo(self.driver).getbyID() 
    
    def testGetUnExisting(self):
        todo_page.todo(self.driver).getUnExisting() 

    def testCreateNewTodoWithouttask(self):
        todo_page.todo(self.driver).createNewTodoWithouttask() 
    
    def testDeleteUnExisting(self):
        todo_page.todo(self.driver).deleteUnExisting() 

    def testUpadateUnExistingTodo(self):
        todo_page.todo(self.driver).upadateUnExistingTodo() 
    
    def testCreatewithChar(self):
        todo_page.todo(self.driver).createwithChar() 

    def testCreateWithExistingID(self):
        todo_page.todo(self.driver).createWithExistingID() 
    
    def testConvertCheckBox(self):
        todo_page.todo(self.driver).convertCheckBox() 


    def tearDown(self):
        self.driver.quit()
        print('DONE')


if __name__ == "__main__":
    unittest.main()