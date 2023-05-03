import pickle
import streamlit as st  

# load save model
model = pickle.load(open('estimasi_real_estate.sav', 'rb'))

#judulweb
st.title('Estimasi Harga Real Estate Rumah')

trasaction_data = st.number_input ('Data transaksi')
house_age = st.number_input ('Usia rumah')
distance_to_the_nearest_MRT_station = st.number_input ('jarak ke stasiun MRT terdekat')
number_of_convenience_stores = st.number_input ('jumlah toko')
latituted = st.number_input ('Garis lintang area')    
longitude = st.number_input ('Garis bujur area')

#code untuk prediksi
predict = ''

#membuat tombol untuk prediksi
if st.button('Estimasi Harga'):
    predict = model.predict(
        [[trasaction_data, house_age, distance_to_the_nearest_MRT_station, number_of_convenience_stores, latituted, longitude]]
        )
st.write ('Estimasi Harga Real Estate Rumah :', predict)