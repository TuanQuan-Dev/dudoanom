import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

import streamlit as st

import warnings
warnings.filterwarnings("ignore")

#streamlit run Cuong.py

# Dữ liệu 


st.title("DỰ ĐOÁN kom")
st.write("<br/>", unsafe_allow_html=True)

st.header("Dữ liệu gốc:")

X = np.array([0, 10, 20, 30, 40, 50, 60]) 
y = np.array([32, 20, 12.5, 8, 4.8, 3, 2])
 
plt.plot(X, y) 
st.pyplot(plt)

X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

model = LinearRegression()
model.fit(X, y)

text = st.number_input("Vui lòng nhập nhiệt độ:")
X_test = np.array([text])
y = model.predict(X_test.reshape(-1, 1))[0][0]

st.write(f"Kết quả: <b>{y}</b>", unsafe_allow_html=True)
