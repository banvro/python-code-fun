# from ascii_magic import AsciiArt

# AsciiArt.from_image("naresh_new.jpeg").to_terminal()



import streamlit as st
from countryinfo import CountryInfo
import pycountry
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="🌍 Country Info Explorer", layout="wide")

st.title("🌍 Country Info Explorer")
st.write("Select a country from the dropdown to see all its information.")

# --- Get all country names ---
countries_list = [country.name for country in pycountry.countries]
countries_list.sort()

# --- Dropdown selection ---
selected_country = st.selectbox("Choose a country:", countries_list)

if selected_country:
    country = CountryInfo(selected_country)
    info = country.info()  # full info dictionary

    # --- Display in two columns ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 Basic Info")
        st.write(f"**Capital:** {country.capital()}")
        st.write(f"**Population:** {country.population():,}")
        st.write(f"**Region:** {info.get('region', 'N/A')}")
        st.write(f"**Subregion:** {info.get('subregion', 'N/A')}")
        st.write(f"**Currencies:** {', '.join(country.currencies())}")
        st.write(f"**Languages:** {', '.join(country.languages())}")

    with col2:
        st.subheader("🌐 Other Info")
        st.write(f"**Timezones:** {', '.join(country.timezones())}")
        st.write(f"**Borders:** {', '.join(country.borders()) if country.borders() else 'None'}")
        st.write(f"**Calling Codes:** {', '.join(country.calling_codes())}")
        st.write(f"**ISO Codes:** {info.get('alpha2', 'N/A')} / {info.get('alpha3', 'N/A')}")

