import streamlit as st
import random
from datetime import datetime

# 星座判定関数
def get_zodiac(month, day):
    zodiac_dates = [
        (1, 20, "山羊座"), (2, 19, "水瓶座"), (3, 20, "魚座"), (4, 20, "牡羊座"),
        (5, 21, "牡牛座"), (6, 21, "双子座"), (7, 23, "蟹座"), (8, 23, "獅子座"),
        (9, 23, "乙女座"), (10, 23, "天秤座"), (11, 22, "蠍座"), (12, 22, "射手座"),
        (12, 31, "山羊座")
    ]
    date = (month, day)
    for (m, d, sign) in zodiac_dates:
        if date <= (m, d):
            return sign
    return "山羊座"

# 運勢生成関数
def get_fortune():
    fortunes = [
        "素晴らしい1日になるでしょう！", "新しい出会いがあるかもしれません。",
        "慎重に行動しましょう。", "良いアイデアが浮かぶでしょう。",
        "リラックスする時間を作りましょう。"
    ]
    return random.choice(fortunes)

# Streamlitアプリ
st.title("星座占いアプリ")

# 誕生日入力
birth_date = st.date_input("誕生日を選択してください")

if st.button("占う"):
    # 星座判定
    zodiac = get_zodiac(birth_date.month, birth_date.day)
    
    # 運勢生成
    fortune = get_fortune()
    
    # 結果表示
    st.subheader(f"あなたの星座: {zodiac}")
    st.write(f"今日の運勢: {fortune}")

