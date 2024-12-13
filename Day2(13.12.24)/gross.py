import streamlit as  st
st.header("Gross salary")
salary=st.number_input('Enter your salary', min_value=0)
hra=0
da=0
if st.button("Gross"):
    if (salary<10000):
        gross = ((67 / 100) * salary)+((73 / 100) * salary)+salary
    elif (salary<20000):
        gross = ((69 / 100) * salary) + ((76 / 100) * salary) + salary
    else :
        gross = ((73 / 100) * salary) + ((81/ 100) * salary) + salary
    st.info(f'gross salary {gross}')