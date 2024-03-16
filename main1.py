#Sintaxs dalam streamlit
import streamlit as st
import pandas as pd

st.title('FUNDAMENTAL STREAMLIT FRAMEWORK FOR BASIC MACHINE LEARNING')
st.header('Sebuah Header dengan _italics_ :blue[colors] dan jangan lupa full senyum Xixixi :sunglasses:')
st.divider()
st.subheader('Sebuah Sub header dengan _italics_ :blue[colors] dan jangan lupa full senyum Xixixi :sunglasses:')
st.caption('Caption todyas is :red[Menyala Abangkuh]')
st.text('Text todyas is Ilmu Kapas Abangkuh')
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.write(1234567)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4, 5],
    'second column': [10, 20, 30, 40, 50],
}))
code = '''def hello():
    print ("Hello, Streamlit!")'''
st.code(code, language='python')
st.code('x=2024')
st.markdown('Teks ini berwarna merah :red[merah], dan ini **:blue[biru]** and bold.')
st.markdown(':green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:')