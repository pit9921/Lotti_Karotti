#!/usr/bin/env python
# coding: utf-8
# %%
import streamlit as st  
import os
import random
from PIL import Image
import pyautogui

imgExtension = ["png", "jpeg", "jpg"] #Image Extensions to be chosen from
allImages = list()

def chooseRandomImage(directory="./Images"):
    for img in os.listdir(directory): #Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice] #Do Whatever you want with the image file
    return chosenImage

randomImage = chooseRandomImage()


# %%
st.set_page_config(
    page_title="Lotti Karotti",
    layout="wide",
)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    
    
local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                }
               .css-1d391kg {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

image = Image.open('./Images/' + str(randomImage))

import time
time.sleep(1.5)
st.image(image)


 
if st.button("Nächste"):
    pyautogui.hotkey("ctrl","F5")
#     st.experimental_rerun()


# Remove “Made with Streamlit” from bottom of app
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# %%
