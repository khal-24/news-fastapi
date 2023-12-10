from repositories.news import NewsRepository
from services.news import NewsService


def news_service():
    return NewsService(NewsRepository)
