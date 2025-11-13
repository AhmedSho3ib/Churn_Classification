import streamlit as st
from utils.inference import predict_new
from utils.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor, forest_model, xgboost_model
from utils.CustomerData import CustomerData

# Page configuration
st.set_page_config(
    page_title=f"{APP_NAME} v{VERSION}",
    page_icon="🏦",
    layout="wide"
)

# Session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Authentication function
def authenticate():
    st.title(f"🔐 {APP_NAME} Login")
    st.write(f"Version {VERSION}")
    
    api_key = st.text_input("Enter API Key", type="password")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Login", use_container_width=True):
            if api_key == SECRET_KEY_TOKEN:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid API Key. Access denied.")
    
    # Footer
    st.write("")
    st.write("---")
    st.markdown("<div style='text-align: center;'><strong>Made With Love by Eng. Ahmed Shoaib</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><a href='https://github.com/AhmedSho3ib' target='_blank'>GitHub Profile</a></div>", unsafe_allow_html=True)

# Main application
def main_app():
    # Header
    st.title(f"🏦 {APP_NAME}")
    st.caption(f"Version {VERSION}")
    st.write("Predict customer churn using machine learning models")
    
    # Logout button at top right
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        if st.button("Logout", type="secondary"):
            st.session_state.authenticated = False
            st.rerun()
    
    st.write("---")
    
    # Model selection with radio buttons
    st.write("## 🤖 Select Prediction Model")
    model_choice = st.radio(
        "Choose a model:",
        ["Random Forest", "XGBoost"],
        horizontal=True,
        help="Select the machine learning model for prediction"
    )
    
    st.write("---")
    
    # Input form
    st.write("## Customer Information")
    
    with st.form("prediction_form"):
        # Create three columns for better layout
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("📊 Financial Info")
            credit_score = st.number_input(
                "Credit Score",
                min_value=300,
                max_value=850,
                value=650,
                help="Customer's credit score"
            )
            
            balance = st.number_input(
                "Account Balance ($)",
                min_value=0.0,
                value=0.0,
                step=1000.0,
                format="%.2f",
                help="Current account balance"
            )
            
            estimated_salary = st.number_input(
                "Estimated Salary ($)",
                min_value=0.0,
                value=50000.0,
                step=1000.0,
                format="%.2f",
                help="Estimated annual salary"
            )
        
        with col2:
            st.subheader("👤 Personal Info")
            geography = st.selectbox(
                "Country",
                options=['Spain', 'Germany', 'France'],
                help="Customer's country of residence"
            )
            
            gender = st.selectbox(
                "Gender",
                options=['Male', 'Female'],
                help="Customer's gender"
            )
            
            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=35,
                help="Customer's age (18-100)"
            )
        
        with col3:
            st.subheader("🏦 Account Details")
            tenure = st.slider(
                "Tenure (Years)",
                min_value=0,
                max_value=10,
                value=5,
                help="Years as a customer (0-10)"
            )
            
            num_of_products = st.selectbox(
                "Number of Products",
                options=[1, 2, 3, 4],
                index=0,
                help="Number of bank products held"
            )
            
            has_cr_card = st.selectbox(
                "Has Credit Card",
                options=[0, 1],
                format_func=lambda x: "Yes" if x == 1 else "No",
                help="Does the customer have a credit card?"
            )
            
            is_active_member = st.selectbox(
                "Active Member",
                options=[0, 1],
                format_func=lambda x: "Yes" if x == 1 else "No",
                help="Is the customer an active member?"
            )
        
        # Submit button
        st.write("")
        submit_button = st.form_submit_button(
            "🔮 Make Prediction",
            use_container_width=True,
            type="primary"
        )
    
    # Make prediction
    if submit_button:
        try:
            with st.spinner("Analyzing customer data..."):
                # Create CustomerData object
                customer_data = CustomerData(
                    CreditScore=credit_score,
                    Geography=geography,
                    Gender=gender,
                    Age=age,
                    Tenure=tenure,
                    Balance=balance,
                    NumOfProducts=num_of_products,
                    HasCrCard=has_cr_card,
                    IsActiveMember=is_active_member,
                    EstimatedSalary=estimated_salary
                )
                
                # Select model
                model = forest_model if model_choice == "Random Forest" else xgboost_model
                
                # Make prediction
                result = predict_new(
                    data=customer_data,
                    preprocessor=preprocessor,
                    model=model
                )
                
                # Display results
                st.write("---")
                st.success("✅ Prediction completed!")
                st.write("## 📊 Prediction Results")
                
                # Create metrics display
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Model Used", model_choice)
                
                # Display result based on structure
                if isinstance(result, dict):
                    # Check for common prediction keys
                    if 'prediction' in result:
                        with col2:
                            prediction_label = "Will Churn" if result['prediction'] == 1 else "Will Stay"
                            st.metric("Prediction", prediction_label)
                    
                    if 'probability' in result or 'churn_probability' in result:
                        prob_key = 'probability' if 'probability' in result else 'churn_probability'
                        with col3:
                            prob_value = result[prob_key]
                            if isinstance(prob_value, (list, tuple)):
                                prob_value = prob_value[1] if len(prob_value) > 1 else prob_value[0]
                            st.metric("Churn Probability", f"{prob_value:.2%}")
                    
                    # Display all results
                    st.write("### Detailed Results")
                    for key, value in result.items():
                        if key not in ['prediction', 'probability', 'churn_probability']:
                            st.write(f"**{key.replace('_', ' ').title()}:** {value}")
                else:
                    with col2:
                        st.write(result)
                
                # Show raw result in expander
                with st.expander("🔍 View Raw Results"):
                    st.json(result)
                
                # Show input data summary
                with st.expander("📋 Input Data Summary"):
                    input_data = {
                        "Credit Score": credit_score,
                        "Geography": geography,
                        "Gender": gender,
                        "Age": age,
                        "Tenure": tenure,
                        "Balance": f"${balance:,.2f}",
                        "Number of Products": num_of_products,
                        "Has Credit Card": "Yes" if has_cr_card == 1 else "No",
                        "Active Member": "Yes" if is_active_member == 1 else "No",
                        "Estimated Salary": f"${estimated_salary:,.2f}"
                    }
                    for key, value in input_data.items():
                        st.write(f"**{key}:** {value}")
                    
        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")
            st.write("Please check your input data and try again.")
            with st.expander("Error Details"):
                st.code(str(e))
    
    # Footer
    st.write("")
    st.write("---")
    st.markdown("<div style='text-align: center;'><strong>Made With Love by Eng. Ahmed Shoaib</strong></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><a href='https://github.com/AhmedSho3ib' target='_blank'>GitHub Profile</a></div>", unsafe_allow_html=True)

# App flow
if not st.session_state.authenticated:
    authenticate()
else:
    main_app()