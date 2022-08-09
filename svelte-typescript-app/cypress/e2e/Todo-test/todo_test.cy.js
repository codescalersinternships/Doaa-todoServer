import todo_page from "../../pages-objects/todo_page"

describe('it should be able to add a new todo to the list',()=>{
    
    before(function(){
        cy.visit('/')
    })


    it('Create New todo', function(){
        todo_page.createNewtodo()
    })

    it('DeleteExistingTodo', function(){
        todo_page.deleteExistingTodo()
    })

    it('UpdateExisitingTodo', function(){
        todo_page.updateExisitingTodo()
    })

    it('GetExisitingTodo', function(){
        todo_page.getExisitingTodo()
    })

    it('GetUn-exisitingTodo', function(){
        todo_page.getUnExisitingTodo()
    })

    it('Create New todo without entered Task', function(){
        todo_page.createNewTodoWithoutEnteredTask()
    })

    it('DeleteUnExistingTodo', function(){
        todo_page.deleteUnExistingTodo()
    })

    it('UpdateUnExistingTodo', function(){
        todo_page.updateUnExistingTodo()
    })
    it('CreateNewTodoWithCharId', function(){
        todo_page.createNewTodoWithCharId()
    })
     
    it('CreateNewTodoWithExisitingId', function(){
        todo_page.createNewTodoWithExisitingId()
    })
    
    it('convert the checkbox to true then display the todo', function(){
        todo_page.checkboxMark()
    })
    after(function(){
        cy.log('Done')
    })


})