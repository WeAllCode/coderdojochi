import faker from "faker";


describe("Create a course through admin", () => {
    it("Log into admin", () => {
        cy.visit('/dj-admin');
        cy.get('#id_username').type('gregoriofs+admin@uchicago.edu');
        cy.get('#id_password').type('admin');
        cy.contains('Log in').click();
        cy.get('#user-tools > strong').should('have.text',"Ali");
    })

    it("Adds a course", () => {
        cy.get('tbody > .model-course > td:first').click();
        cy.get('#id_username').type('gregoriofs+admin@uchicago.edu');
        cy.get('#id_password').type('admin');
        cy.contains('Log in').click();

        const title = faker.lorem.word(6);
        const code = `${title}${faker.datatype.number()}`;
        const duration = `0${faker.datatype.number({min: 1, max: 4})}:00:00`;
        const description = faker.lorem.words(10);
        const minAge = faker.datatype.number({min: 7, max: 10});
        const maxAge = minAge + 8;

        cy.get('#id_code').type(code);
        cy.get('#id_title').type(title);
        cy.get('#id_description').type(description);
        cy.get('#id_duration').clear().type(duration);
        cy.get('#id_minimum_age').clear().type(minAge);
        cy.get('#id_maximum_age').clear().type(maxAge);

        cy.contains('Save').click();

        cy.get('.success').should('exist');
    })
})