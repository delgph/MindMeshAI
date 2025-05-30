#!/bin/zsh
echo "Building Next.js frontend..."
npm install
npm run build

echo "Starting Next.js frontend on port 3000..."
npm start &

cd ..

echo "Activating Python virtual environment..."
source venv/bin/activate

echo "Starting FastAPI backend on port 8000..."
gunicorn server.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000