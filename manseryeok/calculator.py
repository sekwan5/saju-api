from datetime import datetime
from korean_saju import Saju, load_bundled_data

class SajuCalculator:
    def __init__(self, birth_date: datetime):
        self.birth_date = birth_date
        # 1. 라이브러리에 내장된 한국천문연구원(KASI) 절기 데이터를 불러옵니다.
        _, self.solar_terms = load_bundled_data()

    def calculate(self) -> dict:
        """korean-saju 라이브러리를 활용해 최종 사주팔자 결과 반환"""
        
        # 2. 생년월일시와 절기 데이터를 바탕으로 사주 객체를 생성합니다.
        saju = Saju.from_birth(
            kst_moment=self.birth_date,
            solar_terms=self.solar_terms,
            longitude=126.9784,     # 대한민국 서울 경도 기준 (진태양시 보정용)
            yaja_si_separated=True  # 야자시/조자시 분리 적용 (정통 명리학 기준)
        )
        
        # 3. 생성된 saju 객체를 텍스트로 변환하면 "己巳(기사) 丙子(병자) 丙寅(병인) 癸巳(계사)" 형태로 출력됩니다.
        # 이 문자열을 공백을 기준으로 쪼개서 각각 년, 월, 일, 시주에 담아줍니다.
        pillars = str(saju).split()
        
        return {
            "년주": pillars[0], 
            "월주": pillars[1], 
            "일주": pillars[2], 
            "시주": pillars[3]  
        }