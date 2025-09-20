
# Face Mask Deection
This project implements a **Face Mask Detection System** using **YOLO** for real-time detection. It includes data preprocessing, model training, live detection, and a web interface built with Flask.

## 📌 Features
✅ Computer vision and Tensorflow  
🔥 Trained on kaggle dataset 
💡 Uses ONNX for optimized inference  
🎯 High accuracy prediction  

## **Project Structure**
```
Face-Mask-Detection/
Research/
│   ├── 01.data_load.ipynb
│   ├── 02.data_preprocesing.ipynb
│   ├── 03.train_and_evaluation.ipynb
│   ├── Face Mask Detection Full Notebook.ipynb
│   ├── __init__.py
│   ├── data.yaml
│
best_model/
│   ├── best.onnx
│
│── config/
│   ├── config.yaml
│
│── params/
│   ├── params.yaml
│
│── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_load.py
│   │   ├── data_preprocessing.py
│   │   ├── train_model.py
│   │
│   ├── constant/
│   │   ├── __init__.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── Live_detection.py
│   │   ├── prediction.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── exception.py
│   │   ├── logger.py
│
│── static/
│   ├── results/
│   ├── uploads/
│   ├── style.css
│
│── templates/
│   ├── index.html
│
│── test_result/
│   ├── results/  # Stores test results
│
│── .gitignore
│── LICENSE
│── README.md
│── app.py  # Main entry point for Flask or FastAPI application
│── data.yaml  # Data configuration file
│── dirManager.py  # Script for managing directories and file operations
│── render.yaml  # Render deployment configuration
│── requirements.txt  # Python dependencies
│── setup.py  # Installation setup
│── yolo11n.pt  # YOLO model weights
```
## Dataset link 

```bash
https://www.kaggle.com/datasets/andrewmvd/face-mask-detection
```
# Describe the project
## Dataset deatils:
### About Dataset
Masks play a crucial role in protecting the health of individuals against respiratory diseases, as is one of the few precautions available for COVID-19 in the absence of immunization. With this dataset, it is possible to create a model to detect people wearing masks, not wearing them, or wearing masks improperly.
This dataset contains 853 images belonging to the 3 classes, as well as their bounding boxes in the PASCAL VOC format.
The classes are:

    With mask
    Without mask
    Mask worn incorrectly

#### Dataset dstribution:
we split our dataset in two set.Such as:

       Train dataset
       Validation dataset
       

Train dataset contained 0.80(80% of the entrire dataset)

Validation dataset contained 0.20(20% of the entire dataset)




## preprocessesor 
    Normalization
    Augmentation
## kaggle notebook link
```bash 
https://www.kaggle.com/code/azizashfak/face-mask-detection-full-notebook
```

## Installation
1. Clone the repository:
   ```bash
   git clone <https://github.com/aziz-ashfak/Face-Mask-Detection.git>
   ```
2. Navigate to the project directory:
   ```bash
   cd <Face-Mask-Detection>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Usage
Run the main application script:
```bash
python app.py
   ```

## use cloud servce 
```bash 
link : www.render.com
```
## Use Face-Mask-Detection web-service link

```bash
 https://face-mask-detection.onrender.com
```
## Contributing
If you would like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the [LICENSE] file included in the repository.

## Author

👤 **Aziz Ashfak**  
📧 Email: [azizashfak@gmail.com](mailto:azizashfak@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/aziz-ashfak](https://www.linkedin.com/in/aziz-ashfak1/)  
🐙 GitHub: [github.com/aziz-ashfak](https://github.com/aziz-ashfak/) 
# Acknowledgement 
![Python](https://img.shields.io/badge/Python-3.10%2B-blue) 
![Tenssorflow](https://img.shields.io/badge/PASCAL-VOC%20-orange)
![Tenssorflow](https://img.shields.io/badge/Tenssorflow%20-orange)
![Computer Vision](https://img.shields.io/badge/Computer%20Vison-YOLOv11-red)
![Computer Vision](https://img.shields.io/badge/Opencv%20-ImageProcessing-red)
![Flask](https://img.shields.io/badge/Flask-Web%20App-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
---

## Motivation

In the wake of the COVID-19 pandemic, wearing face masks became a crucial preventive measure to limit the spread of the virus. However, ensuring proper mask usage in public spaces remains a challenge. This project aims to leverage deep learning and computer vision to create an end-to-end face mask detection system that can accurately identify whether a person is wearing a mask correctly, wearing it incorrectly, or not wearing one at all.

By integrating YOLO for real-time detection, Flask for web deployment, and ONNX for optimized model inference, this project provides a fast, reliable, and scalable solution for monitoring mask compliance. The goal is to contribute towards public health safety by automating mask detection in various environments such as workplaces, malls, and public transport systems. 

This repository documents the complete pipeline, from data collection and preprocessing to model training, evaluation, and deployment, making it a valuable resource for those interested in AI-driven computer vision applications. 

## problem 
I deploy this project in render cloud, which is free. The render cannot load  to run the webcam and some time stuck in internal server error . So if you want to  run my web service, please! run it locally by cloning my repo.
