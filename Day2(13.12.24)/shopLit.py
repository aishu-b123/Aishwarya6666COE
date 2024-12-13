import streamlit as st
salary=st.number_input('enter the salary',step=1)
s1=st.number_input('enter the shopping1 cost',step=1)
s2=st.number_input('enter the shopping2 cost',step=1)
#total_s=s1+s2
if st.button('calculate shopping amount percentage'):
    total_s = s1 + s2
    per=(total_s/salary)*100
    st.write("salary: ",salary)
    st.write("total shopping cost: ",total_s)
    st.write("percentage: ", per)