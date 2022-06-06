import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

print('Beginning file download with urllib2...')

@st.experimental_memo
def download_data():
  url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
  filename = 'cat.jpg'
  urllib.request.urlretrieve(url, 'cat.jpg')
  return filename


st.write(download_data())


n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)
