from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends, HTTPException

from models.news import News, PieceOfNews
from services.news import NewsService
from dependencies import news_service

app = FastAPI(title='News App')


@app.get('/')
async def get_news(news_service: Annotated[NewsService, Depends(news_service)]) -> News:
    news = await news_service.get_news()
    if not news:
        raise HTTPException(status_code=404, detail="Item not found")
    return news


@app.get('/news/{id}')
async def get_piece_of_news(id: int,
                            news_service: Annotated[NewsService, Depends(news_service)],
                            ) -> PieceOfNews:
    piece_of_news = await news_service.get_piece_of_news(id)
    if not piece_of_news:
        raise HTTPException(status_code=404, detail="Item not found")
    return piece_of_news
