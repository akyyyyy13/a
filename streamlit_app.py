# Streamlitライブラリをインポート
import streamlit as st
import random

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('星座おみくじ')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの星座を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('星座を入力する')
　　if user_input:  # 星座が入力されているかチェック
        st.success(f'🌟 こんにちは、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('星座を入力してください。')  # エラーメッセージを表示

important random
#

# 補足メッセージ
st.caption("十字キー（左右）でも調整できます。")

# 選択した数字を表示
st.write(f'あなたが選んだ数字は「{number}」です。')

# 選択した数値を2進数に変換
binary_representation = bin(number)[2:]  # 'bin'関数で2進数に変換し、先頭の'0b'を取り除く
st.info(f'🔢 10進数の「{number}」を2進数で表現すると「{binary_representation}」になります。 🔢')  # 2進数の表示をハイライト
# 最小値と最大値の入力を受け取る
min_val = st.number_input('最小値を入力してください', value=0)
max_val = st.number_input('最大値を入力してください', value=10)
# 乱数生成ボタンを配置
if st.botton('乱数を生成'):
    # 最小値と最大値の間で乱数を生成
    random_num = random.randint(min_val, max_val)
    st.write(f'生成された乱数:{random_num}')
