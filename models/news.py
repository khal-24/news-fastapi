from datetime import datetime
from typing import List, Annotated

from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: str = str(datetime.now())
    comment: str


class PieceOfNews(BaseModel):
    id: int
    title: str
    date: str = str(datetime.now())
    body: str
    deleted: bool = False
    comments: List[Comment] = [Comment]
    comments_count: int = 1


class News(BaseModel):
    news: List[PieceOfNews]
    news_count: int = 0


class Comments(BaseModel):
    comments: List[Comment]
    news_count: int = 0
