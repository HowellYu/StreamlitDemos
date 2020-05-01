import streamlit as st
import pandas as pd
from matplotlib import pyplot



## Working with Text
# Text/Title
st.title("Streamlit Tutorials")

# Header/Subheader
st.header("Working with Text")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")



## Working with Colorful Text and Error Messages
st.header("Working with Colorful Text and Error Messages")
st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")



## Getting Help Info About Python
st.header("Getting Help Info About Python")
st.help(range)



## Widget: Checkbox,Selectbox,Radio button,etc
st.header("Widget: Checkbox,Selectbox,Radio button,etc")

# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
	st.success("You are Active")
else:
	st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","DataScientist","Doctor","Businessman"])
st.write("You selected this option ",occupation)

# MultiSelect
location = st.multiselect("Where do you work?",("London","New York","Accra","Kiev","Nepal"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)

# Buttons
st.button("Simple Button")

if st.button("About"):
	st.text("Streamlit is Cool")



## How to receive user input and process them with streamlit?
st.header("How to receive user input and process them with streamlit?")

# Receiving User Text Input
firstname = st.text_input("Enter Your Firstname","Type Here..")
if st.button("Submit Key"):
	result = firstname.title()
	st.success(result)

# Text Area
message = st.text_area("Enter Your message","Type Here..")
if st.button("Submit"):
	result = message.title()
	st.success(result)

# Date Input
import datetime
today = st.date_input("Today is",datetime.datetime.now())

# Time
the_time = st.time_input("The time is",datetime.time())



# # Working with media files eg images,audio,video
# st.header("Working with media files eg images,audio,video")
# # Images
# from PIL import Image
# img = Image.open("example.jpeg")
# st.image(img,width=300,caption="Simple Image")
#
#
# # Videos
# vid_file = open("example.mp4","rb").read()
# # vid_bytes = vid_file.read()
# st.video(vid_file)
#
# # Audio
# audio_file = open("examplemusic.mp3","rb").read()
# st.audio(audio_file,format='audio/mp3')



## Using the Write Function For More
st.header("Using the Write Function For More")
# Writing Text/Super Fxn
st.write("Text with write")
st.write(range(10))



## Displaying Raw Code and JSON
st.header("Displaying Raw Code and JSON")
# Displaying Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw Code
with st.echo():
# This will also show as a comment
    df = pd.DataFrame({'col1':[1,2,3], 'col2':[2,3,4]})



## Displaying JSON
st.header("Displaying JSON")
st.text("Display JSON")
st.json({'name':"Jesse",'gender':"male"})



## Displaying Progressbars,Spinners and Balloons
st.header("Displaying Progressbars,Spinners and Balloons")
# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting .."):
     time.sleep(2)
     st.success("Finished!")

# Balloons
st.balloons()



## Working with Data Science (DataFrame,Plot,Tables,etc)
st.header("Working with Data Science (DataFrame,Plot,Tables,etc)")
# Plot
st.pyplot()

# DataFrames
st.dataframe(df)

# Tables
st.table(df)



## Showing Sidebars
sidebar_text = st.selectbox("Sidebar text",["This is a sidebar","Introducing: sidebar","Hey","What up"]) # the whole notebook will be re-run
st.header("Showing Sidebars")
# SIDEBARS
st.sidebar.header(sidebar_text)
st.sidebar.text("This is Streamlit Tut")



## Working with Functions
st.header("Working with Functions")
# Normal Function
def run_fxn():
    return range(100)

st.write(run_fxn())

# To Improve Performance/Speed via caching
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())
