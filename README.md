# Brain-Tumor-MRI-Image-Classification

## Overview
This project is focused on classifying brain tumor images into four categories:
- **Glioma**
- **Pituitary**
- **Meningioma**
- **No Tumor**

It uses **Explainable AI (XAI) with LIME** to highlight the areas in the image that contribute to the classification decision. The user interface is built using **Streamlit**, allowing users to upload MRI images and get predictions along with an explanation of the model's decision.

## Features
- **Deep Learning Models**: Implemented three models: 
  - **Custom CNN** *(Best performing model, used for LIME explanation)*
  - **VGG16**
- **Explainable AI (XAI)**: Used **LIME (Local Interpretable Model-Agnostic Explanations)** to highlight important regions in the image contributing to classification.
- **Streamlit UI**: Users can upload MRI images and receive a classification along with an explainability heatmap.


## Installation
To run this project locally, follow these steps:

### 1. Clone the repository
```bash
 git clone 
 cd 
```
### 2. Run the Streamlit app
```bash
streamlit 
```

## Model Details
### 1. Custom CNN *(Best performing model)*
- **Architecture**: 4 convolutional layers, batch normalization, dropout, and fully connected layers.
- **Performance**: Achieved the best accuracy among the models tested.
- **Used for LIME explainability**.

### 2. VGG16 
- Pretrained models used for comparison.
- Fine-tuned on the brain tumor dataset.

## Explainability with LIME
LIME (Local Interpretable Model-Agnostic Explanations) is used to visualize which parts of the image influenced the model's decision.

**Example Output:**
- **Original MRI Image**
- **Predicted Class: Glioma**
- **LIME Highlighted Regions** (showing critical areas used for classification)




## Dataset
- The dataset consists of MRI scans categorized into **Glioma, Pituitary, Meningioma, and No Tumor**.
- Data augmentation techniques were applied for better generalization.

## Future Enhancements
- Adding more advanced XAI techniques such as Grad-CAM.
- Deploying the app as a web service.



## Contact  
📧 Email:  
🔗 GitHub: 
