git clone https://github.com/Nattallliy/VKR.git
cd siteSmail
python manage.py makemigrations 
python manage.py migrate 
python manage.py createsuperuser (создать своего суперпользователя, который на данный момент является администратором, 
для входа в базу данных необходимо набрать http://localhost:8000/admin/ в браузере. Здесь localhost — это имя компьютера)
python manage.py runserver
