import streamlit as st
import pandas as pd
import os

def main():
    st.title("Upload and Display CSV")

    # D drive project folder path
    project_folder = "D:/FinalProject"

    # Create the folder if it doesn't exist
    if not os.path.exists(project_folder):
        os.makedirs(project_folder)

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a CSV file")

    if uploaded_file is not None:
        # Save the uploaded file to the project folder
        file_path = os.path.join(project_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")

        # Read the uploaded CSV file
        df = pd.read_csv(file_path)

        # Display the DataFrame
        st.write(df)

if __name__ == "__main__":
    main()
