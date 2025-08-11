import streamlit as st
import pickle

# Load your model
with open("firstAIDmodel.pkl", "rb") as f:
    model = pickle.load(f)

st.title("First Aid Helper 🩹")
st.write("Enter an injury description to get severity, first aid steps, and injury type.")

# Input from user
injury_description = st.text_area("Injury Description")

if st.button("Predict"):
    if injury_description.strip():
        prediction = model.predict([injury_description])
        severity, first_aid_steps, injury_type = prediction[0]
        
        st.subheader("Prediction")
        st.write(f"**Severity:** {severity}")
        st.write(f"**First Aid Steps:** {first_aid_steps}")
        st.write(f"**Injury Type:** {injury_type}")
    else:
        st.warning("Please enter a description.")
