import streamlit as st

# 페이지 등록
main_p = st.Page("00-text.py", title="홈")
data_p = st.Page("01-data.py", title="데이터")

pg = st.navigation([main_p, data_p], position="hidden")
pg.run()

# 메인 페이지의 내용
st.title("여기는 메인 페이지입니다")
if st.button("데이터 페이지로 이동"):
    st.switch_page(data_p) # 또는 "01_data.py"