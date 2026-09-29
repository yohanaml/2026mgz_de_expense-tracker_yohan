# v0.1 — 카테고리별 지출 합계 CLI

환율 연동 개인 지출 트래커 MVP의 첫 번째 버전입니다. 외부 라이브러리 없이 Python 표준 라이브러리만 사용합니다.

## 실행 방법

```bash
python summarize.py
```

같은 폴더의 `expenses.csv`를 읽어서 카테고리별·통화별 합계를 출력합니다. 다른 파일을 쓰려면:

```bash
python summarize.py 내파일.csv
```

## 파일 구성

- `expenses.csv` — 연습용 샘플 지출 데이터 (직접 수정하거나 행을 추가해보세요)
- `summarize.py` — CSV를 읽고 집계하는 스크립트

## 이번 버전에서 연습하는 것

- 파일 읽기 (`open`, `csv.DictReader`)
- 딕셔너리로 데이터 집계하기 (`collections.defaultdict`)
- 함수를 역할별로 나누기 (`read_expenses`, `summarize_by_category`, `print_summary`)
- 잘못된 데이터를 만났을 때 예외처리 (`try/except`, `FileNotFoundError`, `ValueError`)

## 다음 단계로 넘어가는 기준 (v0.1 → v0.2)

- [ ] `expenses.csv`에 자신의 실제(또는 가상의) 지출 데이터를 10줄 이상 더 추가해봤다
- [ ] 코드를 한 줄씩 읽으며 각 함수가 무엇을 하는지 설명할 수 있다
- [ ] `amount` 칸에 문자를 넣어 일부러 에러를 내보고, 프로그램이 죽지 않고 건너뛰는 것을 확인했다
- [ ] 이 폴더를 GitHub 저장소로 만들어 첫 커밋을 했다

## 다음 버전(v0.2) 예고

지금은 KRW와 USD를 그냥 더하고 있습니다(의도적인 단순화). v0.2에서는 무료 환율 API를 붙여서 외화 지출을 원화로 정확히 환산하고, API 호출이 실패할 때를 대비한 예외처리를 추가합니다.
