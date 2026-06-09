import re
from datetime import datetime
from korean_saju import Saju, load_bundled_data

class SajuCalculator:
    def __init__(self, birth_date: datetime):
        self.birth_date = birth_date
        _, self.solar_terms = load_bundled_data()

    def calculate(self) -> dict:
        """korean-saju 라이브러리를 활용해 두 줄 형태의 사주팔자 결과 반환"""
        saju = Saju.from_birth(
            kst_moment=self.birth_date,
            solar_terms=self.solar_terms,
            longitude=126.9784,     
            yaja_si_separated=True  
        )
        
        # 1. 라이브러리 출력값 분리 (예: ['甲辰(갑진)', '庚午(경오)', '乙丑(을축)', '丙子(병자)'])
        pillars = str(saju).split()
        
        hangul_pillars = []
        for p in pillars:
            # 2. 정규식을 이용해 텍스트에서 한글만 추출 (예: "甲辰(갑진)" -> "갑진")
            hangul = "".join(re.findall(r'[가-힣]', p))
            if hangul:
                hangul_pillars.append(hangul)
        
        # 3. 배열 순서 뒤집기 (년, 월, 일, 시 ➔ 시, 일, 월, 년)
        hangul_pillars.reverse()
        
        # 4. 천간(윗줄)과 지지(아랫줄) 분리
        # 첫 번째 글자들만 모으면 천간, 두 번째 글자들만 모으면 지지가 됨
        top_row = "".join([pillar[0] for pillar in hangul_pillars])
        bottom_row = "".join([pillar[1] for pillar in hangul_pillars])
        
        return {
            "top": top_row,
            "bottom": bottom_row
        }