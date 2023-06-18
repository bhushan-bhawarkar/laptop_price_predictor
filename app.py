import pandas as pd
import numpy as np
import streamlit as st
import pickle


pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title('Well Come To My Laptop Price Predictor')

company = st.selectbox('Brand',df['Company'].unique())

TypeName = st.selectbox('TypeName',df['TypeName'].unique())

Ram = st.selectbox('Ram (In GB)',[2,4,6,8,12,16,24,32,64])

Weight = st.number_input('Wight of the laptop')

Touchscreen = st.selectbox('Touchscreen',['Yes','No'])

Ips = st.selectbox('Ips',['Yes','No'])

screen_size = st.number_input('screen_size')

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

Cpu_brand = st.selectbox('Cpu brand',df['Cpu brand'].unique())

hdd = st.selectbox('HDD (In GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    if Touchscreen == 'Yes':
        Touchscreen = 1
    else:
        Touchscreen = 0

    if Ips == 'Yes':
        Ips= 1
    else:
        Ips= 0  
    x =  int(resolution.split('x')[0]) 
    y =  int(resolution.split('x')[1]) 

    ppi = (x**2 + y**2)**0.5/(screen_size + 0.001)

    quary = np.array([company,TypeName,Ram,Weight,Touchscreen,Ips,ppi,Cpu_brand,hdd,ssd,gpu,os])
                      
    quary = quary.reshape(1,12)

    st.markdown("<h2 style='color: red;'>The predicted price of this configuration is</h2>", unsafe_allow_html=True)
    st.title(str(int(round(np.exp(pipe.predict(quary)[0])))))
    st.write("Enjoy your new laptop!")
                





