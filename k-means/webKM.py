import pickle 
import streamlit as st

# Memuat model dari file pickle
with open('KM_pickle', 'rb') as r:
    classifier1 = pickle.load(r)

# Menambahkan pilihan menu
menu = ['Halaman Utama', 'Tentang Kami', 'Kontak']
choice = st.sidebar.selectbox('Navigasi', menu)

# Menampilkan konten sesuai dengan pilihan tab
if choice == 'Halaman Utama':
    st.title('Halaman Utama')

    def welcome():  
        return 'Welcome you all'   
        
    def prediction1(longitude, latitude):    
        prediction = classifier1.predict([[longitude, latitude]])  
        print(prediction)  
        return prediction   
        
    def main():  
        st.title('Aplikasi Web Machine Learning')  
        st.subheader("Klaster Rumah") 
        
        longitude = st.text_input("Longitude", "")  
        latitude = st.text_input("Latitude", "")   
       
        result = ""  
        if st.button("Predict"):  
            result = prediction1(longitude, latitude)
            if result[0] == 0:
                result = 'Cukup Tinggi'
            elif result[0] == 1:
                result = 'Cukup Tinggi'
            elif result[0] == 2:
                result = 'Lebih Rendah'
                
        st.success('Masuk ke Klaster Rumah: {}'.format(result))
        st.write("Masuk ke Klaster Rumah:", result)
    
    if __name__ == '__main__':  
        main()

elif choice == 'Tentang Kami':
    st.title('Tentang Kami')
    st.write('Buku ini dibuat untuk belajar aplikasi Streamlit.')
    st.write('Kami sangat senang Anda belajar machine learning dengan Streamlit.')

elif choice == 'Kontak':
    st.title('Kontak')
    st.write('Bisa menghubungi kami di @Ahmadromadhanny.')