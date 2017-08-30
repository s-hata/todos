const fs = require('fs');
import { TodoAppPage } from './app.po';
import { browser } from 'protractor';

describe('todo-app App', () => {
  let page: TodoAppPage;

  beforeEach(() => {
    page = new TodoAppPage();
  });

  it('should title is Todos', () => {
    page.navigateTo();
    browser.takeScreenshot().then(function (png) {
        writeScreenShot(png, 'screenshot/sign-in-before.png');
    });
    expect(page.getTitleText()).toEqual('Todos');
  });

  it('should demo user sign-in', () => {
    page.setUsername('demo');
    page.setPassword('demo');
    page.doSignIn()
    browser.takeScreenshot().then(function (png) {
        writeScreenShot(png, 'screenshot/sign-in-after.png');
    });
    expect(page.getTitleText()).toEqual('Todos List');
  });

  it('should add Todos', () => {
    page.addTodo('Todo 1');
    browser.takeScreenshot().then(function (png) {
        writeScreenShot(png, 'screenshot/add-todo.png');
    });
    expect(page.getTitleText()).toEqual('Todos List');
  });

});

function writeScreenShot(data, filename) {
    var stream = fs.createWriteStream(filename);
    stream.write(new Buffer(data, 'base64'));
    stream.end();
}
