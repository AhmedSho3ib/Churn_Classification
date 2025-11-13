# Customer Churn Prediction

A production-ready application for predicting customer churn using Machine Learning models (Random Forest and XGBoost). Available as both a FastAPI REST API and an interactive Streamlit web application.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

Deployment Link : https://churnclassification1.streamlit.app/
API_Key = 3bfb7a2dac4d604e5174b3f416f79cfa

## Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Streamlit Web App](#streamlit-web-app)
- [FastAPI REST API](#fastapi-rest-api)
- [API Documentation](#-api-documentation)
- [Streamlit Deployment](#-streamlit-deployment)
- [Docker Deployment](#-docker-deployment)
- [Model Training](#-model-training)
- [Testing](#-testing)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## Features

- **Interactive Web App** - User-friendly Streamlit interface for predictions
- **High-Performance API** - FastAPI REST API for programmatic access
- **Dual Model Support** - Random Forest and XGBoost models
- **API Key Authentication** - Secure access control
- **Docker Ready** - Containerized deployment
- **Interactive Documentation** - Auto-generated Swagger UI for API
- **Fast Inference** - Optimized prediction pipeline
- **CORS Enabled** - Cross-origin resource sharing support
- **Preprocessing Pipeline** - Automated data preprocessing

---

## Project Structure

```bash
customer-churn-prediction/
│
├── .env.example                  # Example environment variables
├── .gitignore                    # Git ignore file
├── Dockerfile                    # Docker configuration
├── docker-compose.yml            # Docker Compose configuration
├── main.py                       # FastAPI application entry point
├── streamlit_app.py                        # Streamlit application
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── test.ipynb                    # API testing notebook
├── .codegpt/                     # CodeGPT configuration
├── .vscode/                      # VS Code settings
│   └── settings.json
├── dataset/                      # Training data
│   └── churn-data.csv           # Customer churn dataset
├── models/                       # Trained models
│   ├── forest_tuned.pkl         # Random Forest model
│   ├── preprocessor.pkl         # Data preprocessor
│   └── xgb-tuned.pkl            # XGBoost model
├── notebooks/                    # Jupyter notebooks
│   ├── main_notebook.ipynb      # Model training notebook
│   └── secrets_key.ipynb        # API key generation
└── utils/                        # Utility modules
    ├── __init__.py              # Package initializer
    ├── config.py                # Configuration settings
    ├── CustomerData.py          # Data model/schema
    └── inference.py             # Prediction logic
```

---

## Prerequisites

- **Python**: 3.11 or higher
- **pip**: Latest version
- **Docker**: (Optional) For containerized deployment
- **Git**: For version control

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AhmedSho3ib/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your configuration
# Use a text editor to add your SECRET_KEY_TOKEN
```

---

## Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Application Settings
APP_NAME=Customer Churn Prediction API
VERSION=1.0.0

# Security
SECRET_KEY_TOKEN=your-secure-api-key-here

# Model Paths (optional - defaults in config.py)
FOREST_MODEL_PATH=models/forest_tuned.pkl
XGBOOST_MODEL_PATH=models/xgb-tuned.pkl
PREPROCESSOR_PATH=models/preprocessor.pkl

# Server Settings (optional)
HOST=0.0.0.0
PORT=8000
RELOAD=False
```

### Streamlit Configuration

Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
headless = true
port = 8501
```

Create `.streamlit/secrets.toml` (local only - don't commit):

```toml
SECRET_KEY_TOKEN = "your-secure-api-key-here"
```

---

## Usage

You can run the application in two ways:

### Streamlit Web App

The easiest way to interact with the models through a user-friendly interface.

#### Start the Streamlit App

```bash
streamlit run app.py
```

#### Access the Application

- **Streamlit App**: http://localhost:8501

#### Features

- Interactive form for customer data input
- Easy model selection (Random Forest / XGBoost)
- Visual prediction results
- Secure login with API key
- Responsive design

---

### FastAPI REST API

For programmatic access and integration with other systems.

#### Start the API Server

```bash
# Development mode (with auto-reload)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

#### Access the Application

- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

---

## API Documentation

### Authentication

All prediction endpoints require API key authentication via header:

```http
X-API-Key: your-api-key-here
```

### Endpoints

#### 1. **Health Check**

```http
GET /
```

**Response:**
```json
{
  "message": "Welcome to Customer Churn Prediction API v1.0.0"
}
```

---

#### 2. **Random Forest Prediction**

```http
POST /predict/forest
```

**Headers:**
```http
X-API-Key: your-api-key-here
Content-Type: application/json
```

**Request Body:**
```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Male",
  "Age": 35,
  "Tenure": 5,
  "Balance": 125000.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000.0
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.15,
  "model": "Random Forest"
}
```

---

#### 3. **XGBoost Prediction**

```http
POST /predict/xgboost
```

**Headers:**
```http
X-API-Key: your-api-key-here
Content-Type: application/json
```

**Request Body:** Same as Random Forest

**Response:** Same structure as Random Forest

---

### Example Usage

#### cURL

```bash
curl -X POST "http://localhost:8000/predict/forest" \
  -H "X-API-Key: your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "CreditScore": 650,
    "Geography": "France",
    "Gender": "Male",
    "Age": 35,
    "Tenure": 5,
    "Balance": 125000.0,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 50000.0
  }'
```

#### Python

```python
import requests

url = "http://localhost:8000/predict/forest"
headers = {
    "X-API-Key": "your-api-key-here",
    "Content-Type": "application/json"
}
data = {
    "CreditScore": 650,
    "Geography": "France",
    "Gender": "Male",
    "Age": 35,
    "Tenure": 5,
    "Balance": 125000.0,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 50000.0
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

---

## Streamlit Deployment

### Deploy on Streamlit Community Cloud

#### 1. Prepare Your Repository

Ensure these files are in your repository:
- `app.py` - Your Streamlit application
- `requirements.txt` - All dependencies including `streamlit`
- `.streamlit/config.toml` - Streamlit configuration
- `models/` - Your trained models

**Important:** Add to `.gitignore`:
```
.streamlit/secrets.toml
.env
```

#### 2. Push to GitHub

```bash
git add .
git commit -m "Add Streamlit app"
git push origin main
```

#### 3. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repository
5. Set main file path: `app.py`
6. Click **"Advanced settings"**
7. Add your secrets in the Secrets section:
   ```toml
   SECRET_KEY_TOKEN = "your-actual-secret-key"
   ```
8. Click **"Deploy"**

Your app will be live at: `https://your-app-name.streamlit.app`

#### 4. Handling Large Model Files

If your model files are > 100MB, use **Git LFS**:

```bash
# Install Git LFS
git lfs install

# Track your model files
git lfs track "*.pkl"
git lfs track "*.joblib"

# Add and commit
git add .gitattributes
git add models/
git commit -m "Add models with Git LFS"
git push
```

---

## Docker Deployment

### Docker for Streamlit

**Dockerfile.streamlit:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Build and Run:**
```bash
docker build -f Dockerfile.streamlit -t churn-streamlit .
docker run -p 8501:8501 --env-file .env churn-streamlit
```

### Docker for FastAPI

```bash
# Build the image
docker build -t churn-prediction-api .

# Run the container
docker run -d \
  -p 8000:8000 \
  --name churn-api \
  --env-file .env \
  churn-prediction-api
```

### Using Docker Compose (Run Both)

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - ./models:/app/models

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile.streamlit
    ports:
      - "8501:8501"
    env_file:
      - .env
    volumes:
      - ./models:/app/models
    depends_on:
      - api
```

**Run both services:**
```bash
docker-compose up -d
```

---

## Model Training

The models are pre-trained and stored in the `models/` directory. To retrain:

### 1. Open Training Notebook

```bash
jupyter notebook notebooks/main_notebook.ipynb
```

### 2. Follow the Notebook Steps

- Data loading and exploration
- Feature engineering
- Model training and tuning
- Model evaluation
- Model export

### 3. Update Models

Replace the files in the `models/` directory with newly trained models:
- `forest_tuned.pkl`
- `xgb-tuned.pkl`
- `preprocessor.pkl`

---

## Testing

### Interactive Testing with Streamlit

Simply run the Streamlit app and use the web interface:

```bash
streamlit run app.py
```

### API Testing with Jupyter

Open `test.ipynb` to test the API interactively:

```bash
jupyter notebook test.ipynb
```

### Manual API Testing

Use the Swagger UI at http://localhost:8000/docs to test endpoints interactively.

---

## Security

### Best Practices

1. **Never commit secrets** - Keep `.env` and `.streamlit/secrets.toml` out of version control
2. **Use strong API keys** - Generate with `secrets.token_urlsafe(32)`
3. **Enable HTTPS** - Use reverse proxy (Nginx/Caddy) in production
4. **Rate limiting** - Implement rate limiting for production
5. **Input validation** - Both FastAPI and Streamlit handle validation
6. **Keep dependencies updated** - Regularly update packages

### Production Checklist

- [ ] Change default SECRET_KEY_TOKEN
- [ ] Add secrets to Streamlit Cloud
- [ ] Disable debug mode
- [ ] Set up HTTPS/SSL
- [ ] Implement rate limiting
- [ ] Add monitoring and logging
- [ ] Set up backup for models
- [ ] Configure firewall rules

---

## Troubleshooting

### Common Issues

#### 1. **Streamlit App Not Loading Models**

```bash
# Solution: Verify model files exist
ls models/

# Check file paths in utils/config.py
```

#### 2. **Port Already in Use**

```bash
# Streamlit
streamlit run app.py --server.port 8502

# FastAPI
uvicorn main:app --port 8001
```

#### 3. **Secrets Not Working in Streamlit**

```bash
# Verify secrets file exists
cat .streamlit/secrets.toml

# Or use environment variables
export SECRET_KEY_TOKEN="your-key"
streamlit run app.py
```

#### 4. **Module Not Found Error**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### 5. **Docker Container Won't Start**

```bash
# Check logs
docker logs churn-api

# Rebuild
docker-compose down
docker-compose up --build -d
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Write tests for new features
- Update documentation

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Authors

- **Ahmed Shoaib** - *Initial work* - [GitHub](https://github.com/AhmedSho3ib)

---

## Acknowledgments

- FastAPI framework by Sebastián Ramírez
- Streamlit for the amazing web framework
- Scikit-learn and XGBoost teams
- Open source community

---

**Made With Love by Eng. Ahmed Shoaib**
