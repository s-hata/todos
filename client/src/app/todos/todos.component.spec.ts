import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { Router } from '@angular/router';

import { TodosComponent } from './todos.component';
import { FormsModule } from '@angular/forms';
import { TodoDataService } from '../todo-data.service';
import { ApiService } from '../api.service';
import { AuthService } from '../auth.service';
import { ApiMockService } from '../api-mock.service';
import { SessionService } from '../session.service';
import { NO_ERRORS_SCHEMA } from '@angular/core';

describe('TodosComponent', () => {
  let component: TodosComponent;
  let fixture: ComponentFixture<TodosComponent>;
  let mockRouter = {
    navigate: jasmine.createSpy('navigate')
  };

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        FormsModule
      ],
      declarations: [
        TodosComponent
      ],
      providers: [
        AuthService,
        TodoDataService,
        {
          provide: ApiService,
          useClass: ApiMockService
        },
        {
          provide: Router,
          useValue: mockRouter
        },
        SessionService
      ],
      schemas: [
        NO_ERRORS_SCHEMA
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('コンポーネントのインスタンスを生成できる', () => {
    expect(component).toBeTruthy();
  });
});
