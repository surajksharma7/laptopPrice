import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os


def process_input(raw_data, training_columns):
    processed_data = raw_data.copy()
    for col in training_columns:
        if col not in processed_data:
            processed_data[col] = 0 
    processed_data = pd.get_dummies(processed_data, columns=training_columns)
    processed_data = processed_data[training_columns]
    return processed_data

def read_pkl_file(file_path):
    data = pd.read_pickle("model\model.pkl")
    return data

def main():
    st.set_page_config("Price Prediction", "🏘️", "centered", "expanded")
    st_msg = st.container()

    with st_msg:
        st.title("💻 Laptop Price Prediction 💻")

        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, "model", "model.pkl")

        try:
            data = read_pkl_file(file_path)
            all_brands = ['HP']
            all_processors = ['13th Gen Intel Core i3 1315U']
            all_cpu_comb = ['20 Threads']
            all_gpus = ['4GB AMD Radeon RX 5600M ']
            all_os = ['Mac 10.15.3 OS']
            ramopt = [1,2,4,6,8,12,16,32,64,128]
            ramtypeopt = ['DDR4','LPDDR4x', 'Unified', 'DDR4-', 'LPDDR5x', 'DDR']
            romtype = ["HDD","SDD"]
            with st.form("user_input_form"):
                col1, col2 = st.columns(2)
                with col1:
                    brand = st.selectbox("Select Brand", all_brands)
                    spec_rating = st.number_input("Enter Spec Rating", min_value=0, max_value=100, value=40)
                    processor = st.selectbox("Select Processor", all_processors)
                    CPU = st.selectbox("Enter CPU Cores + Threads",all_cpu_comb)
                    Ram = st.selectbox("Enter RAM (GB)",ramopt)
                    OS = st.selectbox("Select OS", all_os)
                    warranty = st.text_input("Warranty Period", "1.0")

                with col2:
                    Ram_type = st.selectbox("Enter RAM Type", ramtypeopt)
                    ROM = st.number_input("Enter Storage (GB)", min_value=1, value=256)
                    ROM_type = st.selectbox("Select Storage Type",romtype)
                    GPU = st.selectbox("Select GPU", all_gpus)
                    display_size = st.text_input("Enter Display Size", "15.6")
                    resolution_width = st.text_input("Enter Resolution Width", "1920")
                    resolution_height = st.text_input("Enter Resolution Height", "1080")
                    

                submit_button = st.form_submit_button("Predict")

            if submit_button:
                user_data = {
                    'brand': [brand],
                    'spec_rating': [spec_rating],
                    'processor': [processor],
                    'CPU': [CPU],
                    'Ram': [Ram],
                    'Ram_type': [Ram_type],
                    'ROM': [ROM],
                    'ROM_type': [ROM_type],
                    'GPU': [GPU],
                    'display_size': [display_size],
                    'resolution_width': [resolution_width],
                    'resolution_height': [resolution_height],
                    'OS': [OS],
                    'warranty': [warranty]
                }

                user_df = pd.DataFrame(user_data)
                enc = LabelEncoder()
                categorical_columns = ['brand', 'processor', 'CPU', 'Ram_type', 'ROM_type', 'GPU', 'OS']
                for column in categorical_columns:
                    user_df[column] = enc.fit_transform(user_df[column])
                prediction = data.predict(user_df)
                st.subheader("Prediction Result")
                st.markdown(f'<div class="prediction">{prediction}</div>', unsafe_allow_html=True)
                st.markdown(
                  """
                  <style>
                    .prediction {
                      font-size: 24px;
                      font-weight: bold;
                      color: green;
                    }
                    .stForm {
                      height: 500px; /* Adjust the height as needed */
                    }
                  </style>
                  """,
                  unsafe_allow_html=True
                )

        except FileNotFoundError:
            st.error(f"File not found: {file_path}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
