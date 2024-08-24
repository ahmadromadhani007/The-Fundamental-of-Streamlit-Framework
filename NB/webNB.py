import pickle 
import streamlit as st 

# Membaca file bayes_pickle
with open('bayes_pickle', 'rb') as r:
    hasil = pickle.load(r)
    
# Menambahkan pilihan menu
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)

# Menampilkan konten sesuai dengan pilihan
if choice == 'Halaman Utama':
    st.title('Aplikasi Web Machine Learning')
    
    def welcome():  
        return 'Welcome you all'
  
    def prediction1(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):    
        prediction = hasil.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])  
        print(prediction)  
        return prediction
  
    def main():  
        st.title("Algoritma Naive Bayes")
        
        # Membuat dua kolom untuk input
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=0, max_value=100, step=1)  
            sex = st.number_input("Sex", min_value=0, max_value=1, step=1)  
            cp = st.number_input("Chest Pain Type (cp)", min_value=0, max_value=3, step=1)  
            trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=0, max_value=200, step=1)
            chol = st.number_input("Serum Cholestoral (chol)", min_value=0, max_value=300, step=1)
            fbs = st.number_input("Fasting Blood Sugar (fbs)", min_value=0, max_value=1, step=1)
        with col2:
            restecg = st.number_input("Resting Electrocardiographic Results (restecg)", min_value=0, max_value=2, step=1)  
            thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0, max_value=200, step=1)  
            exang = st.number_input("Exercise Induced Angina (exang)", min_value=0, max_value=1, step=1)  
            oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", step=0.1)    
            slope = st.number_input("Slope of the Peak Exercise ST Segment (slope)", min_value=0, max_value=2, step=1)
            ca = st.number_input("Number of Major Vessels (ca)", min_value=0, max_value=4, step=1) 
            thal = st.number_input("Thalassemia (thal)", min_value=0, max_value=3, step=1)
        
        result = ""
        
        if st.button("Predict"):  
            result = prediction1(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
            if result[0] == 0:
                result = 'Tidak Punya Penyakit Jantung'
            elif result[0] == 1:
                result = 'Punya Penyakit Jantung'
        
        st.success('Hasil Prediksinya adalah {}'.format(result))
        st.write("Hasil Prediksinya adalah", result)         
    
    if __name__ == '__main__':  
        main()  

elif choice == 'Tentang Kami':
    st.title('Tentang Kami')
    st.write('Buku ini dibuat untuk belajar aplikasi Streamlit.')
    st.write('Kami sangat senang Anda belajar machine learning dengan Streamlit.')

elif choice == 'Kontak':
    st.title('Kontak')
    st.write('Kalian bisa menghubungi kami di @Ahmadromadhanny.')