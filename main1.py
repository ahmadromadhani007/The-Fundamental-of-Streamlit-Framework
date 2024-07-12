#2.1 Dasar streamlit
import streamlit as st
import pandas as pd
# perintah st.title
st.title('FUNDAMENTAL STREAMLIT FRAMEWORK FOR BASIC MACHINE LEARNING')
st.title('By Ahmadromadhanny')
# perintah st.divider garis pemisah horizontal
st.divider()
# perintah st.header
st.header('Sebuah Header dengan _italics_ :blue[colors] dan jangan lupa full senyum Xixixi :sunglasses:')
# perintah st.subheader
st.subheader('Sebuah Sub header dengan _italics_ :blue[colors] dan jangan lupa full senyum Xixixi :sunglasses:')
# perintah st.captions
st.caption('Caption todyas is :red[Menyala Abangkuh]')
# perintah st.text
st.text('Text todyas is Ilmu Kapas Abangkuh')
# perintah st.latex
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
# perintah st.code
code = '''def hello():
    print ("Hello, Streamlit!")'''
st.code(code, language='python')
st.code('x=2024')
#st.write
st.write(1234567)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4, 5],
    'second column': [10, 20, 30, 40, 50],
}))
#2.2 Element Text
st.markdown('Teks ini berwarna merah :red[merah], dan ini **:blue[biru]** and bold.')
st.markdown(':green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:')