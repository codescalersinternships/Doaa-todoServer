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



    //create new todo , by entering the new id , its task and click on create button
    createNewtodo(){

        this.getTitle().contains("TODO APP")
        this.getIdInput().type("166")
        this.getTaskInput().type("eaten")
        this.getSubmitButton().click()
    }
    //delete todo , by entering the id and click on delete button

    deleteExistingTodo(){
        this.getDeleteMark().click()
    }

    //update  todo , by entering the id and its task and click on update button

    updateExisitingTodo(){
         this.getIdInput().type("1")
         this.getTaskInput().type("DoaaSaber")
         this.getUpdateButton().click()
        }
        
        //get todo , by entering the id and click on get button

    getExisitingTodo(){
        this.getIdInput().type("1")
        this.getButton().click()}

   //get todo , by entering un-existing id and click on get button
 
    getUnExisitingTodo(){
    this.getIdInput().clear({force: true})
    this.getIdInput().type("15")
    this.getButton().click()

    }


    //create new todo , by entering the new id and click on create button

    createNewTodoWithoutEnteredTask(){
    this.getIdInput().type("9")
    this.getSubmitButton().click()}

    //delete todo , by entering un-existing id and click on delete button

    deleteUnExistingTodo(){
    this.getIdInput().type("36")
    this.getDeleteButton().click()
    }

    //update  todo , by entering un-existing id and its task and click on update button

    updateUnExistingTodo(){
        this.getIdInput().type("88")
        this.getTaskInput().type("DoaaSaber")
        this.getUpdateButton().click()
    }

    //create new todo , by entering the new id(begain with character) , its task and click on create button

    createNewTodoWithCharId(){
        this.getIdInput().type("BB")
        this.getTaskInput().type("jj")
        this.getSubmitButton().click()
    }

    //create new todo , by entering the existing id ,its task and click on create button

    createNewTodoWithExisitingId(){
        this.getIdInput().type("1")
        this.getTaskInput().type("amira")
        this.getSubmitButton().click()
    }

    //click on the checkbox to toggle the "done" 

    checkboxMark(){
        this.getcheckMark().click()
        this.getIdInput().type(" ")
        this.getIdInput().type(1)
        this.getButton()
    }
    
}
export default new todo();