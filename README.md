# flea_market
Simple marketplace created in Django.

![alt text](https://github.com/dawmro/flea_market/blob/main/screenshot.PNG?raw=true)

## Setup:
1. Create new virtual env:
``` sh
python -m venv env
```
2. Activate your virtual env:
``` sh
env/Scripts/activate
```
3. Install packages from included requirements.txt:
``` sh
pip install -r .\requirements.txt
```
4. Go into flea_market folder:
``` sh
cd ./flea_market
```
5. Convert models into database schema:
``` sh
python manage.py migrate
```
6. Create admin account:
``` sh
python manage.py createsuperuser
```


## Usage:
1. Start server:
``` sh
python manage.py runserver
```
2. Add categories for items in admin panel:
``` sh
http://127.0.0.1:8000/admin/
```
