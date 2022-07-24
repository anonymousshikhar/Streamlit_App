import streamlit as st
import pandas as pd

st.header('''
This is a Streamlit app Demo''')

st.subheader('Addition of Two numbers')

def user_input():
  first_num = st.number_input('Enter First Number')
  second_num = st.number_input('Enter Second Number')

  data = {'First Number':first_num,
          'Second Number':second_num}

  features = pd.DataFrame(data, index = [0])
  features['Sum of the numbers'] = features.sum(axis = 1)
  return features 

df = user_input()
st.write(df)
