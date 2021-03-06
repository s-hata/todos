/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { TodoListHeaderComponent } from './todo-list-header.component';
import { FormsModule } from '@angular/forms';

describe('TodoListHeaderComponent', () => {
  let component: TodoListHeaderComponent;
  let fixture: ComponentFixture<TodoListHeaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        FormsModule
      ],
      declarations: [ TodoListHeaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodoListHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('コンポーネントのインスタンスを生成できる', () => {
    expect(component).toBeTruthy();
  });

  it('ヘッダーに表示されるタイトルがTodos Listである', () => {
    let title = fixture.debugElement.query(By.css('h1'));
    let titleElement = title.nativeElement;
    expect(titleElement.textContent).toBe('Todos List');
  });
});
