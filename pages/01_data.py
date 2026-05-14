import streamlit as st
import pandas as pd
import numpy as np


st.title('데이터프레임 튜토리얼')

# DataFrame 생성
dataframe = pd.DataFrame({
    '이름': ['이정민', '정준우', '박채윤', '장서윤'],
    '수학': [75, 57, 83, 55],
    '영어': [23, 76, 18, 27]
})

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
st.dataframe(dataframe, use_container_width=True)


# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(dataframe)


# # 메트릭
st.metric(label="온도", value="10°C", delta="1.2°C")
st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")
col4.metric(label="정민이 성적", value="100점", delta="50점")