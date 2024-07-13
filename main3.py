#c. file metric.py()
import streamlit as st
st.metric(label="Temperature", value="70 oF", delta="1.2 oF")
st.caption('dibawah ini kombinasi coding st.metric() dengan st.column()')
st.divider()
kolom1, kolom2, kolom3 = st.columns(3)
kolom1.metric("Temperature", "70 oF", "1.2 oF")
kolom2.metric("Wind", "9 mph", "-8%")
kolom3.metric("Humanity", "86%", "4%")
st.divider()
#d. perintah st.json()
st.json({
    'Name' : 'Ayu Nawiroh',
    'Address' : 'Bondowoso',
    'Hobby': [
        'Cooking',
        'Reciting',
        'Memorizing',
    ],
})
