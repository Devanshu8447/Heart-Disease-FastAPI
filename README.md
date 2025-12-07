# Heart Disease Prediction API

A production-ready FastAPI for predicting heart disease risk using machine learning. This application provides real-time heart disease predictions through a RESTful interface, complete with patient data management and an interactive frontend for easy testing and visualization.

**Key Capabilities:**
- 🔬 **ML-Powered Predictions**: Accurate heart disease risk assessment using trained models
- 🌐 **RESTful API**: Easy integration with any application or service
- 💾 **Patient Data Management**: Store and retrieve patient records with predictions
- 🖥️ **Interactive Frontend**: User-friendly web interface for testing predictions
- 🐳 **Docker Ready**: Containerized deployment for seamless scaling

## 🌟 Features

- **Machine Learning Model**: Pre-trained model for heart disease prediction based on clinical parameters
- **RESTful API Endpoints**: Well-documented API for seamless integration
- **Patient Database**: JSON-based storage for patient records and prediction history
- **Interactive Frontend**: Streamlit-based UI for easy data input and visualization
- **Input Validation**: Schema validation to ensure data integrity
- **Docker Support**: Containerized application for easy deployment
- **Modular Architecture**: Clean separation of concerns with organized folder structure

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- pip package manager

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/Devanshu8447/Heart-Disease-FlaskAPI.git
   cd Heart-Disease-FlaskAPI
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Run the Flask API**
```bash
   python app.py
```
   The API will be available at `http://localhost:5000`

4. **Run the Frontend (Optional)**
```bash
   streamlit run frontend.py
```
   The frontend will be available at `http://localhost:8501`

### Docker Deployment

1. **Build the Docker image**
```bash
   docker build -t heart-disease-api .
```

2. **Run the container**
```bash
   docker run -p 5000:5000 heart-disease-api
```

3. **Access the API**
   Navigate to `http://localhost:5000`

## 📖 API Usage

### Predict Heart Disease

**Endpoint:** `POST /predict`

**Request Body:**
```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

**Response:**
```json
{
  "prediction": 1,
  "probability": 0.87,
  "risk_level": "High",
  "patient_id": "12345"
}
```

### Get Patient Records

**Endpoint:** `GET /patients`

**Response:**
```json
{
  "patients": [
    {
      "patient_id": "12345",
      "timestamp": "2024-12-07T10:30:00",
      "prediction": 1,
      "risk_level": "High"
    }
  ]
}
```

### Get Single Patient

**Endpoint:** `GET /patients/<patient_id>`

## 🏗️ Project Structure
```
Heart-Disease-FastAPI/
├── api/                        # API route handlers
│   └── routes.py              # Endpoint definitions
├── config/                     # Configuration files
│   └── config.py              # App configuration
├── model/                      # ML model files
│   └── predictor.py           # Model loading and prediction logic
├── schema/                     # Data validation schemas
│   └── validation.py          # Input validation
├── app.py                      # Main Flask application
├── frontend.py                 # Streamlit frontend
├── model.pkl                   # Trained ML model
├── patients.json               # Patient database
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

## 🔧 Technologies Used

- **Scikit-learn**: Machine learning model training and inference
- **Streamlit**: Interactive frontend development
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Docker**: Containerization
- **Python**: Core programming language

## 📊 Model Features

The model uses the following clinical parameters for prediction:

1. **age**: Age of the patient
2. **sex**: Gender (1 = male, 0 = female)
3. **cp**: Chest pain type (0-3)
4. **trestbps**: Resting blood pressure (mm Hg)
5. **chol**: Serum cholesterol (mg/dl)
6. **fbs**: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
7. **restecg**: Resting ECG results (0-2)
8. **thalach**: Maximum heart rate achieved
9. **exang**: Exercise-induced angina (1 = yes, 0 = no)
10. **oldpeak**: ST depression induced by exercise
11. **slope**: Slope of peak exercise ST segment (0-2)
12. **ca**: Number of major vessels colored by fluoroscopy (0-3)
13. **thal**: Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)

## 📝 How It Works

1. **Data Input**: Patient clinical data is submitted via API or frontend
2. **Validation**: Input data is validated against predefined schemas
3. **Preprocessing**: Data is preprocessed to match model requirements
4. **Prediction**: Machine learning model generates risk prediction
5. **Storage**: Patient data and predictions are stored in JSON database
6. **Response**: Prediction results with risk level are returned

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions regarding medical conditions.

## 🐛 Known Issues

- JSON database is suitable for development; consider using a proper database for production
- Model performance depends on the quality and diversity of training data
- API currently doesn't implement authentication/authorization

## 🔮 Future Enhancements

- [ ] Add user authentication and authorization
- [ ] Implement PostgreSQL/MongoDB for production database
- [ ] Add model retraining pipeline
- [ ] Add unit and integration tests
- [ ] Implement logging and monitoring
- [ ] Add support for batch predictions
- [ ] Create model explanation/interpretability features
- [ ] Add data visualization dashboards
- [ ] Implement CI/CD pipeline

## 📧 Contact

**Devanshu** - [@Devanshu8447](https://github.com/Devanshu8447)

Project Link: [https://github.com/Devanshu8447/Heart-Disease-FlaskAPI](https://github.com/Devanshu8447/Heart-Disease-FlaskAPI)

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Heart Disease dataset
- Scikit-learn community for excellent ML tools
- Flask and Streamlit communities for their frameworks
- The open-source community

---

⭐ If you find this project useful, please consider giving it a star!
