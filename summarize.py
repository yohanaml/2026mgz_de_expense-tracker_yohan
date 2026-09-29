"""
v0.1 - 카테고리별 지출 합계 CLI
------------------------------------
목표: CSV 파일을 읽어서 카테고리별로 금액을 더한 뒤 터미널에 보여준다.
사용하는 지식: 파일 I/O, csv 모듈, 딕셔너리, 함수 분리, 예외처리

주의(의도적인 단순화): 이 버전에서는 KRW와 USD를 환율 계산 없이 그냥 더합니다.
통화 환산은 다음 버전(v0.2)에서 환율 API를 붙여 해결할 예정입니다.

실행 방법:
    python summarize.py
    python summarize.py my_expenses.csv   (다른 파일을 쓰고 싶을 때)
"""

import csv
import sys
from collections import defaultdict


def read_expenses(filepath: str) -> list[dict]:
    """CSV 파일을 읽어서 한 줄(row)씩 딕셔너리로 담은 리스트를 반환한다."""
    rows = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"[오류] 파일을 찾을 수 없습니다: {filepath}")
        sys.exit(1)
    return rows


def summarize_by_category(rows: list[dict]) -> dict:
    """카테고리별로 금액을 더해서 {카테고리: 합계} 형태의 딕셔너리로 반환한다."""
    totals = defaultdict(float)
    skipped = 0

    for row in rows:
        category = row.get("category", "미분류")
        amount_str = row.get("amount", "")
        try:
            amount = float(amount_str)
        except ValueError:
            # 금액 칸이 비어있거나 숫자가 아니면 건너뛰고 개수만 센다
            skipped += 1
            continue
        totals[category] += amount

    if skipped:
        print(f"[안내] 금액을 읽을 수 없어 건너뛴 행: {skipped}개")

    return dict(totals)


def summarize_by_currency(rows: list[dict]) -> dict:
    """통화별로도 따로 합계를 내본다 (v0.2에서 환율 환산할 때 쓸 재료)."""
    totals = defaultdict(float)
    for row in rows:
        currency = row.get("currency", "KRW")
        try:
            amount = float(row.get("amount", ""))
        except ValueError:
            continue
        totals[currency] += amount
    return dict(totals)


def print_summary(category_totals: dict, currency_totals: dict) -> None:
    """집계 결과를 사람이 읽기 좋은 형태로 출력한다."""
    print("\n=== 카테고리별 지출 합계 (통화 구분 없이 단순 합산) ===")
    for category, total in sorted(category_totals.items(), key=lambda x: -x[1]):
        print(f"  {category:6s} : {total:,.2f}")

    grand_total = sum(category_totals.values())
    print(f"  {'합계':6s} : {grand_total:,.2f}")

    print("\n=== 통화별 합계 (참고용, v0.2에서 환율 적용 예정) ===")
    for currency, total in currency_totals.items():
        print(f"  {currency} : {total:,.2f}")


def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "expenses.csv"

    rows = read_expenses(filepath)
    if not rows:
        print("[안내] 읽어들인 지출 내역이 없습니다.")
        return

    category_totals = summarize_by_category(rows)
    currency_totals = summarize_by_currency(rows)
    print_summary(category_totals, currency_totals)


if __name__ == "__main__":
    main()
