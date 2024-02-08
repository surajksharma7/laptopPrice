import streamlit as st

st.header(":mailbox: Get In Touch With Me")


contact_form = """
<form action="https://formsubmit.co/surajksharma2304@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Enter Your Name" required>
    <input type="email" name="email" placeholder="Enter Email Address" required>
    <textarea name="message" placeholder="Enter Your Message"></textarea>
    <button type="submit">Send</button>
</form>

"""

st.markdown(contact_form,unsafe_allow_html = True)

