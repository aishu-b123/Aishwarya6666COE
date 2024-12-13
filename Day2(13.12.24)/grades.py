import streamlit as st
st.header("Grades of a student")
project=st.number_input('project score',min_value=0)
internal=st.number_input('internal score',min_value=0)
external=st.number_input('external score',min_value=0)

if st.button("total "):
    if (project>=50 and internal >=50 and external >=50):
        total = ((70 / project ) * 100) + ((10 / internal ) * 100) +((20 / external ) * 100)
        st.info(total)
        if total>=90:
            st.write(' Grade A')
        elif total>80:
            st.write('Grade B')
        else:
            st.write('Grade C')
    else:
        if project<50:
            st.write('failed in project' , project)
        if external<50:
            st.write('failed in external' , external)
        if internal<50:
            st.write('failed in internal' , internal)