# API test automation project for the "reqres" demo service
> https://reqres.in/ — a sample application for practicing REST requests.

### Tech stack
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
</p>

## Test coverage
### reqres resource
- Create a user
- Update user data
- Successful registration of a new user
- Successful login
- Login with invalid credentials
- Users schema validation
- Get a page of users
- Get a single user
- Get a non-existent user
- Delete a user
- Registration with invalid data

## Running tests


### Local run
1. Clone the repository ($ git clone [Git repo](https://github.com/Obrams/qa_guru_project_API))
2. Open the project in PyCharm
3. Run in the terminal
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

### Running tests in [Jenkins](https://jenkins.autotests.cloud/job/qa_guru_ozerov_project_API/)
Click "Build Now"
<p><img src="images/screenshot/jenkins_job.png"></p>

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure test reports
#### For a local run:
Run in the terminal 
```
allure serve allure-results
``` 
#### For a Jenkins run
Click Allure Report or the report icon in a finished build
<p><img title="Jenkins_Allure" src="images/screenshot/jenkins_allure.png"></p>

### Tests in the report
<img title="Allure_Report" src="images/screenshot/Allure Report0.png">
<img title="Allure_Example_Report" src="images/screenshot/Allure Report.png">

### <p><img width="3%" title="Telegram" src="images/logo/tg.png"> Telegram</p>
<p>Test reports are sent to <a href='https://t.me/aqa_report_bot'>Telegram</a></p>
<img title="Telegram_report_screen" src="images/screenshot/telegram.png">
