import streamlit as st

# using one terminal window to run streamlit
# and one for everything else
st.title('yo big title') #large font

st.write('poggggg it\'s a normal line of text') #smaller font

btn = st.button('name') #becomes true when clicked on
cbox = st.checkbox('name') #true when selected
sbox_options = ['a','list','of','options']
sbox = st.selectbox('name of sbox', sbox_options)

slider = st.slider('slide name', 0, 20) #name, start, end
st.write(f'you selected {slider}') 
