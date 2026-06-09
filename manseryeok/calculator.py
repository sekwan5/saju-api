import re
from datetime import datetime
from korean_saju import Saju, load_bundled_data

class SajuCalculator:
    def __init__(self, birth_date: datetime):
        self.birth_date = birth_date
        _, self.solar_terms = load_bundled_data()

    def calculate(self) -> dict:
        saju = Saju.from_birth(
            kst_moment=self.birth_date,
            solar_terms=self.solar_terms,
            longitude=126.9784,     
            yaja_si_separated=True  
        )
        
        # 1. 라이브러리 출력값 분리 (순서: 년, 월, 일, 시)
        pillars = str(saju).split()
        
        # 2. 사주 명식 배열을 위해 순서 뒤집기 (순서: 시, 일, 월, 년)
        pillars.reverse()
        pillar_names = ["시주", "일주", "월주", "년주"]
        
        # 3. 프론트엔드로 넘겨줄 구조화된 딕셔너리 생성
        saju_data = {}
        
        for i, p in enumerate(pillars):
            pillar_key = pillar_names[i]
            
            # 정규식으로 한자와 한글 분리 매칭
            match = re.match(r'([一-龥])([一-龥])\(([가-힣])([가-힣])\)', p)
            if match:
                hanja_top, hanja_bottom = match.group(1), match.group(2)
                hangul_top, hangul_bottom = match.group(3), match.group(4)
                
                # 각각의 글자를 변수(Key)에 독립적으로 담기
                saju_data[pillar_key] = {
                    "천간": f"{hangul_top}({hanja_top})",
                    "지지": f"{hangul_bottom}({hanja_bottom})"
                }
            else:
                # 파싱 실패 시 원본 유지 (안전 장치)
                saju_data[pillar_key] = {
                    "천간": p,
                    "지지": p
                }
                
        return saju_data