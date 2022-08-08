import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

    def test_case1(self):
        todo_page.todo(self.driver).CreateNewTodo()

    def test_case2(self):
        todo_page.todo(self.driver).DeleteExistingTodo()  
    
    def test_case3(self):
        todo_page.todo(self.driver).UpadateTodo() 

    def test_case4(self):
        todo_page.todo(self.driver).GetbyID() 
    
    def test_case5(self):
        todo_page.todo(self.driver).GetUnExisting() 

    def test_case6(self):
        todo_page.todo(self.driver).CreateNewTodoWithouttask() 
    
    def test_case7(self):
        todo_page.todo(self.driver).DeleteUnExisting() 

    def test_case8(self):
        todo_page.todo(self.driver).UpadateUnExistingTodo() 
    
    def test_case9(self):
        todo_page.todo(self.driver).CreatewithChar() 

    def test_case10(self):
        todo_page.todo(self.driver).CreateWithExistingID() 
    
    def test_case11(self):
        todo_page.todo(self.driver).ConvertCheckBox() 


    def tearDown(self):
        self.driver.quit()
        print('DONE')


if __name__ == "__main__":
    unittest.main()