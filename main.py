import streamlit as st
import joblib

# Load the pre-trained model
model = joblib.load('personality_model.pkl')
# Function to make predictions
def predict(input_data):
    result = ""
    # Convert input data to the format expected by the model
    input_data = [input_data]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "Introvert"
    else:
        result = "Extrovert"
    return result

# Streamlit app

st.title("Personality Type Prediction")
st.write("This app predicts whether a person is an Introvert or an Extrovert based on their responses to a questionnaire.")
# Input fields for the questionnaire

# columns for model
# 1. Time spent alone
# 2. Stage fear (categorical) needs to be converted to numerical only yes and no = 0 and 1
# 3. Social event attendance
# 4. Going outside
# 5. Drained by socializing (categorical) needs to be converted to numerical only yes and no = 0 and 1
# 6. Friend circle size
# 7. Post Frequency

time_spent_alone = st.slider("Time spent alone (hours per day)", 0, 10, 1)
stage_fear = st.selectbox("Do you have stage fear?", ["No", "Yes"])
social_event_attendance = st.slider("Social event attendance (events per month)", 0, 30, 5)
going_outside = st.slider("Going outside (hours per week)", 0, 10, 1)
drained_by_socializing = st.selectbox("Do you feel drained by socializing?", ["No", "Yes"])
friend_circle_size = st.slider("Friend circle size", 1, 100, 15)
post_frequency = st.slider("Post frequency (posts per week)", 0, 100, 5)
# Convert categorical inputs to numerical values
stage_fear = 1 if stage_fear == "Yes" else 0
drained_by_socializing = 1 if drained_by_socializing == "Yes" else 0
# Create a dictionary to hold the input data
input_data = [
    time_spent_alone,
    stage_fear,
    social_event_attendance,
    going_outside,
    drained_by_socializing,
    friend_circle_size,
    post_frequency
]
# Make prediction when the button is clicked
if st.button("Predict"):
    prediction = predict(input_data)
    st.success(f"The predicted personality type is: {prediction}")
