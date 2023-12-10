from datetime import datetime
import json
from abc import ABC, abstractmethod
from pathlib import Path

from models.news import News, PieceOfNews, Comments, Comment


class AbstractRepository(ABC):
    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self):
        raise NotImplementedError


class LocalDriveJSONRepository(AbstractRepository):
    model = None
    __news_path = Path('local_drive/news.json').resolve()
    __comment_path = Path('local_drive/comments.json').resolve()

    async def get_one(self, id: int):
        news = self.__get_news(id)
        if news.news:
            news.news = news.news[:1]
            self.__get_comments(news.news)
            piece_of_news = news.news[0]
            del piece_of_news.comments
            return piece_of_news

    async def find_all(self):
        news = self.__get_news(id=False)
        news.news = self.__sort_by_date(news.news)

        self.__get_comments(news.news)

        return news

    def __get_news(self, id):
        with open(self.__news_path, encoding='utf8') as news_file:
            news: News = News(**json.load(news_file))
            news.news = list(filter(lambda x: self.__filter_news(x, id), news.news))
        return news

    def __get_comments(self, news):
        with open(self.__comment_path, encoding='utf8') as comment_file:
            comments = Comments(**json.load(comment_file))
            for piece_of_news in news:
                comments = list(filter(lambda x: x.news_id == piece_of_news.id, comments.comments))
                piece_of_news.comments = self.__sort_by_date(comments)
                piece_of_news.comments_count = len(comments)

    def __filter_news(self, item: PieceOfNews, id):
        if (item.id != id and id) or datetime.fromisoformat(item.date) > datetime.now() or item.deleted:
            return False
        return True

    def __sort_by_date(self, items):
        return sorted(items, key=lambda x: datetime.fromisoformat(x.date))
