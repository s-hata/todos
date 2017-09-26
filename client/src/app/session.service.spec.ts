import { TestBed, inject } from '@angular/core/testing';

import { SessionService } from './session.service';

describe('SessionService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SessionService]
    });
  });

  it('サービスのインスタンスをインジェクションできる', inject([SessionService], (service: SessionService) => {
    expect(service).toBeTruthy();
  }));
});
