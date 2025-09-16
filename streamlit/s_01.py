# pip install streamlit - 터미널에서 실행
import streamlit as st
st.title('타이틀')
st.header('헤더')
st.subheader('서브헤더')
st.button('버튼')
st.checkbox('체크박스')
st.radio('라디오박스', ('a', 'b', 'c'))
st.selectbox('셀렉트 박스', ('1번', '2번'))
st.slider('슬라이더', 0, 100, 50) # 최소 최대 기본값
st.text_input('텍스트 상자')

# streamlit run ./streamlit/s_01.py  --> 2주차 블로그에 적기
