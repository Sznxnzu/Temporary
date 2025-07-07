import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Custom HTML Viewer", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      min-height: 100vh;
    }

    body {
      background-image: url("https://raw.githubusercontent.com/Sznxnzu/Temporary/main/Stardew%20Valley%20Font.png");
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center center;
      background-color: black; /* fallback color behind transparent areas */
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    h1 {
      background: rgba(0, 0, 0, 0.5);
      padding: 20px;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <h1>Welcome Back to the Farm, Naomi!</h1>
</body>
</html>
"""

components.html(html_code, height=700)
