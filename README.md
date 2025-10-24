# AI Satın Alma Analiz Dashboard

Monorepo: FastAPI backend + React (Vite + Tailwind) frontend.

## Başlatma (lokal)

### Backend
1. Python ortamını hazırla ve bağımlılıkları kur:
```
cd backend
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
2. Geliştirme sunucusunu başlat:
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
3. Test: http://localhost:8000/

### Frontend
1. Kurulum ve geliştirme:
```
cd frontend
npm install
npm run dev
```
2. http://localhost:5173 (Vite) veya build sonrası preview: `npm run build && npm run preview`

## Docker ile çalıştırma
```
docker compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

## API Uçları
- POST /upload/ : multipart/form-data (file) ile Excel yükle, özet döner.
- POST /forecast : [{YIL, AY, Tutar, ...}] veri ile aylık tahmin döner (Prophet).
- GET /anomalies : placeholder
- GET /reports : placeholder

## Frontend Sayfalar
- / : Dashboard (örnek grafik placeholder)
- /upload : Excel yükleme ve özet görüntüleme

## Notlar
- Prophet derleme bağımlılıkları için backend Dockerfile içinde build-essential ve atlas kütüphaneleri eklendi.
- Frontend Docker imajı build alır ve `serve` ile dist klasörünü 3000 portunda sunar.
- Gerektiğinde Chart.js/echarts eklenerek grafik içerikleri doldurulabilir.
