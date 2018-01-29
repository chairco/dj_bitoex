# dj_bitoex

記錄與分析過內比特幣交易平台 BitoEx 買賣價資訊

## Getting Started

目前僅支援 Python 3.6 以上版本，Django 為 2.x 所以必須要注意語法以及 build-in function 會有些差異。

支援 pipenv 管理環境，但因為目前 pipenv 還在修正中，所以也可以使用 python 3.x 的虛擬環境與使用 pip 安裝套件。


### Requirements
Git 1.8+
Python 3.6+

### Install Dependencies

clone project

```python
>>> git clone https://github.com/chairco/dj_bitoex.git
>>> cd dj_bitoex
```

use pip

```python
>>> pip install -r requirements.txt
```

use pipenv

```python
>>> pipenv install
```


## Get Ready for Development

cd into the src directory and migrate database.

On this project we suggest using PostgreSQL db because Django-Q is our default schedule and task workflow manager and it's some issue if using sqlite to be db. So make sure you have set up postgreSQL already.


### Set up Local Environment Variables and Database

Settings are stored in environment variables via [django-environ](http://django-environ.readthedocs.org/en/latest/). The quickest way to start is to copy local.sample.env into local.env: 

```
cp src/src/settings/local_sample.env src/src/settings/local.env
```

Then edit the SECRET_KEY line in local.env, full SECRET_KEY= into any Django Secret Key value. An example:

```shell
$ export SECRET_KEY=python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))'

# echo $SECRET_KEY
twvg)o_=u&@6^*cbi9nfswwh=(&hd$bhxh9iq&h-kn-pff0&&3.6

$ sed -ri 's/^SECRET_KEY=/SECRET_KEY="'$SECRET_KEY'"/' local.env
```


### Create necessary folder and Migrate database

After that, start run the migration

```
$ cd src
$ mkdir -p logs
$ mkdir -p static
$ python manage.py migrate
```

Now you’re all set!


## Run the Development Server

```
python manage.py runserver
```