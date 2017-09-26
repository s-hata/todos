import {Todo} from './todo';

describe('Todo', () => {
  it('モデルのインスタンスを生成できる', () => {
    expect(new Todo()).toBeTruthy();
  });

  it('コンストラクタでインスタンスを初期化できる', () => {
    const todo = new Todo({
      title: 'hello',
      complete: true
    });
    expect(todo.title).toEqual('hello');
    expect(todo.complete).toEqual(true);
  });
});
