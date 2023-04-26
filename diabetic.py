import pickle
import streamlit as st 

# loading diabetic model
model = pickle.load(open('diabetic_model.pkl','rb'))
scaler = pickle.load(open('stdscalers.pkl','rb'))

st.set_page_config(page_title="Diabetes Prediction", page_icon="💉")
st.markdown('''<h1 style="color:purple;font-family:verdana;font-size:50px">Diabetes Prediction</h1>''',unsafe_allow_html=True)

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<div class="alert alert-danger" role="alert">
    This model is trained with 77.27% accuracy so it may give wrong prediction to.
</div>
""", unsafe_allow_html=True)



col1, col2, col3 = st.columns(3)
 # taking values from user
with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
with col2:
    Glucose = st.text_input('Glucose Level')
with col3:
    BloodPressure = st.text_input('Blood Pressure Value')
with col1:
    SkinThickness = st.text_input('Skin Thickness Value')
with col2:
    Insulin = st.text_input('Insulin Level')
with col3:
    BMI = st.text_input('BMI Value')
with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
with col2:
    Age = st.text_input('Age')
    #  code for prediction
if st.button('Diabetes Test'):
    data = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
    data = scaler.transform(data)
    prediction = model.predict(data)
    if (prediction[0] == 0):
        Result = 'The person is not diabetic'
    else:
        Result = 'The person is diabetic'
    
    st.header(Result)