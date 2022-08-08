class todo{
    GetTitle(){
        return cy.get('h2.svelte-1odsl5c')
    }
     GetIdInput(){
        return cy.get('#inputID')
    }
     GetTaskInput(){
        return cy.get('#inputTask')
    }
     GetSubmitButton(){
        return  cy.get('[type="create"]')
    }
     GetUpdateButton(){
        return cy.get('[type="update"]')
    }
     GetDeleteButton(){
        return cy.get('[type="delete"]')
    }
     GetButton(){
        return cy.get('[type="get"]')
    }
     GetDeleteMark(){
       return cy.get(':nth-child(5) > .btn > i')
    }

    GetcheckMark(){
        return cy.get(':nth-child(6) > input')
    }



    case2(){
        //case2
        this.GetTitle().contains("TODO APP")
        this.GetIdInput().type("166")
        this.GetTaskInput().type("eaten")
        this.GetSubmitButton().click()
    }
    //case3
    case3(){
        this.GetDeleteMark().click()
    }

    //case4
    case4(){
         this.GetTitle().contains("TODO APP")
         this.GetIdInput().type("1")
         this.GetTaskInput().type("DoaaSaber")
         this.GetUpdateButton().click()}
        
        //case5
        case5(){
        this.GetTitle().contains("TODO APP")
        this.GetIdInput().type("1")
        this.GetButton().click()}

        //case6 
        case6(){
        this.GetTitle().contains("TODO APP")
        this.GetIdInput().clear({force: true})
        this.GetIdInput().type("15")
        this.GetButton().click()
        }


        //case7
        case7(){
        this.GetTitle().contains("TODO APP")
        this.GetIdInput().type("9")
        this.GetSubmitButton().click()}
 
        //case8
        case8(){
        this.GetTitle().contains("TODO APP")
        this.GetIdInput().type("36")
        this.GetDeleteButton().click()
        }

        //case9
        case9(){
        this.GetTitle().contains("TODO APP")
         this.GetIdInput().type("88")
         this.GetTaskInput().type("DoaaSaber")
         this.GetUpdateButton().click()
        }
  
        //case10
        case10(){
            this.GetTitle().contains("TODO APP")
            this.GetIdInput().type("BB")
            this.GetTaskInput().type("jj")
            this.GetSubmitButton().click()
        }

        //case11
        case11(){
            this.GetTitle().contains("TODO APP")
            this.GetIdInput().type("1")
            this.GetTaskInput().type("amira")
            this.GetSubmitButton().click()
        }

        //case12
        case12(){
            this.GetTitle().contains("TODO APP")
            this.GetcheckMark().click()
            this.GetIdInput().type(" ")
            this.GetIdInput().type(1)
            this.GetButton
        }
    
}
export default new todo();