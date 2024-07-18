import pickle 
import streamlit as st  

with open('DT_pickle','rb') as r:
    hasil = pickle.load(r)

# Menambahkan pilihan
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)

# Menampilkan konten sesuai dengan pilihan
if choice == 'Halaman Utama':
    st.title('Halaman Utama')
    
    def welcome():  
        return 'Welcome you all'    
    
    def prediction1(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):    
        prediction1 = hasil.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        print(prediction1)  
        return prediction1[0]  # Get the first element of the prediction array
    
    def main():  
        st.title('Aplikasi Web Machine Learning')  
        st.title("Algoritma Decision Tree ") 
        
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = st.text_input("Pregnancies", "")  
            Glucose = st.text_input("Glucose", "")  
            BloodPressure = st.text_input("BloodPressure", "")  
            SkinThickness = st.text_input("SkinThickness", "")
        with col2:
            Insulin = st.text_input("Insulin", "")  
            BMI = st.text_input("BMI", "")  
            DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction", "")  
            Age = st.text_input("Age", "")    

        result = ""      
        if st.button("Predict"):  
            result = prediction1(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
            st.success('Hasil Prediksinya adalah {}'.format(result))
            st.write("Jika hasil prediksinya adalah (0) maka tidak mengidap diabetes, jika hasilnya (1) maka mengidap diabetes", result)

    if __name__ == '__main__':  
        main()  

elif choice == 'Tentang Kami':
    st.title('Tentang Kami')
    st.write('Buku ini dibuat untuk belajar aplikasi Streamlit')
    st.write('Kami sangat senang anda belajar machine learning dengan streamlit.')

elif choice == 'Kontak':
    st.title('Kontak')
    st.write('Kalian Bisa Menghubungi kami di abu@unuja.ac.id')
