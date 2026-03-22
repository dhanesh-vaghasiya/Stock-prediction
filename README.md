# Stock Price Prediction

Full-stack app with Flask backend (LSTM model using TensorFlow/yfinance) and React frontend.

## Production Setup

### Frontend: Vercel
1. Set the frontend root to `frontend` in Vercel.
2. Add an environment variable before build:
	- `REACT_APP_API_URL=https://your-render-service.onrender.com`
3. Build command: `npm run build`
4. Output directory: `build`

### Backend: Render
1. Create a new Web Service from the `backend` folder.
2. Build command: `pip install -r requirements.txt`
3. Start command: `gunicorn app:app`
4. Add an environment variable:
	- `FRONTEND_ORIGIN=https://your-vercel-project.vercel.app`
5. Set the service to use Python 3.10 if Render asks for a runtime.

### Health checks
- Backend health endpoint: `/health`
- Prediction endpoint: `/predict`

## Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

## Frontend
```bash
cd frontend
npm install
npm start
```

