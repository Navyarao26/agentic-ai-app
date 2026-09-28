import streamlit as st
t1,t2=st.tabs(["login form","Reg Form"])
with t1:
    st.title("login Form")
    with st.form("login form"):
        st.text_input("Email", placeholder="Enter your email")
        st.text_input("Password", placeholder="Enter your password", type="password")
        st.text_input("Re-enter Password", placeholder="Re-enter the password", type="password")
with t2:
    st.title("Registration Form")
    with st.form("Reg form"):
        st.text_input("Name", placeholder="Enter your name")
        st.text_input("Email", placeholder="Enter your email")
        st.text_input("Password", placeholder="Enter your password", type="password")
        st.text_input("Re-enter Password", placeholder="Re-enter the password", type="password")
        st.selectbox("Role",[" ","trainer","Student"])
        st.form_submit_button("Register")
