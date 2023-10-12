import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Exploratory Data Analysis')

import streamlit as st
import pandas as pd

# Buat aplikasi Streamlit
st.markdown('Aplikasi Data Streamlit')

# Buat input data
uploaded_file = st.file_uploader("Unggah File CSV", type=["csv"])

# Tampilkan 5 data teratas jika data sudah diunggah
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    if st.button('Pratinjau Data'):
        st.write("5 Data Teratas")
        st.write(data.head(5))
        st.write("Informasi Data")
        st.write(data.describe())
else:
    st.write("Silakan unggah file CSV untuk melanjutkan.")

# menapilkan nama kolom
if st.checkbox("Tampilkan Nama Kolom"):
    st.write(data.columns)

# Melihat Dimensi Data
data_dim = st.radio('Jumlah data mana yang ingin dilihat?', {'Baris', 'Kolom', 'Semua'})
if data_dim == 'Baris' :
    st.text('menampilkan Jumlah Baris')
    st.write(data.shape[0])
elif data_dim == 'Kolom' :
    st.text('Menampilkan Jumlah Kolom')
    st.write(data.shape[1])
else:
    st.text('Menampilkan Jumlah Baris dan Kolom')
    st.write(data.shape)

# memilih kolom barti ambil dr data.columns
st_tags(label='#pilih')

keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=(data.columns),
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags = 4,
    key='1'
)