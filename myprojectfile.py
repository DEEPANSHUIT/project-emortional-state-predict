import pickle
import streamlit as st
model1=pickle.load(open("social.pkt",'rb'))
def myfn():
    st.title("PREDICTING EMOTIONAL STATE ON THE BASIS OF SOCIAL MEDIA USAGE ")
    age=st.number_input("Enter your age:")
    gender=st.number_input("Enter your gender : 0 for Female and 1 for Male")
    dailyusage=st.number_input("Enter your daily usage on Social Media in Minutes")
    post=st.number_input("Enter number of posts per day")
    likes=st.number_input("Enter number of likes per day")
    comments=st.number_input("Enter number of comments received per day")
    messages=st.number_input("Enter number of messages sent per day")
    pred=st.button("Click here to predict your Emotion State")
    if pred:
        op=model1.predict([[age,gender,dailyusage,post,likes,comments,messages]])
        st.write("0 means Anger")
        st.write("1 means Anxiety")
        st.write("2 means Boredom")
        st.write("3 means Happiness")
        st.write("4 means Neutral")
        st.write("5 means Sadness")
            
        st.write("your emotional state is:",op)
myfn()

    