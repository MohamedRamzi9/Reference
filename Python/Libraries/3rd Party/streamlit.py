import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time

st.set_page_config(page_title="Streamlit Widget Demo", layout="wide")

st.title("🎛️ Streamlit Full Widget Demo App")
st.write("This app demonstrates every major Streamlit widget.")

# ---------------------------
#   LAYOUT
# ---------------------------
tab_inputs, tab_selectors, tab_buttons, tab_chat, tab_display, tab_data, tab_layout, tab_media = st.tabs([
    "Inputs", "Selectors", "Buttons", "Chat", "Display", "Data", "Layout", "Media"
])

# -----------------------------------------------------
#   INPUTS TAB
# -----------------------------------------------------
with tab_inputs:
    st.header("🟦 Input Widgets")

    text_val = st.text_input("Text Input:", "Hello")
    area_val = st.text_area("Text Area:", "Write something...")
    num_val = st.number_input("Number Input:", 0, 100, 42)
    date_val = st.date_input("Date Input:", date.today())
    time_val = st.time_input("Time Input:", time(12, 0))
    file_val = st.file_uploader("File Uploader:")
    color_val = st.color_picker("Color Picker:", "#00ff00")
    img_val = st.camera_input("Camera Input (take a picture):")

    st.write("### Output:")
    st.write({
        "text": text_val,
        "textarea": area_val,
        "number": num_val,
        "date": date_val,
        "time": time_val,
        "color": color_val,
        "file_uploaded": file_val.name if file_val else None,
        "image_taken": img_val is not None
    })

# -----------------------------------------------------
#   SELECTORS TAB
# -----------------------------------------------------
with tab_selectors:
    st.header("🟩 Selector Widgets")

    select_val = st.selectbox("Selectbox:", ["A", "B", "C"])
    multi_val = st.multiselect("Multiselect:", ["A", "B", "C", "D"])
    radio_val = st.radio("Radio:", ["Option 1", "Option 2", "Option 3"])
    check_val = st.checkbox("Checkbox")
    slider_val = st.slider("Slider:", 0, 100, 50)
    range_val = st.slider("Range Slider:", 0, 100, (20, 80))

    st.write("### Output:")
    st.write({
        "select": select_val,
        "multiselect": multi_val,
        "radio": radio_val,
        "checkbox": check_val,
        "slider": slider_val,
        "range_slider": range_val
    })

# -----------------------------------------------------
#   BUTTONS TAB
# -----------------------------------------------------
with tab_buttons:
    st.header("🟨 Buttons & Forms")

    if st.button("Simple Button"):
        st.success("Button clicked!")

    with st.form("my_form"):
        name = st.text_input("Name in Form:")
        submitted = st.form_submit_button("Submit Form")

    if submitted:
        st.info(f"Form submitted: {name}")

    st.download_button("Download file", "Hello world!", "hello.txt")

# -----------------------------------------------------
#   CHAT TAB
# -----------------------------------------------------
with tab_chat:
    st.header("💬 Chat Widgets")

    msg = st.chat_input("Say something:")
    if msg:
        st.chat_message("user").write(msg)
        st.chat_message("assistant").write(f"Echo: {msg}")

# -----------------------------------------------------
#   DISPLAY TAB
# -----------------------------------------------------
with tab_display:
    st.header("📢 Display Elements")

    st.success("Success message!")
    st.error("Error message")
    st.warning("Warning")
    st.info("Information message")
    st.exception(Exception("This is an exception"))

    st.markdown("### Markdown Example")
    st.markdown("**Bold**, *italic*, `code`")

    st.code("print('hello world')")

    st.metric("Temperature", "30°C", "+2°C")

    st.progress(40)

    with st.spinner("Loading..."):
        pass

# -----------------------------------------------------
#   DATA TAB
# -----------------------------------------------------
with tab_data:
    st.header("📊 Data Widgets")

    df = pd.DataFrame({
        "A": np.random.randn(10),
        "B": np.random.randn(10),
        "C": np.random.randn(10),
    })

    st.write("### DataFrame:")
    st.dataframe(df)

    st.write("### Table:")
    st.table(df.head())

    st.write("### JSON:")
    st.json({"name": "Streamlit", "version": 1})

    st.write("### Charts:")
    st.line_chart(df)
    st.bar_chart(df)

# -----------------------------------------------------
#   LAYOUT TAB
# -----------------------------------------------------
with tab_layout:
    st.header("📐 Layout Widgets")

    st.subheader("Sidebar")
    st.sidebar.write("This is the sidebar!")
    st.sidebar.selectbox("Sidebar Selectbox", [1, 2, 3])

    st.subheader("Columns")
    col1, col2 = st.columns(2)
    col1.write("Left column")
    col2.write("Right column")

    st.subheader("Expander")
    with st.expander("Open Me"):
        st.write("Hidden content")

    st.subheader("Container")
    container = st.container()
    container.write("Inside container")

    st.subheader("Placeholder")
    placeholder = st.empty()
    placeholder.write("This will update in 2 seconds...")

    import time
    time.sleep(2)
    placeholder.write("Updated!")

# -----------------------------------------------------
#   MEDIA TAB
# -----------------------------------------------------
with tab_media:
    st.header("📷 Media Widgets")

    st.image("https://placekitten.com/300/200", caption="Random Cat")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav")

st.write("---")
st.write("Made with ❤️ using Streamlit")
