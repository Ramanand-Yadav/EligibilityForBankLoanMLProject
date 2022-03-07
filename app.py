# %%writefile app.py
import streamlit as st 
import pickle
from PIL import Image
import pandas as pd

model = pickle.load(open('BankLoanmodel.pkl', 'rb'))

def run():
  img1 = Image.open('img1.jpg')
  st.image(img1)
  st.title("""
  Bank Loan Prediction using Machine Learning
  **The major aim of this project is to predict which of the customers will have their loan approved.**
""")

  # Account No
  account_no = st.text_input('Account number')

  # Full Name
  fn = st.text_input('Full Name')

  # For gender
  gen_display = ('Female','Male')
  gen_options = list(range(len(gen_display)))
  gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

  # For Marital Status
  mar_display = ('Yes', 'No')
  mar_options = list(range(len(mar_display)))
  Married = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

  # No of dependets
  dep_display = ('No','One','Two','More than Two')
  dep_options = list(range(len(dep_display)))
  Dependents = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

  # For edu
  edu_display = ('Graduate','Not Graduate')
  edu_options = list(range(len(edu_display)))
  Education = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

  # For emp status
  emp_display = ('Job','Business')
  emp_options = list(range(len(emp_display)))
  Self_Employed = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

  # Applicant Monthly Income
  ApplicantIncome = st.number_input("Applicant's Monthly Income($)",value=0)

  # Co-Applicant Monthly Income
  CoapplicantIncome = st.number_input("Co-Applicant's Monthly Income($)",value=0)

  # Loan AMount
  LoanAmount = st.number_input("Loan Amount",value=0)


  # For Credit Score
  cred_display = ('Between 300 to 500','Above 500')
  cred_options = list(range(len(cred_display)))
  Credit_History = st.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])


  # For Property status
  prop_display = ('Rural','Urban','Semi-Urban')
  prop_options = list(range(len(prop_display)))
  prop = st.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])



  # loan duration
  dur_display = ['Less than 1 Month','1 Month', '2 Month','4 Month', '6 Month','8 Month','10 Month','1 Year','16 Month']
  dur_options = range(len(dur_display))
  dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])
  duration = 0
  if dur == 0:
    duration = 12
  if dur == 1:
    duration = 36
  if dur == 2:
    duration = 60
  if dur == 3:
    duration = 120
  if dur == 4:
    duration = 180
  if dur==5:
    duration = 240
  if dur==6:
    duration = 300
  if dur==7:
    duration = 360
  if dur==8:
    duration = 480

#   features = pd.DataFrame({'Gender':gen, 'Married':Married, 'Dependents':Dependents, 'Education':Education,
#                             'Self_Employed':Self_Employed,'ApplicantIncome':ApplicantIncome, 'CoapplicantIncome':CoapplicantIncome,
#                             'LoanAmount':LoanAmount,'Loan_Amount_Term':duration, 'Credit_History':Credit_History, 'Property_Area':prop},index=[0])
#   features = features.astype('int')
#   st.write(features)




  if st.button("Submit"):
    features = pd.DataFrame({'Gender':gen, 'Married':Married, 'Dependents':Dependents, 'Education':Education,
                             'Self_Employed':Self_Employed,'ApplicantIncome':ApplicantIncome, 'CoapplicantIncome':CoapplicantIncome,
                             'LoanAmount':LoanAmount,'Loan_Amount_Term':duration, 'Credit_History':Credit_History, 'Property_Area':prop},index=[0])
    features = features.astype('int')
    st.write(features)
    prediction = model.predict(features)
    lc = [str(i) for i in prediction]
    ans = int("".join(lc))
    if ans == 0:
        st.error(
            "Hello: " + fn +" || "
            "Account number: "+account_no +' || '
            'According to our Calculations, you will not get the loan from Bank'
        )
    else:
        st.success(
            "Hello: " + fn +" || "
            "Account number: "+account_no +' || '
            'Congratulations!! you will get the loan from Bank'
        )
  





run()