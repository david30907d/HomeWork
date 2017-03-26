# PMI of KCM

一個將PMI套用到KCM上的django套件

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need python3 `sudo apt-get update; sudo apt-get install; python3 python3-dev`

### Installing

1. 使用虛擬環境 Use virtualenv is recommended：
  1. `virtualenv venv`
2. 啟動方法 How to activate virtualenv
  1. for Linux：`. venv/bin/activate`
  2. for Windows：`venv\Scripts\activate`
3. 安裝 Install：`pip install PMIofKCM`

## Running & Testing

## Run

1. `settings.py`裏面需要新增`PMIofKCM`這個app：

  - add this:

    ```
    INSTALLED_APPS=[
    ...
    ...
    ...
    'PMIofKCM',
    ]
    ```

2. `urls.py`需要新增下列代碼 把所有 `pmi` 開頭的request都導向到`PMIofKCM`這個app：

  - add this:

    ```
    # pmiOfKcm
    import PMIofKCM.urls
    urlpatterns += [
        url(r'^pmi/', include(PMIofKCM.urls))
    ]
    ```

3. `python manage.py runserver`：即可進入頁面 `127.0.0.1:8000/pmi` 測試 pmi 是否安裝成功。

### Break down into end to end tests

not yet.

### And coding style tests

目前沒有coding style tests...

## Deployment

PMIofKCM is a django-app, so depends on django project.

PMIofKCM 是一般的django插件，所以必須依存於django專案

## Built With

* python3.5
* pymongo

## Versioning

For the versions available, see the [tags on this repository](https://github.com/david30907d/KCM/releases).

## Contributors

* **陳聖軒**
* **張泰瑋** [david](https://github.com/david30907d)

## License

This package use `GPL3.0` License.

## Acknowledgments
