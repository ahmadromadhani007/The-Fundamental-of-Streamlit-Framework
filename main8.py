import streamlit as st
import pandas as pd
import numpy as np
import time

# Menampilkan layouts dan countainer
pilih = st.sidebar.selectbox(
    "Pilihlah algoritma yang ingin digunakan !", ("NB", "K-NN", "SVM")
)
with st.sidebar:
    pilih_radio = st.radio(
        "Pilihlah type data", ("Numerik", "Kategorik")
    )

# Perintah st.column
col1, col2 = st.columns(2)
with col1:
    chart_data = pd.DataFrame(
        np.random.randn(5, 3),
        columns=['Kolom1', 'Kolom2', 'Kolom3']
    )
    st.table(chart_data)
with col2:
    chart_data = pd.DataFrame(
        np.random.randn(5, 3),
        columns=['Kolom1', 'Kolom2', 'Kolom3']
    )
    st.area_chart(chart_data)

# perintah st.tab()
tab1, tab2 = st.tabs(['Chart', 'Data'])
data = np.random.randn(10, 1)
tab1.subheader("Contoh tab dengan grafik")
tab1.line_chart(data)
tab2.subheader("Contoh tab dengan data")
tab2.write(data)

# perintah st.expander with
with st.expander("Klik untuk melihat Expander"):
    st.write('Ini adalah contoh expander')
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
# perintah st.expander object
klik = st.expander("Klik untuk melihat Expander")
klik.write('Ini adalah contoh expander')
klik.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

# perintah st.container with
with st.container():
    st.write('Ini dalam container')
st.write('Ini diluar container')
# perintah st.container object
klik = st.container()
klik.write('Ini adalah contoh container')
klik.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

#perintah st.empty menggunakan with
with st.empty():
    for seconds in range(10):
        st.write(f" {seconds} detik akan selesai")
        time.sleep(1)
        st.write("10 detik sudah selesai")
#perintah st.empty menggunakan object
klik = st.empty()
for detik in range(10):
        klik.write(f" {detik} detik akan selesai")
        time.sleep(1)
        klik.write("10 detik sudah selesai")