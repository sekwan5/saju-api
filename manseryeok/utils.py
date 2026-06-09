from datetime import datetime

def get_base_year_pillar(year: int) -> tuple[int, int]:
    """
    단순 연도 기반 천간, 지지 인덱스를 반환합니다.
    1984년(갑자년)을 기준으로 계산합니다.
    """
    cheongan_idx = (year - 4) % 10
    jiji_idx = (year - 4) % 12
    return cheongan_idx, jiji_idx

def is_after_ipchun(date: datetime) -> bool:
    """
    입춘(立春)이 지났는지 여부를 확인합니다.
    *주의: 매년 입춘 절입 시각이 다르므로, 상용화를 위해서는 천문 데이터가 필수입니다.
    현재는 임시로 2월 4일 자정 기준으로 판별합니다.
    """
    ipchun_date = datetime(date.year, 2, 4)
    return date >= ipchun_date