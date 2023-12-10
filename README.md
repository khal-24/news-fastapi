### Реализация

* Приложение реализовано с помощью паттерна репозитрий
* Чтение данных происходит синхронно напрямую из файлов .json
* Асинхронная запись методов нужна для сохранения возможности замены реализации репозитория на другой (СУБД с асинхронным драйвером)



### Запуск

Находясь в корневой директории, запустить

1. ` docker build . -t  news-fastapi`
2. `docker run -p 8000:8000 news-fastapi`

Обращение по адресу 127.0.0.1

GET "/" - возвращает список новостей следующего формата.

```javascript
{
 "news": [
    {
      "id": 1,
      "title": "news_1",
      "date": "2019-01-01T20:56:35",
      "body": "The news",
      "deleted": false,
      "comments_count": 1,
    },
 ],
 "news_count": 1
}
```

GET "/news/{id}" - возвращает новость по ее id.
```javascript
{
 "id": 1,
 "title": "news_1",
 "date": "2019-01-01T20:56:35",
 "body": "The news",
 "deleted": false,
 "comments": [
     {
     "id": 1,
     "news_id": 1,
     "title": "comment_1",
     "date": "2019-01-02T21:58:25",
     "comment": "Comment",
     },
 ],
 "comments_count": 1
}
```