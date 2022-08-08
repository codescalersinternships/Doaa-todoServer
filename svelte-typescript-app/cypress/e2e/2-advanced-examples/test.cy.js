/// <reference types="cypress"/>

import todo_page from "../../pages/todo_page"

it('it should be able to add a new todo to the list',()=>{
    cy.visit('http://localhost:3001/')
    cy.get('body')

    cy.get('h2.svelte-11uzi9e')
    cy.contains("TODO APP")

    cy.get('[type="submit"]')
    cy.contains("Submit")

    cy.get('#inputID').type("44")

    cy.get('#inputTask').type("github")

    cy.get('[type="submit"]')
    .click()

    cy.get(':nth-child(5) > .btn > i')
    .click()

    cy.get(':nth-child(6) > input')
    .click()

    cy.get("#inputID").type('4').should('have.value','4')

    .get("#inputTask").type('clean').should('have.value','clean')
    
   
  })

  it('it should be able to add a new todo to the list',()=>{    
    todo_page.NavigitorToTodo()
  })

