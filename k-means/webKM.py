import pickle
import streamlit as st  

# Membaca file svm_pickle
with open('RF_pickle', 'rb') as r:
    classifier1 = pickle.load(r)

# Menambahkan pilihan
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)

# Menampilkan konten sesuai dengan pilihan
if choice == 'Halaman Utama':
    st.title('Halaman Utama')   
    
    def welcome():  
        return 'Welcome you all'  
        
    def prediction1(sepal_length1, sepal_width1, petal_length1, petal_width1):    
        prediction1 = classifier1.predict([[sepal_length1, sepal_width1, petal_length1, petal_width1]])  
        return prediction1   
    
    def main():  
        st.title('Aplikasi Web Machine Learning')  
        st.subheader("Prediksi Bunga Iris") 
        sepal_length1 = st.text_input("Sepal Length", "")  
        sepal_width1 = st.text_input("Sepal Width", "")  
        petal_length1 = st.text_input("Petal Length", "")  
        petal_width1 = st.text_input("Petal Width", "")  
        result = ""  
            
        if st.button("Predict"):  
            result = prediction1(sepal_length1, sepal_width1, petal_length1, petal_width1)
            if result[0] == 1:
                result = 'Bunga iris Setosa'
            elif result[0] == 2:
                result = 'Iris-versicolor'
            elif result[0] == 3:
                result = 'Iris-virginica'
                
        st.success('Hasil Prediksinya adalah {}'.format(result))

    if __name__ == '__main__':  
        main()

elif choice == 'Tentang Kami':
    st.title('Tentang Kami')
    st.write('Buku ini dibuat untuk belajar aplikasi Streamlit.')
    st.write('Kami sangat senang Anda belajar machine learning dengan Streamlit.')

elif choice == 'Kontak':
    st.title('Kontak')
    st.write('Kalian bisa menghubungi kami di @Ahmadromadhanny.')
