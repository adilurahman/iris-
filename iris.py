import streamlit as st
import numpy as np
import pickle


with open ("model.pkl","rb") as f:
    model=pickle.load(f)


st.title("Iris Flower Species Prediction app")
sepal_length=st.number_input("Sepal Length (cm)",min_value=0.0,max_value=10.0,value=5.0)
sepal_width=st.number_input("Sepal Width (cm)",min_value=0.0,max_value=10.0,value=3.5)
petal_length=st.number_input("Petal Length (cm)",min_value=0.0,max_value=10.0,value=1.5)
petal_width=st.number_input("Petal Width (cm)",min_value=0.0,max_value=10.0,value=0.2)
predict =st.button("Predict Species")
# button predictl store cheyyunnu


#after clicking the button

if predict:
   input_data= np.array([[sepal_length,sepal_width,petal_length,petal_width]])
   prediction=model.predict(input_data)

   st.success(f"predicted species is : {prediction[0]}")
   st.balloons()
#