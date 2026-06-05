⚡ Energy Load Forecasting & Smart Grid Optimization System

An AI-powered energy forecasting system using LSTM, XGBoost, and ARIMA models with a modern React frontend. Predict electricity demand, optimize grid performance, and track carbon emissions in real-time.

🚀 Features:
- Multi-model forecasting (LSTM, XGBoost, ARIMA, Ensemble)
- Peak load prediction and grid optimization
- Carbon impact estimation and tracking
- Interactive dashboard with real-time charts
- Dark/Light mode support
- Gemini AI integration for smart insights

🛠️ Tech Stack:
- Backend: FastAPI, Python, Scikit-learn, XGBoost
- Frontend: React, Tailwind CSS, Recharts
- Database: SQLite
- ML Models: Random Forest (CPU-optimized), XGBoost, ARIMA

📊 Use Cases:
- Utility companies for demand planning
- Smart city energy management
- Renewable energy integration
- Carbon footprint reduction

🔧 Installation:
1. Clone the repository
2. Backend: `cd backend && pip install -r requirements.txt && python run.py`
3. Frontend: `cd frontend && npm install && npm run dev`
4. Access: http://localhost:5173

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18.2+-blue.svg)](https://reactjs.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📊 Overview

An end-to-end AI-powered energy forecasting system that predicts electricity demand, optimizes grid performance, and tracks carbon emissions using multiple machine learning models.

![Dashboard Preview](https://via.placeholder.com/800x400?text=Energy+Forecast+Dashboard)

## ✨ Features

### 🤖 Multi-Model Forecasting
- **LSTM** - Deep learning for complex patterns
- **XGBoost** - Gradient boosting for feature-rich predictions  
- **ARIMA** - Statistical time series analysis
- **Ensemble** - Combined model for best accuracy (93.9%)

### 🏭 Grid Optimization
- Peak load prediction and reduction
- Load balancing strategies
- What-if scenario simulation
- Real-time optimization recommendations

### 🌍 Carbon Impact Tracking
- CO2 emission calculations
- Carbon intensity monitoring
- Reduction recommendations
- Offset project tracking

### 📊 Interactive Dashboard
- Real-time energy monitoring
- Interactive charts and graphs
- Dark/Light theme support
- Exportable reports

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | FastAPI, Python 3.10+, SQLAlchemy |
| **ML Models** | Scikit-learn, XGBoost, Statsmodels |
| **Frontend** | React 18, Tailwind CSS, Recharts |
| **Database** | SQLite (development), PostgreSQL (production) |
| **Deployment** | Docker, Nginx |

## 📁 Project Structure
m
## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/energy-forecast-system.git
cd energy-forecast-system

cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py

cd frontend
npm install
npm run dev