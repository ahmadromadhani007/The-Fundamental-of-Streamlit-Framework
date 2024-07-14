import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -12],
    columns=['lat', 'lon'])
st.map(df)
st.divider()

# Create the button
if st.button('Klik disini'):
    st.write('Selamat belajar button')
else:
    st.write('Dibawah ini adalah kolom ceklis dari data_editor')
# Create the DataFrame st.data_editor
df = pd.DataFrame(
    [ 
        {"Command": "st.selectbox", "rating": 4, "is_widget": True},
        {"Command": "st.balloons", "rating": 5, "is_widget": False},
        {"Command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
# Display the DataFrame using Streamlit's experimental data editor
tampil = st.data_editor(df, num_rows="dynamic", use_container_width=True)

# Create the button download
@st.cache_data
def convert_df(df):
    #convert dataframe to csv
    return df.to_csv().encode('utf-8')
#membuat contoh data frame yang akan di download
df = pd.DataFrame(np.random.randn(800, 2))
csv = convert_df(df)
# Mengatur layout dengan kolom agar berada di kanan
col1, col2, col3 = st.columns([1, 1, 1])
# Menampilkan tombol download di kolom ketiga
with col3:
    st.download_button(
        label="Download data",
        data=csv,
        file_name="data.csv",
        mime="text/csv",
)

#membuat perintah checkBox
st.checkbox('Ini adalah checkbox')
st.radio("Option", ('Pria', 'Wanita'))
st.selectbox("Menu", ('Ayam', 'Ikan Asap', 'Siongan Jumbo'))

# Membuat perintah multiSelect
options = st.multiselect(
    'Hobi kamu apa?', 
    ['Badminton', 'Bola Sepak', 'Volley']
)

st.write('Kamu memilih:', options)

# Membuat perintah slider untuk tinggi
tinggi = st.slider('Berapa tinggi Anda?', 0, 175, 145)
st.write('Tinggi saya:', tinggi, 'cm')

# Membuat perintah slider untuk nilai interval 0-1
nilai = st.slider('Pilih interval 0-1', min_value=0.0, max_value=1.0, value=0.5)
st.write('Nilai interval yang dipilih adalah:', nilai)