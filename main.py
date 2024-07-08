import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn import feature_extraction

# loading the saved models
from joblib import load
spam_detection_model = load('spam_detection_model.sav')


    # page title
st.title('Spam SMS Detection using ML')
    
    
    # creating a text box for user input
Text = st.text_area('Enter the SMS text here')


# code for Prediction
result = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):
    input_data_features = feature_extraction.transform(Text)
    prediction = spam_detection_model.predict(input_data_features)
    
    if (prediction[0] == 1):
        result = 'SMS is spam'
    else:
        result = 'SMS is not spam'
    
st.success(result)




