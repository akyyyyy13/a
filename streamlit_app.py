import streamlit as st
import random
from datetime import datetime

def get_zodiac(month, day):
    zodiac_signs = [
        ("山羊座", (1, 1), (1, 19)),
        ("水瓶座", (1, 20), (2, 18)),
        ("魚座", (2, 19), (3, 20)),
        ("牡羊座", (3, 21), (4, 19)),
        ("牡牛座", (4, 20), (5, 20)),
        ("双子座", (5, 21), (6, 20)),
        ("蟹座", (6, 21), (7, 22)),
        ("獅子座", (7, 23), (8, 22)),
        ("乙女座", (8, 23), (9, 22)),
        ("天秤座", (9, 23), (10, 22)),
        ("蠍座", (10, 23), (11, 21)),
        ("射手座", (11, 22), (12, 21)),
        ("山羊座", (12, 22), (12, 31))
    ]
    
    for sign, start, end in zodiac_signs:
        if (month, day) >= start and (month, day) <= end:
            return sign
    return "不明"

def get_fortune():
    fortunes = [
        "素晴らしい1日になりそうです！",
        "新しい出会いがあるかもしれません。",
        "慎重に行動しましょう。",
        "良いアイデアが浮かぶでしょう。",
        "リラックスする時間を作りましょう。"
    ]
    return random.choice(fortunes)

st.title("今日の星座占い")

today = datetime.now()
zodiac = get_zodiac(today.month, today.day)

st.write(f"今日は{today.year}年{today.month}月{today.day}日です。")
st.write(f"今日の星座は{zodiac}です。")

if st.button("占う"):
    fortune = get_fortune()
    st.write(f"今日の{zodiac}の運勢: {fortune}")


