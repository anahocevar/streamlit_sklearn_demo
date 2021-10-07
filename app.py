import streamlit as st
import dill

def app():
    
    st.title("A Streamlit App Demo")
    
    st.sidebar.markdown('''This is the sidebar. If you want content in your sidebar, enter it here.''')

    
    st.markdown(""" ## About this app""")
    st.markdown("""
     This app can make predictions! You can use it by passing in the miles per gallon of a car, the number of cylinders and the horsepower and get the prediction of car weight. The app uses:

        * sklearn
        * and streamlit
                """)
    
    st.markdown(""" ## Predict the weight of the car!""")


    mpg = float(st.text_input('What is the mpg of the car', '0'))
    cylinders = float(st.text_input('How many cylinders does it have?', '0'))
    horsepower = float(st.text_input('What is the horsepower?', '0'))
    
    
    with open('weight_model.dill', 'rb') as f:
            weight_model = dill.load(f)
            
    if st.button("Predict weight!"):

        prediction = weight_model.predict([[mpg, cylinders, horsepower]])

        st.markdown("""The predicted weight of the car is:""")

        st.write(prediction[0])


if __name__ == '__main__':
    app()
