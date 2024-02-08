# import streamlit as st

# def main():
#     st.title("Image Uploader")
#     st.write("Upload two images and see them side by side:")

#     with st.container():
#         col1, col2 = st.columns(2)

#         uploaded_file1 = col1.file_uploader("Choose the first image...", type=["jpg", "jpeg", "png"])
#         if uploaded_file1 is not None:
#             col1.image(uploaded_file1, caption='First Image.', use_column_width=True)

#         uploaded_file2 = col2.file_uploader("Choose the second image...", type=["jpg", "jpeg", "png"])
#         if uploaded_file2 is not None:
#             col2.image(uploaded_file2, caption='Second Image.', use_column_width=True)

# if __name__ == "__main__":
#     main()



# import streamlit as st
# import os

# def main():
#     st.title("Image Display")

#     image_folder = os.path.join(os.path.dirname(__file__), "images")  # Path to the images folder

#     st.write("Displaying images from the 'images' folder:")

#     with st.container():
#         col1, col2 = st.columns(2)

#         image_path1 = os.path.join(image_folder, "image1.jpg")
#         col1.image(image_path1, caption='First Image.', use_column_width=True)

#         image_path2 = os.path.join(image_folder, "image2.jpg")
#         col2.image(image_path2, caption='Second Image.', use_column_width=True)

# if __name__ == "__main__":
#     main()


import streamlit as st
# import os

# def main():
#     st.title("Image Display")

#     # Assuming your Streamlit script is located in a folder named "page" within your project folder
#     # and the "images" folder is located within the project folder
#     image_folder = os.path.join(os.path.dirname(os.path.dirname("Images")), "images")

#     st.write("Displaying images from the 'images' folder:")

#     with st.container():
#         col1, col2 = st.columns(2)

#         # Fetching image paths from the "images" folder
#         image_files = os.listdir(image_folder)

#         # Displaying images
#         for i, image_file in enumerate(image_files):
#             image_path = os.path.join(image_folder, image_file)
#             if os.path.isfile(image_path):
#                 if i % 2 == 0:
#                     col1.image("Images\download.png", caption=image_file, use_column_width=True)
#                 else:
#                     col2.image("Images\download copy.png", caption=image_file, use_column_width=True)

# if __name__ == "__main__":
#     main()

import streamlit as st
import os

def main():
    st.title("Image Display")

    # Assuming your Streamlit script is located in a folder named "page" within your project folder
    # and the "images" folder is located within the project folder
    image_folder = os.path.join(os.path.dirname(os.path.dirname("Images")), "images")

    st.write("Displaying images from the 'images' folder:")

    with st.container():
        col1, empty, col2 = st.columns([1, 1.1, 1])  # Adding an empty column

        # Fetching image paths from the "images" folder
        image_files = os.listdir(image_folder)

        # Displaying images
        for i, image_file in enumerate(image_files):
            image_path = os.path.join(image_folder, image_file)
            if os.path.isfile(image_path):
                if i % 2 == 0:
                    col1.image("Images\download.png", caption="SURAJ KUMAR", use_column_width=True,width=int)
                    col1.write("suraj kumar")
                else:
                    col2.image("Images\download copy.png", caption=image_file, use_column_width=True)

if __name__ == "__main__":
    main()
