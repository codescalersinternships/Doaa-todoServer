import todo_page from "../../pages/todo_page"

describe('it should be able to add a new todo to the list',()=>{
    
    before(function(){
        cy.visit('http://localhost:3001/')
    })


    it('Create New todo', function(){
        todo_page.case2()
    })

    it('Delete existing todo', function(){
        todo_page.case3()
    })

    it('Update exisiting todo', function(){
        todo_page.case4()
    })

    it('Get exisiting todo', function(){
        todo_page.case5()
    })

    it('Get Un-exisiting todo', function(){
        todo_page.case6()
    })

    it('Create New todo without entered Task', function(){
        todo_page.case7()
    })

    it('Delete Un-existing todo', function(){
        todo_page.case8()
    })

    it('Update Un-existing todo', function(){
        todo_page.case9()
    })
    it('Create New todo with char id', function(){
        todo_page.case10()
    })
     
    it('Create New todo with exisiting id', function(){
        todo_page.case11()
    })
    
    it('convert the checkbox to true then display the todo', function(){
        todo_page.case12()
    })
    after(function(){
        cy.log('Done')
    })


})