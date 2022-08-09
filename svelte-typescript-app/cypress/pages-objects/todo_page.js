class todo{
    getTitle(){
        return cy.get('h2.svelte-1odsl5c')
    }
     getIdInput(){
        return cy.get('#inputID')
    }
     getTaskInput(){
        return cy.get('#inputTask')
    }
     getSubmitButton(){
        return  cy.get('[type="create"]')
    }
     getUpdateButton(){
        return cy.get('[type="update"]')
    }
     getDeleteButton(){
        return cy.get('[type="delete"]')
    }
     getButton(){
        return cy.get('[type="get"]')
        
    }
     getDeleteMark(){
       return cy.get(':nth-child(5) > .btn > i')
    }

    getcheckMark(){
        return cy.get(':nth-child(6) > input')
    }



    createNewtodo(){
        //case2
        this.getTitle().contains("TODO APP")
        this.getIdInput().type("166")
        this.getTaskInput().type("eaten")
        this.getSubmitButton().click()
    }
    //case3
    deleteExistingTodo(){
        this.getDeleteMark().click()
    }

    //case4
    updateExisitingTodo(){
         this.getIdInput().type("1")
         this.getTaskInput().type("DoaaSaber")
         this.getUpdateButton().click()
        }
        
        //case5
    getExisitingTodo(){
        this.getIdInput().type("1")
        this.getButton().click()}

        //case6 
    getUnExisitingTodo(){
    this.getIdInput().clear({force: true})
    this.getIdInput().type("15")
    this.getButton().click()

    }


    //case7
    createNewTodoWithoutEnteredTask(){
    this.getIdInput().type("9")
    this.getSubmitButton().click()}

    //case8
    deleteUnExistingTodo(){
    this.getIdInput().type("36")
    this.getDeleteButton().click()
    }

    //case9
    updateUnExistingTodo(){
        this.getIdInput().type("88")
        this.getTaskInput().type("DoaaSaber")
        this.getUpdateButton().click()
    }

    //case10
    createNewTodoWithCharId(){
        this.getIdInput().type("BB")
        this.getTaskInput().type("jj")
        this.getSubmitButton().click()
    }

    //case11
    createNewTodoWithExisitingId(){
        this.getIdInput().type("1")
        this.getTaskInput().type("amira")
        this.getSubmitButton().click()
    }

    //case12
    checkboxMark(){
        this.getcheckMark().click()
        this.getIdInput().type(" ")
        this.getIdInput().type(1)
        this.getButton()
    }
    
}
export default new todo();