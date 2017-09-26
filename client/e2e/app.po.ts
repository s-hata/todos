import { protractor, browser, element, by } from 'protractor';

export class TodoAppPage {
  navigateTo() {
    return browser.get('/');
  }

  getTitleText() {
    return element(by.css('app-root h1')).getText();
  }

  setUsername(username) {
    let usernameInput = element(by.css("#username"));
    usernameInput.sendKeys(username);
  }

  setPassword(password) {
    let usernameInput = element(by.css("#password"));
    usernameInput.sendKeys(password);
  }

  doSignIn() {
    let signInButton = element(by.css("#sign-in"));
    signInButton.click();
  }

  addTodo(title) {
    let newTodoInput = element(by.css(".new-todo"));
    newTodoInput.sendKeys(title);
    newTodoInput.sendKeys(protractor.Key.ENTER);
  }

  done(label) {
    let todo1 = element(by.cssContainingText("label", label));
    todo1.click();
  }

  delete() {
    var todos = element.all(by.css('.destroy'));
    todos.last().click();
  }

}
