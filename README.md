# Пример проекта UI автотестов на демо-интернет-магазина "https://www.saucedemo.com/"
> www.saucedemo.com - это набор обучающих страниц по функционалу интернет-магазина.

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

## Покрываемый функционал
- Проверка успешной авторизации в интернет-магазин.
- Проверка авторизации с пустыми полями.
- Проверка авторизации под заблокированным пользователем.
- Проверка авторизации с не корректными данными для авторизации.
- Проверка добавления товара в корзину.
- Проверка удаления товара в корзину.
- Проверка оформления заказа.


## Запуск тестов
#### По умолчанию все тесты запускаются удалённо на Selenoid

### Для локального запуска
1. Склонировать репозиторий ($ git clone [Git repo](https://github.com/Obrams/qa_guru_project_UI))
2. Откройте проект в PyCharm
3. Введите в терминале команду
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

### Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/Ozerov_qa_quru_project_UI)
Нажмите кнопку «Собрать сейчас»
<p><img src="images/screenshot/jenkins_job.png"></p>

Для удалённого запуска API-тестов, в разделе **Сборка**, необходимо добавить шаг по созданию/изменению .env-файла с данными вашей учетной записи сервиса <code>www.saucedemo.com</code>(**username_shop**, **password_shop**, **block_username_shop**, **block_password_shop**, **uncorrected_username_shop**, **uncorrected_password_shop**).

Пример файла <code>.env</code> в [Jenkins](https://jenkins.autotests.cloud/job/Ozerov_qa_quru_project_UI/configure)

<img src="images/screenshot/env.jpg"/>
Примечание данные для авторизации тестовые.

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Отчетность о прохождении тестов в Allure
#### Если тест запускался локально:
Введите в терминале команду 
```
allure serve allure-results
``` 
#### Если тест запускался в Jenkins
Нажмите Allure Report или кликните по иконке отчёта в завершённой сборке
<p><img title="Jenkins_Allure" src="images/screenshot/jenkins_allure.png"></p>

### Примеры отображения тестов
<img title="Allure_Report" src="images/screenshot/Allure Report0.png">
<img title="Allure_Example_Report" src="images/screenshot/Allure Report.png">

#### Так же в отчетах для каждого UI-теста прикрепляется видео
<img src="images/screenshot/video.gif">

### <p><img width="3%" title="Telegram" src="images/logo/tg.png"> Telegram</p>
<p>Настроена отправка отчета в <a href='https://t.me/aqa_report_bot'>Telegram</a></p>
<img title="Telegram_report_screen" src="images/screenshot/telegram.png">