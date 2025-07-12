# Brain Tumor Classification using CNN & XAI (LIME)

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
  - **VGG19**
- **Explainable AI (XAI)**: Used **LIME (Local Interpretable Model-Agnostic Explanations)** to highlight important regions in the image contributing to classification.
- **Streamlit UI**: Users can upload MRI images and receive a classification along with an explainability heatmap.

## Demo Video
🎥 [Watch the Demo](https://github.com/GaneshPrasadSahoo/Brain-Tumor-Classification-using-CNN-XAI/raw/main/braintumor.mp4)

## Installation
To run this project locally, follow these steps:

### 1. Clone the repository
```bash
 git clone https://github.com/GaneshPrasadSahoo/Brain-Tumor-Classification-using-CNN-XAI.git
 cd Brain-Tumor-Classification-using-CNN-XAI
```
### 2. Run the Streamlit app
```bash
streamlit run app.py
```

## Model Details
### 1. Custom CNN *(Best performing model)*
- **Architecture**: 4 convolutional layers, batch normalization, dropout, and fully connected layers.
- **Performance**: Achieved the best accuracy among the models tested.
- **Used for LIME explainability**.

### 2. VGG16 & VGG19
- Pretrained models used for comparison.
- Fine-tuned on the brain tumor dataset.

## Explainability with LIME
LIME (Local Interpretable Model-Agnostic Explanations) is used to visualize which parts of the image influenced the model's decision.

**Example Output:**
- **Original MRI Image**
- **Predicted Class: Glioma**
- **LIME Highlighted Regions** (showing critical areas used for classification)

## Project Structure
```
📁 Brain-Tumor-Classification-using-CNN-XAI
│── 📁 models            # Contains trained models
│── 📁 datasets          # Contains dataset (if applicable)
│── 📁 static            # Stores images and UI assets
│── 📜 final.py            # Main Streamlit UI script& LIME   XAI
│── 📜 README.md         # Project documentation
```

## Dataset
- The dataset consists of MRI scans categorized into **Glioma, Pituitary, Meningioma, and No Tumor**.
- Data augmentation techniques were applied for better generalization.

## Future Enhancements
- Adding more advanced XAI techniques such as Grad-CAM.
- Deploying the app as a web service.



## Contact
**Ganesh Prasad Sahoo**  
📧 Email: [ganeshprasadsahoo348@gmail.com]  
🔗 GitHub: [GaneshPrasadSahoo](https://github.com/GaneshPrasadSahoo)
