from repositories.repository import AbstractRepository


class NewsService:
    def __init__(self, news_repo: AbstractRepository):
        self.news_repo: AbstractRepository = news_repo()

    async def get_piece_of_news(self, id: int):
        piece_of_news = await self.news_repo.get_one(id)
        return piece_of_news

    async def get_news(self):
        news = await self.news_repo.find_all()
        return news
