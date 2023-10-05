import streamlit as st
import numpy as np
import pandas as pd


import pickle 
pickle_in = open('clf.pkl' , 'rb')

clf = pickle.load(pickle_in)

def Flower_Prediction (SepalLengthCm,SepalWidthCm , PetalLengthCm , PetalWidthCm):

    SepalLengthCm  =float(SepalLengthCm)
    SepalWidthCm  =float(SepalWidthCm )
    PetalLengthCm  =float(PetalLengthCm)
    PetalWidthCm  = float(PetalWidthCm )
    prediction = clf.predict([[SepalLengthCm,SepalWidthCm , PetalLengthCm , PetalWidthCm]])

    print(prediction[0])
    return prediction[0]

def main():
    st.title("Flower Prediction Price")   
    html_temp = """
    <div style = "background-color : tomato; padding : 10px">
    <h2 style = "color:white ; text-align:centre;> Flower Prediction ML App</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html= True)

    SepalLengthCm = st.text_input("sepal length","")
    SepalWidthCm = st.text_input("sepal width ","")
    PetalLengthCm= st.text_input("petal length","")
    PetalWidthCm = st.text_input("petal width ","")


    result = ""

    if st.button("predict"):
        result = Flower_Prediction(SepalLengthCm,SepalWidthCm , PetalLengthCm , PetalWidthCm)
        if result == 1 :
            result = 'Iris-setosa'
        elif result ==2 : 
            result  ='Iris-versicolor' 
        else:
            result  = 'Iris-virginica'
       
    st.success("The Output is {}".format(result))    
    if st.button("About"):
        st.text("Let's Learn")

        st.text("Built With Streamlit")
 

if __name__ == '__main__' :
    main()