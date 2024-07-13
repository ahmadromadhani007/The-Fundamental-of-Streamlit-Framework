#2.3 Menampilkan sebuah data
import streamlit as st
import pandas as pd
import numpy as np

#a. perintah DataFrame
st.title('Dataframe Basic')
df = pd.DataFrame(
    np.random.rand(10, 5),
    columns=('col %d' % i for i in range(5)))
st.dataframe(df)
#b. perintah st.table()
st.table(df)


