# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:23:04 2024

@author: Paul
"""

import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title('Titulo del proyecto de Ciencia')
st.write('Hola **como** estás')

#num=st.slider('Barra de numeros',value=(datetime(2020,1,1,9,30),datetime(2021,1,1,9,30)), format="DD/MM/YY-hh:mm")
#st.write('La fecha ingresada es: {}'.format(num))

d=st.date_input("Fecha de cumpleanos",
                datetime.date(2019,7,6))
st.write('Tu cumpleanos es:',d)

option=st.selectbox('Como quisieras ser contactado?',
                    ('Email','Whastssap','Twiter'))
st.write('Selecciono {}'.format(option))

n=st.slider("n",5,100,step=1)
chart_data=pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

df=pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[37.76,-122.4],
    columns=['lat','lon'])

st.map(df)