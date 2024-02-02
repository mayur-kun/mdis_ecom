import streamlit as st 
# import pickle
import joblib
from google.cloud import storage

# Load model from storage bucket
client = storage.Client()
bucket = client.bucket('ecom_deployment_bucket')
blob = bucket.blob('random_forest_model_v1-0.pkl')
model = joblib.load(blob.open('rb'))

def predict(list1):
    
    print("inside predict function")
    prediction=model.predict(list1)
    return prediction


def main():

    pred_arr = []

    gender_dict = {"Male":1, "Female":0}
    marital_status_dict = {"Single":(0,0,1), "Married":(0,1,0), "Divorced":(1,0,0)}
    pref_login_device_dict = {"Mobile Phone":1, "Computer":0}
    pref_payment_mode_dict = {"Debit Card":(0,0,1,0,0), "Credit Card":(0,1,0,0,0), "E Wallet":(0,0,1,0,0), 
                         "Cash on Delivery": (1,0,0,0,0), "UPI": (0,0,0,0,1)}
    pref_order_category_dict = {"Fashion":(0,0,1,0,0), "Grocery":(0,1,0,0,0), "Laptop & Accessory":(0,0,1,0,0), 
                           "Mobile Phone": (1,0,0,0,0), "Others": (0,0,0,0,1)}
    


    st.title("E-Commerce Customer Churn Prediction")
    html_temp = """
    <div style="background-color:#b3db86;padding:5px">
    <h2 style="color:black;text-align:center;">Predicting Customer Churn</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    tenure = st.slider("\n Customer tenure?", min_value=0, max_value=100)
    pred_arr.extend([tenure])

    login_device = st.selectbox("Preferred login device?", ("Mobile Phone", "Computer"))
    pred_arr.extend([pref_login_device_dict[login_device]])

    city_tier = st.selectbox("Which tier city do you live in?",("1", "2", "3"))
    pred_arr.extend([city_tier])

    warehouse_to_home = st.slider("Distance from the warehouse to customer address?", min_value=0, max_value=500)
    pred_arr.extend([warehouse_to_home])

    payment_mode = st.selectbox("Preferred payment mode?", ("Debit Card", "Credit Card", "E Wallet", "Cash on Delivery", "UPI"))
    pred_arr.extend(list(pref_payment_mode_dict[payment_mode]))

    gender = st.selectbox("Gender",("Male", "Female"))
    pred_arr.extend([gender_dict[gender]])

    hours_spent_app = st.slider("Hours spent on the app in a day?", min_value=0, max_value=10)
    pred_arr.extend([hours_spent_app])

    devices_registered = st.slider("No. of registered devices?", min_value=0, max_value=10)
    pred_arr.extend([devices_registered])

    order_category = st.selectbox("Preferred order category",("Fashion", "Grocery", "Laptop & Accessory", "Mobile Phone", "Others"))
    pred_arr.extend(list(pref_order_category_dict[order_category]))
    
    satisfaction_score = st.slider("Customer satisfaction score", min_value=0, max_value=10)
    pred_arr.extend([satisfaction_score])

    marital_status = st.selectbox("Marital status",("Single", "Married", "Divorced"))
    pred_arr.extend(list(marital_status_dict[marital_status]))

    number_of_adresses = st.slider("No. of unique customer addresses", min_value=0, max_value=30)
    pred_arr.extend([number_of_adresses])

    complain_amt = st.slider("No. of complains from the customer", min_value=0, max_value=5)
    pred_arr.extend([complain_amt])

    order_hike_yoy = st.slider("Increase in customer's order amount from last year", min_value=0, max_value=50)
    pred_arr.extend([order_hike_yoy])

    no_of_coupons_used = st.slider("No. of coupons used by the customer", min_value=0, max_value=30)
    pred_arr.extend([no_of_coupons_used])

    order_count = st.slider("No. of orders?", min_value=0, max_value=30)
    pred_arr.extend([order_count])

    days_since_last_order = st.slider("No. of days since last order?", min_value=0, max_value=100)
    pred_arr.extend([days_since_last_order])

    cashback_amt = st.slider("Cashback amount", min_value=0, max_value=500)
    pred_arr.extend([cashback_amt])


    result=""
    if st.button("Predict"):
        
        # print(len(pred_arr))
        result = predict([pred_arr])

        print("Awaiting result...")
        print(result)
        
        if result[0] == 0:
                st.success('The customer will not churn!', icon="✅")
        else:
            st.error("The customer is likely to churn!")
    if st.button("About"):
        st.text("Built with Streamlit, Best model used: Random Forest!")

main()