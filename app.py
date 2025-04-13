import streamlit as st
import numpy as np
import pickle

# Set page title
st.title("Insurance Premium Prediction 💰")

try:
    # Load the model
    with open('modl.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # Create input fields
    st.subheader("Enter Your Details:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Personal Information
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        marital_status = st.selectbox("Marital Status", ["Married", "Unmarried"])
        dependants = st.number_input("Number of Dependants", min_value=0, max_value=5, value=0)
        region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])
    
    with col2:
        # Financial and Employment Information
        income = st.number_input("Income (in Lakhs)", min_value=1.0, max_value=100.0, value=12.5)
        insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])
        employment = st.selectbox("Employment Status", ["Other", "Salaried", "Self-Employed"])
        risk_score = st.slider("Risk Score", min_value=0.0, max_value=1.0, value=0.5)

    # Health Information
    st.subheader("Health Information:")
    col3, col4 = st.columns(2)
    
    with col3:
        bmi_category = st.selectbox("BMI Category", ["Normal", "Underweight", "Overweight", "Obesity"])
    with col4:
        smoking = st.selectbox("Smoking Status", ["No Smoking", "Occasional", "Regular"])

    # Predict button
    if st.button("Calculate Premium"):
        # Convert categorical to numeric
        plan_mapping = {"Bronze": 0, "Silver": 1, "Gold": 2}
        insurance_plan_encoded = plan_mapping[insurance_plan]
        
        # Create input array
        input_data = np.array([[
            age,
            dependants,
            income,
            insurance_plan_encoded,
            risk_score,
            1 if gender == "Male" else 0,
            1 if region == "Northwest" else 0,
            1 if region == "Southeast" else 0,
            1 if region == "Southwest" else 0,
            1 if marital_status == "Unmarried" else 0,
            1 if bmi_category == "Obesity" else 0,
            1 if bmi_category == "Overweight" else 0,
            1 if bmi_category == "Underweight" else 0,
            1 if smoking == "Occasional" else 0,
            1 if smoking == "Regular" else 0,
            1 if employment == "Salaried" else 0,
            1 if employment == "Self-Employed" else 0
        ]])

        try:
            # Make prediction
            prediction = model.predict(input_data)
            
            # Display result in a nice format
            st.success(f"Predicted Annual Premium: ₹{prediction[0]:,.2f}")
            
            # Display summary of key factors
            st.info("""
            Key factors affecting your premium:
            • Age and number of dependants
            • Insurance plan type
            • BMI category and smoking status
            • Employment status and income
            """)
            
        except Exception as e:
            st.error(f"Prediction Error: {str(e)}")

except FileNotFoundError:
    st.error("Error: Model file 'modl.pkl' not found!")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
