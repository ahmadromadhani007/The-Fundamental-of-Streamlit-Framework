# Import library yang digunakan
import pickle
import streamlit as st

# Membaca file svm_pickle
with open('svm_pickle', 'rb') as r:
    model = pickle.load(r)

# Menambahkan pilihan
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)

# Menampilkan konten sesuai dengan pilihan
if choice == 'Halaman Utama':
    st.title('Halaman Utama')

    def welcome():
        return 'Welcome you all'
    
    def prediction1(x1, x2, x3, x4, x5, x6, x7,
                    x8, x9, x10 ,x11, x12, x13,
                    x14, x15, x16, x17, x18, x19, 
                    x20, x21, x22 ,x23, x24, x25, 
                    x26, x27, x28, x29, x30):
        prediction1 = model.predict([[x1, x2, x3, x4, x5, x6, x7,
                    x8, x9, x10 ,x11, x12, x13,
                    x14, x15, x16, x17, x18, x19, 
                    x20, x21, x22 ,x23, x24, x25, 
                    x26, x27, x28, x29, x30]])
        print(prediction1)
        return prediction1
    
    def main():
        st.title('Aplikasi Web Machine Learning')
        st.title('Prediksi Kanker Payudara')
        st.title('Menggunakan Algoritma Support Vector Machine')
        col1, col2, col3 = st.columns(3)
        with col1:
            x1 = st.text_input ("mean radius ", "")  
            x2 = st.text_input ("mean texture ", "")  
            x3 = st.text_input ("mean perimeter ", "")  
            x4 = st.text_input ("mean area ", "") 
            x5 = st.text_input ("mean smoothness ", "")  
            x6 = st.text_input ("mean compactness ", "")  
            x7 = st.text_input ("mean concavity ", "")  
            x8 = st.text_input ("mean concave points ","")
            x9 = st.text_input ("mean symmetry ", "")  
            x10 = st.text_input ("mean fractal dimension", "")
        with col2:  
            x11 = st.text_input ("radius error ", "")  
            x12 = st.text_input ("texture error ", "")
            x13 = st.text_input ("perimeter error ", "")
            x14 = st.text_input ("area error ", "")
            x15 = st.text_input ("smoothness error ", "")
            x16 = st.text_input ("compactness error ", "")
            x17 = st.text_input ("concavity error ", "")
            x18 = st.text_input ("concave points error ", "")
            x19 = st.text_input ("symmetry error ", "")
            x20 = st.text_input ("fractal dimension error", "")
        with col3:
            x21 = st.text_input ("worst radius", "")
            x22 = st.text_input ("worst texture", "")
            x23 = st.text_input ("worst perimeter", "") 
            x24 = st.text_input ("worst area", "")
            x25 = st.text_input ("wworst smoothness", "") 
            x26 = st.text_input ("worst compactness", "")
            x27 = st.text_input ("worst concavity", "")
            x28 = st.text_input ("worst concave points", "")
            x29 = st.text_input ("worst symmetry", "")
            x30 = st.text_input ("worst fractaldimension", "")
        hasil = " "
        if st.button ("Predict"):  
            hasil = prediction1 (x1, x2, x3, x4, x5,
x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16,
x17, x18, x19, x20, x21, x22, x23, x24, x25, x26,
x27, x28, x29, x30)
            
        st.success ('Hasil Prediksinya adalah{}'.format(hasil))
        st.write("Jika hasil prediksinya adalah 'M' kanker (malignant/ganas), jika hasil prediksinya 'B' yang menunjukkan kanker (benign/jinak).! ",
format(hasil))
    if __name__== '__main__':  
        main()
elif choice == 'Tentang Kami':
    st.title('Tentang Kami')
    st.write('Buku ini dibuat untuk belajar aplikasi Streamlit')
    st.write('Kami sangat senang anda belajar machine learning dengan streamlit.')
elif choice == 'Kontak':
    st.title('Kontak')
    st.write('Kalian Bisa DM IG @Ahmadromadhanny')