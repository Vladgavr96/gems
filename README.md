Выполняем следующие команды

1 sudo chown -R $USER:$USER .

2  sudo docker-compose run web ./manage.py migrate

3  docker-compose up 

Эндпоинт расположен по адресу ниже
http://0.0.0.0:8000/api/v1/deals/

При отправке