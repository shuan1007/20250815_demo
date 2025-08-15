import numpy as np
import pandas as pd
import streamlit as st

st.title("demo page")
st.write("123")
st.write("## 123")
st.write("### 123")

# df2= st.dataframe(np.random.randn(10, 5))

df1 = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
st.write(df1)
# st.write(df2)

st.write("## 核取方塊")
r1 = st.checkbox("外帶")
if r1:
        st.write("外帶")
else:
        st.write("內用")

checks = st.columns(3)
txt = ''
with checks[0]:
        r2 = st.checkbox("set A")
        if r2:
                txt += ' A '
with checks[1]:
        r3 = st.checkbox("set B")
        if r3:
                txt += ' B '
st.info(txt)

st.write("## 選項按鈕")
b1 = st.radio("飲料:",("咖啡","紅茶","綠茶"))
st.info(b1)

b2 = st.radio("飲料:",("咖啡","紅茶","綠茶"),key="b2")
st.info(b2)

st.write("## 滑桿")
num = st.slider("請選擇數量:",1.0,5.0,3.0,0.5)
st.info(num)

st.write("## 下拉選單")
city = st.selectbox("請選擇:", ("北", "中", "南"))
if city == "北":
        st.info("A")
elif city == "中":
        st.info("B")
else:
        st.info("C")

st.write("## 下拉選單")
city = st.sidebar.selectbox("請選擇:", ("北", "中", "南"))
if city == "北":
        st.sidebar.info("A")
elif city == "中":
        st.sidebar.info("B")
else:
        st.sidebar.info("C")

st.write("## 按鈕")
a = st.number_input("num...")
b = st.number_input("num...", 1, 10, 5)
if st.button("計算"):
        st.info(a+b)
