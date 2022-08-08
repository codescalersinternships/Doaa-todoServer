class Todos{
    get GetTitle(){
        return cy.get("h2.svelte-11uzi9e")
    }
    get GetIdInput(){
        return cy.get('#inputID')
    }
    get GetTaskInput(){
        return cy.get('#inputTask')
    }
    get GetSubmitButton(){
        return  cy.get('[type="submit"]')
    }
    
    NavigitorToTodo(){
        this.GetTitle.contains("TODO APP")
        this.GetIdInput.type("15")
        this.GetTaskInput.type("eat")
        this.GetSubmitButton.click()
    }

}

export default new Todos();