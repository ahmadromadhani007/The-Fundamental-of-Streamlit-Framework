#2.4 Menampilkan Grafik a. perintah st.line()
import streamlit as st
import pandas as pd
import numpy as np
chart_data = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['kolom1', 'kolom2', 'kolom3'])
st.table(chart_data)
st.line_chart(chart_data)
#perintah st.area
st.area_chart(chart_data)
#perintah st.bar
st.bar_chart(chart_data)
#perintah st.area
st.area_chart(chart_data)