import streamlit as st
import sturgmap.foliumap as sturgmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/nathansturgill/sturgmap_streamlit>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Sturgmap Split Map")

with st.expander("See source code"):
    with st.echo():
        m = sturgmap.Map()
        m.add_basemap("Esri.WorldImagery")
        m.add_basemap("OpenTopoMap")
        m.add_layer_control()

m.to_streamlit(width=1000, height=700)