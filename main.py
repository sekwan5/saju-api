# main.py
from datetime import datetime
from manseryeok.calculator import SajuCalculator

def main():
    # 1. 테스트할 생년월일시 입력 
    # 실제 서비스에서는 사용자에게 입력받는 부분
    test_date = datetime(1992, 8, 28, 20, 29)
    
    print(f"입력된 생년월일시: {test_date}")
    print("-" * 30)

    # 2. 계산기 인스턴스 생성 및 실행
    calculator = SajuCalculator(test_date)
    result = calculator.calculate()

    # 3. 결과 출력
    print("✨ 사주팔자 추출 결과 ✨")
    for pillar, value in result.items():
        print(f"{pillar}: {value}")

if __name__ == "__main__":
    main()