import streamlit as st

# Menampilkan control flow dengan st.stop
st.title("Aplikasi Streamlit")
if st.button("Stop Aplikasi"):
    st.warning("Aplikasi dihentikan!")
    st.stop()
st.write("Baris ini tidak di eksekusi jika aplikasi dihentikan.")

# Menampilkan control flow dengan st.form
with st.form("Formulir Pengguna"):
    nama = st.text_input("Nama")
    umur = st.number_input("Umur", min_value=0, max_value=100, step=1)
    alamat = st.text_area("Alamat")
    submit_button = st.form_submit_button(label="Submite")
if submit_button:
    st.write("Nama:", nama)
    st.write("Umur:", umur)
    st.write("Alamat:", alamat)

# Menampilkan control flow dengan st.form_submit_button
st.title("Aplikasi Dasar Streamlit Formulir")
with st.form("Formulir Data Mahasiswa"):
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama")
        umur = st.number_input("Umur", min_value=0, max_value=100, step=1)
        alamat = st.text_area("Alamat")
        jurusan = st.selectbox("Program Studi", ["IF", "TI", "SI", "TE", "RPL"])
    with col2:
        hobi = st.multiselect("Hobi", ["Membaca", "Menulis", "Olahraga", "Memasak", "Mengaji"])
        uts = st.number_input("UTS", min_value=0, max_value=100, step=1)
        uas = st.number_input("UAS", min_value=0, max_value=100, step=1)
        tugas = st.number_input("Tugas", min_value=0, max_value=100, step=1)
        na =  (uts+uas+tugas)/3
    submit_button = st.form_submit_button(label="Submite")
if submit_button:
    st.write("Data Mahasiswa:")
    st.write("Nama:", nama)
    st.write("Umur:", umur)
    st.write("Alamat:", alamat)
    st.write("Jurusan:", jurusan)
    st.write("Hobi:", hobi)
    st.write("Nilai Akhir:", na)

# Menampilkan control flow dengan st.experimental_return
st.title("Aplikasi Dasar Streamlit")
nama = st.text_input("Nama")
umur = st.number_input("Umur", min_value=0, max_value=100, step=1)
rerun_button = st.button("Rerun")
if rerun_button:
    st.rerun()
st.write("Nama:", nama)
st.write("Umur:", umur)