#perintah st.altair
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c'. tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)