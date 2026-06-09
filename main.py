from datetime import datetime
from manseryeok.calculator import SajuCalculator

def main():
    print("사주를 추출할 생년월일시를 입력해주세요.")
    year = int(input("태어난 연도 (예: 1992): "))
    month = int(input("태어난 월 (예: 8): "))
    day = int(input("태어난 일 (예: 11): "))
    hour = int(input("태어난 시간 (0~23) (예: 20): "))
    minute = int(input("태어난 분 (예: 30): "))

    user_date = datetime(year, month, day, hour, minute)
    
    # 1. API(계산기) 호출 - 구조화된 딕셔너리 데이터를 받음
    calculator = SajuCalculator(user_date)
    saju_data = calculator.calculate()

    # 2. 프론트엔드 렌더링 로직 (받아온 독립된 변수들을 조립)
    top_row = (f"{saju_data['시주']['천간']}\t{saju_data['일주']['천간']}\t"
               f"{saju_data['월주']['천간']}\t{saju_data['년주']['천간']}")
               
    bottom_row = (f"{saju_data['시주']['지지']}\t{saju_data['일주']['지지']}\t"
                  f"{saju_data['월주']['지지']}\t{saju_data['년주']['지지']}")

    # 3. 화면 출력
    print("=" * 40)
    print(top_row)
    print(bottom_row)
    print("=" * 40)

if __name__ == "__main__":
    main()