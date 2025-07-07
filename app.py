import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Custom HTML Viewer", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background-image: url("https://raw.githubusercontent.com/Sznxnzu/Temporary/main/Stardew%20Valley%20Font.png");
      background-size: cover;
      background-position: center;
      margin: 0;
      height: 100vh;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    h1 {
      background: rgba(0, 0, 0, 0.5);
      padding: 20px;
      border-radius: 10px;
    }
  </style>
</head>
<body>

</body>
</html>
"""

components.html(html_code, height=600)
