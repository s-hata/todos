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
    browser.sleep(3000);
    page.doSignIn()
    browser.takeScreenshot().then(function (png) {
        writeScreenShot(png, 'screenshot/sign-in-after.png');
    });
    expect(page.getTitleText()).toEqual('Todos');
  });

  it('should add Todos', () => {
    page.addTodo('Todo 1');
    page.addTodo('Todo 2');
    browser.sleep(3000);
    browser.takeScreenshot().then(function (png) {
        writeScreenShot(png, 'screenshot/add-todo.png');
    });
    expect(page.getTitleText()).toEqual('Todos');
  });

  it('should done Todo item', () => {
    page.done("Todo 1");
    browser.sleep(3000);
    browser.takeScreenshot().then(function (png) {
        writeScreenShot(png, 'screenshot/done-todo.png');
    });
  });

  it('should delete Todo item', () => {
    page.delete();
    browser.sleep(3000);
    browser.takeScreenshot().then(function (png) {
        writeScreenShot(png, 'screenshot/delete-todo.png');
    });
  });

});

function writeScreenShot(data, filename) {
    var stream = fs.createWriteStream(filename);
    stream.write(new Buffer(data, 'base64'));
    stream.end();
}
