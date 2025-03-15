
## **Project Structure**
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
