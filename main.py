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
    
    # 계산기 실행
    calculator = SajuCalculator(user_date)
    result = calculator.calculate()

    # 결과 출력
    print("\n" + "=" * 10)
    print(result["top"])
    print(result["bottom"])
    print("=" * 10)

if __name__ == "__main__":
    main()