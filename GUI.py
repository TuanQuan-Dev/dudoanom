
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
from streamlit_option_menu import option_menu
from data import MyData
from homepage import load_homepage

import warnings
warnings.filterwarnings("ignore")

#streamlit run gui.py

# Dữ liệu 
myData = MyData()


st.title("DỰ ÁN - PHÂN NHÓM KHÁCH HÀNG")
st.write("<br/>", unsafe_allow_html=True)

menu = ["Home", "Khám Phá Dữ Liệu", "Collaborative", ["1", "2"]]


with st.sidebar:
    choice = option_menu("",options=menu, 
        icons=["home", "gear", "gear", "file"], menu_icon="cast", default_index=0)


#----------------------------------------------------------------------------------
def CSS():
    st.markdown("""<style>
                    .item {border: solid 1px; height:350px; margin-bottom:10px; font-size:1em; padding:3px}
                    .title {font-weight: bold; font-size:1.3em;}
                    .review {font-weight: bold;}
                    .star {font-weight: bold;}
                    .level {font-weight: bold;}
                </style>""", unsafe_allow_html=True)
           

#----------------------------------------------------------------------------------
def DNA():
    st.header("KHAI THÁC DỮ LIỆU") 
       

    st.write(f"""
        <div style="font-size:1.1em">
         <ol>
            <li style="font-size:1.3em; font-weight:bold">Tổng quan dữ liệu:
                <ul>
                    <span>Thời gian phân tích từ ngày <b>01/01/2014</b> đến <b>30/12/2015</b> </span><br/>
                    <span>Tổng sản phẩm: <b>{myData.Product.shape[0]}</b></span>, tất cả các sản phẩm đều có giao dịch <br/>
                    <span>Tổng số khách hàng có mua hàng: <b>{myData.Transaction["member_number"].nunique()}</b></span>
                    <span>Tổng số khách hàng có mua hàng: <b>{myData.Transaction["member_number"].nunique()}</b></span>
                </ul>
            </li> 
            <li style="font-size:1.3em; font-weight:bold">Tổng quan dữ liệu:
                <ul>
                    Tổng sản phẩm: <b>{myData.Product.shape[0]}</b>         
                    Tổng sản phẩm: <b>{myData.Product.shape[0]}</b>
                </ul>
            </li>
        </ol>
        </div> 
        """         
         , unsafe_allow_html=True)       
    
        
               
#----------------------------------------------------------------------------------
def Collaborative():
    st.header("COLLABORATIVE FILTERING")       
    pass
        
#----------------------------------------------------------------------------------

CSS()
if choice == "Home":
    load_homepage()
    pass
    
elif choice.lower() == "khám phá dữ liệu":
    
    DNA()
    st.write("quan")

elif choice.lower() == "collaborative":
    Collaborative()
    #optUser = st.selectbox("**Please select user:**", mysurprise.user())    

elif choice.lower() == "read-me":
    st.header("VỀ ỨNG DỤNG RECOMMENDER SYSTEMS")
    
    st.write("""
            <div style="font-size:1.2em">
                Hệ thống được chia làm 2 phần:<br/>
                <ol>
                    <li><b>Người dùng chưa có tài khoản (Content-based filtering)</b>
                        <div style="font-size:1.1em">
                            <ul>
                                <li>
                                    Khi người sử dụng không nhập gì vào ô tìm kiếm, hệ thống tự gợi ý 6 khóa học cho học viên
                                </li>
                                <li>
                                    Nếu nhập vào ô tìm kiếm, hệ thống sẽ gợi ý các khóa học liên quan tới từ gợi ý trên. 
                                    Như tên khóa học, đơn vị đào tạo, trình độ, kết quả khóa học
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li><b>Người dùng đã có tài khoản (Collaborative filtering)</b>
                        <div style="font-size:1.1em">
                            Hệ thống dựa vào lịch sử đánh giá của học viên về các khóa đã học để đề xuất cho học viên các khóa học phù hợp                                                            
                        </div>
                    </li>
                    <li><b>Các thành viên trong nhóm</b>
                        <ul>
                            <li>Thái Tuấn Quân</li>
                            <li>Lê Thị Hương Quỳnh</li>
                            <li>Huỳnh Chí Tài</li>
                        </ul>
                    </li>
                </ol>
            </div> 
            """, unsafe_allow_html=True)
    


