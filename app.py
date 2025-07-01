import streamlit as st
import requests

st.set_page_config(page_title="GitHub Profile Visualizer", layout="centered")

st.title("👩‍💻 GitHub Profile Visualizer")
username = st.text_input("Enter GitHub Username", "")

if username:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        
        st.image(user_data["avatar_url"], width=100)
        st.write(f"**Name:** {user_data.get('name', 'N/A')}")
        st.write(f"**Bio:** {user_data.get('bio', 'N/A')}")
        st.write(f"**Public Repos:** {user_data['public_repos']}")
        st.write(f"**Followers:** {user_data['followers']}")
        st.write(f"**Following:** {user_data['following']}")
        st.write(f"**GitHub URL:** [Visit]({user_data['html_url']})")
    else:
        st.error("User not found. Please check the username.")
