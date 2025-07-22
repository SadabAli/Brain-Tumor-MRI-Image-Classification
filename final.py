import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import time
import lime
from lime import lime_image
import matplotlib.pyplot as plt
from skimage.segmentation import mark_boundaries

# Load the trained model
model_path = r"C:\Users\alisa\OneDrive\Desktop\Brain-Tumor-MRI-Image-Classification\Brain_timor.h5"
model = load_model(model_path)

# Define the class names
class_names = ["glioma", "meningioma", "no_tumor", "pituitary"]

# Streamlit interface
st.title("Brain Tumor Classification")
st.write("Upload an MRI scan image to classify whether it has a brain tumor.")

# Image uploader
uploaded_file = st.file_uploader("Choose an MRI scan...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Resize the uploaded image for display
    image = image.resize((300, 300))
    st.image(image, caption='Uploaded MRI Scan.', use_column_width=False)
    st.write("Classifying...")

    # Show a spinner while processing
    with st.spinner('Processing...'):
        time.sleep(3)

    # Preprocess the image for model prediction
    image = image.convert("RGB")
    image_resized = image.resize((150, 150))
    image_array = np.expand_dims(np.array(image_resized), axis=0)

    # Predict using the loaded model
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    st.write(f"Prediction: {class_names[predicted_class]}")

    # Additional Analysis Button
    if st.button("Run Additional Analysis"):
        st.write("Running additional analysis...")

        # Initialize LIME Explainer
        explainer = lime_image.LimeImageExplainer()

        # Prediction function for LIME
        def predict_fn(images):
            return model.predict(images)

        # Generate LIME explanation
        explanation = explainer.explain_instance(
            np.array(image_array[0]), 
            predict_fn, 
            top_labels=4, 
            hide_color=0, 
            num_samples=1000
        )

        # Get LIME explanation image and mask
        temp, mask = explanation.get_image_and_mask(
            predicted_class, positive_only=True, num_features=10, hide_rest=False
        )

        # Draw a green border around the regions classified as "No Tumor"
        no_tumor_index = class_names.index("No Tumor")
        if predicted_class == no_tumor_index:
            # Outline "No Tumor" regions in green
            explanation_image = mark_boundaries(temp, mask, color=(0, 1, 0), mode='outer')
           # overlay_message = "Green border indicates 'No Tumor' regions."
        else:
            # Outline only the regions classified as "No Tumor"
            explanation_image = mark_boundaries(temp, mask, color=(0, 1, 0), mode='outer')
            #overlay_message = "Green border indicates 'No Tumor' regions; tumor areas have no border."

        # Resize the LIME explanation image for display
        explanation_image_resized = np.array(Image.fromarray((explanation_image * 255).astype(np.uint8)).resize((300, 300)))

        # Display images in two columns
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption='Uploaded MRI Scan.', use_column_width=False)
        with col2:
            st.image(explanation_image_resized, caption='LIME Explanation with Border.', use_column_width=False)

        # Display overlay message
        #st.markdown(f"<span style='color: red;'>{overlay_message}</span>", unsafe_allow_html=True)
