
import streamlit as st

import pandas as pd
import numpy as np
from datetime import date, time

# set the page title and layout
st.set_page_config(page_title="Streamlit Widget Demo", layout="wide")

# app title
st.title("🎛️ Streamlit Full Widget Demo App")
# add text to the page using markdown 
st.write("This app demonstrates every major Streamlit widget.")


# create multiple tabs to organize the layout
tab_inputs, tab_selectors, tab_buttons, tab_chat, tab_display, tab_data, tab_layout, tab_media = st.tabs([
    "Inputs", "Selectors", "Buttons", "Chat", "Display", "Data", "Layout", "Media"
])

# open a tab context to add widgets
with tab_inputs:
    # add a header to the page
    st.header("🟦 Input Widgets")
    # add a text input widget
    text_val = st.text_input("Text Input:", "Hello")
    # add a text area widget
    area_val = st.text_area("Text Area:", "Write something...")
    # add a number input widget with a name, min, max, and default value
    num_val = st.number_input("Number Input:", 0, 100, 42)
    # add a date input widget with a name and default value
    date_val = st.date_input("Date Input:", date.today())
    # add a time input widget with a name and default value
    time_val = st.time_input("Time Input:", time(12, 0))
    # add a file uploader widget with a name
    file_val = st.file_uploader("File Uploader:")
    # add a color picker widget with a name and default value
    color_val = st.color_picker("Color Picker:", "#00ff00")
    # add a camera input widget with a name
    img_val = st.camera_input("Camera Input (take a picture):")

    st.write("### Output:")
    # display json to the page as formatted text
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


with tab_selectors:
    st.header("🟩 Selector Widgets")

    # add a selectbox widget with a name and options
    select_val = st.selectbox("Selectbox:", ["A", "B", "C"])
    # add a multiselect widget with a name and options
    multi_val = st.multiselect("Multiselect:", ["A", "B", "C", "D"])
    # add a radio button widget with a name and options
    radio_val = st.radio("Radio:", ["Option 1", "Option 2", "Option 3"])
    # add a checkbox widget with a name
    check_val = st.checkbox("Checkbox")
    # add a slider widget with a name, min, max, and default value
    slider_val = st.slider("Slider:", 0, 100, 50)
    # add a range slider widget with a name, min, max, and default range value
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


with tab_buttons:
    st.header("🟨 Buttons & Forms")

    # add a simple button widget, and also check if it was clicked
    if st.button("Simple Button"):
        # show a success message
        st.success("Button clicked!")

    # add a form with a text input and a submit button
    with st.form("my_form"):
        name = st.text_input("Name in Form:")
        submitted = st.form_submit_button("Submit Form")

    if submitted:
        # show an info message
        st.info(f"Form submitted: {name}")

    # add a download button
    st.download_button("Download file", "Hello world!", "hello.txt")



with tab_chat:
    st.header("💬 Chat Widgets")

    # add a chat input widget and get the message when user sends it
    msg = st.chat_input("Say something:")
    if msg:
        # write a message to the chat history
        st.chat_message("user").write(msg)
        st.chat_message("assistant").write(f"Echo: {msg}")



with tab_display:
    st.header("📢 Display Elements")

    # display a success message
    st.success("Success message!")
    # display an error message
    st.error("Error message")
    # display a warning message
    st.warning("Warning")
    # display an info message
    st.info("Information message")
    # display an exception message 
    st.exception(Exception("This is an exception"))

    # display text using markdown
    st.markdown("### Markdown Example")
    st.markdown("**Bold**, *italic*, `code`")
    st.code("print('hello world')")

    # add metric widgets
    st.metric("Temperature", "30°C", "+2°C")

    # add a progress bar
    st.progress(40)

    # add a spinner
    with st.spinner("Loading..."):
        pass



with tab_data:
    st.header("📊 Data Widgets")

    df = pd.DataFrame({
        "A": np.random.randn(10),
        "B": np.random.randn(10),
        "C": np.random.randn(10),
    })

    st.write("### DataFrame:")
    # display a pandas dataframe
    st.dataframe(df)

    st.write("### Table:")
    # display a static table
    st.table(df.head())

    st.write("### JSON:")
    # display a JSON object
    st.json({"name": "Streamlit", "version": 1})

    st.write("### Charts:")
    # display line chart of a dataframe
    st.line_chart(df)
    # display area chart of a dataframe
    st.bar_chart(df)


with tab_layout:
    st.header("📐 Layout Widgets")

    st.subheader("Sidebar")
    # create a sidebar to put widgets in
    st.sidebar.write("This is the sidebar!")
    # add widgets to the sidebar
    st.sidebar.selectbox("Sidebar Selectbox", [1, 2, 3])

    st.subheader("Columns")
    # create columns to arrange widgets side by side
    col1, col2 = st.columns(2)
    # add content to each column
    col1.write("Left column")
    col2.write("Right column")

    st.subheader("Expander")
    # create an expander that can hide content
    with st.expander("Open Me"):
        st.write("Hidden content")

    st.subheader("Container")
    # create a container to group elements
    container = st.container()
    # add content to the container
    container.write("Inside container")

    st.subheader("Placeholder")
    # create a placeholder to update content later
    placeholder = st.empty()
    # add content to the placeholder
    placeholder.write("This will update in 2 seconds...")

    time.sleep(2)
    placeholder.write("Updated!")


with tab_media:
    st.header("📷 Media Widgets")

    # display image, video, and audio
    st.image("https://placekitten.com/300/200", caption="Random Cat")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav")

st.write("---")
st.write("Made with ❤️ using Streamlit")
