import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import math as m


st.title("WARFARIN CALCULATOR")


st.markdown(
    """
    <style> 
    .stApp {
        background-color: grey;
    }
    </style>

    """, unsafe_allow_html= True
)




try:
    q1 = st.selectbox("Choose option:", ["Dose taken daily", "Dose taken on alternative periods", "2 doses taken a day"])
    if q1 == "Dose taken daily":
        url = "https://tse3.mm.bing.net/th/id/OIP.YgwNWr0RmiFXxNpDurwhowAAAA?rs=1&pid=ImgDetMain&o=7&rm=3"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption = "CONVERSION TABLE")
        final = st.text_input("enter the dose (mg) he/she needs to take?: ").strip()
        final = float(final)
        day = st.text_input("how many times a day? For example: dly = 1, bd = 2, tds = 3, etc: ").strip()
        day = float(day)
        new = st.text_input("for how long will he or she take this medication in days?: ").strip()
        new = float(new)
        true = (final / 5) * day* new
        st.success(f"The patient will take {m.ceil(true)} tablets. Take {final/5} tablet/s {day} times a day for {new} days")


    elif q1 == "Dose taken on alternative periods":
        url = "https://tse3.mm.bing.net/th/id/OIP.YgwNWr0RmiFXxNpDurwhowAAAA?rs=1&pid=ImgDetMain&o=7&rm=3"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption = "CONVERSION TABLE")
        final = st.text_input("enter the dose (mg) the patient needs to take?: ").strip()
        final = float(final)
        day = st.text_input("how many times a day? For example: dly = 1, bd = 2, tds = 3, etc: ").strip()
        day = float(day)
        new = st.text_input("how many times in a week, will the patient have to take their medication? For example, M,W,F = 3 times a week: ").strip()
        new = float(new)
        week = st.text_input("For how many weeks will the patient take the medication?: ")
        week = float(week)
        true = (final / 5) * day* new * week
        st.success(f"The patient will take {m.ceil(true)} tablets. Take {final/5} tablet/s {day} times a day on alternative days as specified")


    elif q1 == "2 doses taken a day":
        url = "https://tse3.mm.bing.net/th/id/OIP.YgwNWr0RmiFXxNpDurwhowAAAA?rs=1&pid=ImgDetMain&o=7&rm=3"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption = "CONVERSION TABLE")
        final = st.text_input("enter the dose (mg) the patient needs to take in the morning?: ").strip()
        final = float(final)
        final2 =  st.text_input("enter the dose (mg) the patient needs to take at night ?: ").strip()
        final2 = float(final2)
        day = st.text_input("how many times a day? For example: dly = 1, bd = 2, tds = 3, etc: ").strip()
        day = float(day)
        question = st.text_input("is the duration for a week/s or in days?: ").strip().lower()
        if question == "weeks" or question == "week":
            week = st.text_input("For how many weeks will the patient take the medication?: ")
            week = float(week) * 7
            true = (final / 5) * day* week
            true2 = (final2 / 5) * day * week
            total = true + true2
            st.success(f"The patient will take {m.ceil(total)} tablets. Take {final/5} tablet/s of {final}mg, {day} times in the morning then take {final2/5} tablet/s of {final2}mg {day} times at night")
        elif question == "days" or question == "day":
            week = st.text_input("For how many days will the patient take the medication?: ")
            week = float(week)
            true = (final / 5) * day* week
            true2 = (final2 / 5) * day * week
            total = true + true2
            st.success(f"The patient will take {m.ceil(total)} tablets. Take {final/5} Tablet of {final}mg, {day} times in the morning then take {final2/5} tablet of {final2}mg {day} times at night")
        else:
            st.error("Must only be week/s or day/s!!")

except ValueError:
    st.write("Oops! Please make sure you're entering only numbers. If it's a decimal, use a dot (.) — and avoid using words or commas.")
