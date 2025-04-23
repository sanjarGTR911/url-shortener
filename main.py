from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Временное хранилище сокращённых URL
url_store = {}

# Модель запроса
class URLRequest(BaseModel):
    url: str

# 1. Сократить URL
@app.post("/", status_code=201)
async def shorten_url(request: URLRequest):
    original_url = request.url
    url_id = hashlib.md5(original_url.encode()).hexdigest()[:6]
    url_store[url_id] = original_url
    return {"short_url_id": url_id}

# 2. Перенаправление по сокращённому URL на оригинальный
@app.get("/{short_id}")
async def redirect_url(short_id: str):
    original_url = url_store.get(short_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL не найден")
    return RedirectResponse(url=original_url, status_code=307)

# 3. Пример асинхронного сервиса
@app.get("/external-api")
async def get_async_data():
    return {"message": "Это асинхронный endpoint!"}
