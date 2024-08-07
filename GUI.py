import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

import warnings
warnings.filterwarnings("ignore")

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(0, 65, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.plot()
    plt.title("Tính om theo nhiệt độ")
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.yaxis.set(ticks=np.arange(0, 34, 2), label_text='Nhiet do')
    #fig = plt.gcf()
    plt.xlabel(Name)    

    st.pyplot(plt)
#####################################################

# Dữ liệu 

st.title("DỰ ĐOÁN kom")
st.write("<br/>", unsafe_allow_html=True)

st.header("Dữ liệu gốc:")

X = np.array([0, 10, 20, 30, 40, 50, 60]) 
y = np.array([32, 20, 12.5, 8, 4.8, 3, 2])

f = np.polyfit(X, y, 4)
p = np.poly1d(f)
PlotPolly(p, X, y, "om")

text = st.number_input("Vui lòng nhập nhiệt độ:")
y = round(p(text), 1)

st.write(f"Kết quả: <b>{y}</b>", unsafe_allow_html=True)