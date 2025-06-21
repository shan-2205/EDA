




import streamlit as st
import numpy as np
import joblib

# --- Load Model and Vectorizer ---


def load_assets():
    vec = joblib.load("R:/All_Datasets/Password_strength/data/tfidf_vectorizer.pkl")
    clf = joblib.load("R:/All_Datasets/Password_strength/data/logistic_regression_model.pkl")
    return vec , clf


# Load your assets when the app starts
vectorizer, clf = load_assets()



# --- Password Strength Prediction Function (Modified for Streamlit) ---
def predict_strength(password):
    if vectorizer is None or clf is None:
        return "Model not loaded. Please check file paths."

    if not password:
        return "Please enter a password."
    
    # we can recieve password usiing st.text_input()
    # Transform the input password
    sample_array = np.array([password])
    sample_matrix = vectorizer.transform(sample_array)

    # Calculate the additional features
    length_pass = len(password)
    
    # Handle division by zero for empty password (though checked above)
    length_normalised_lowercase = len([char for char in password if char.islower()])/len(password)

    # Combine TF-IDF features with additional features
    # Ensure the combined array matches the model's expected input shape (1, 101)
    new_matrix = np.append(sample_matrix.toarray(), [[length_pass, length_normalised_lowercase]], axis=1)

    # Make the prediction
    result = clf.predict(new_matrix)

    # Interpret the result
    if result == 0:
        return "Weak 😞"
    elif result == 1:
        return "Medium 🙂"
    else: # result == 2
        return "Strong! 💪"




# --- Streamlit App ---

## set_page_config() : configure the basic settings of your web application page.
## page_title = "Bitcoin Dashboard":
## This sets the title that appears in your browser tab or window..
## layout = "centered": , This sets the layout of the app to be centered (content appears in the middle of the page).
# --- Configuration ---




# --- Streamlit App Layout ---
st.set_page_config(
    page_title="Password Strength Predictor",
    page_icon="🔒",
    layout="centered"
)

st.title("🔒 Password Strength Predictor") ## 🔒 - locked emoji 
st.markdown("Type a password below and hit 'Enter' or click 'Check Strength'.")

# st.text_input() : create Input field for password
# type = "password" , Hides the characters the user types (like dots or asterisks)
# placeholder = "" , Faint text shown inside the box until the user types something
password_input = st.text_input("Enter your password:", type="password", placeholder="myS3cr3tP@ssw0rd")

# Button to trigger prediction (optional, can also use on_change in text_input)
if st.button("Check Strength"):  ## if user clicks on Check Strength button, the code inside the block runs.
    if password_input: ## if the user has entered a password..
        strength = predict_strength(password_input)
        st.markdown("**Your password strength is: " + strength + "**")
    else:
        st.warning("Please enter a password to check its strength.")

st.markdown("---")
st.info("This simple app uses a trained machine learning model to estimate password strength.")






## open powershell prompt : 
## cd "R:\2.. Entire_Data_Science_Projects\2.. NLP\Password_Strength\2.. Current_Password_Strength_Udemy\Feb_2023"
## streamlit run NLP_password_strength_deployment.py



