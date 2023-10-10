import requests
import allure
from jsonschema.validators import validate

from conftest import open_json_schema, request_api

from allure_commons.types import Severity

service = 'reqres'


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.title('Создание пользователя')
def test_create_user():
    response = request_api(
        service,
        'post',
        url='/api/users',
        data={'name': 'quagurov', 'job': 'student'}
    )
    assert response.status_code == requests.codes.created
    assert response.json()['name'] == 'quagurov'
    assert response.json()['job'] == 'student'


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.title('Обновление данных пользователя')
def test_update_user():
    response = request_api(
        service,
        'put',
        url='/api/users/2',
        data={'name': 'quagurov', 'job': 'best student'}
    )

    assert response.status_code == 200
    assert response.json()['name'] == 'quagurov'
    assert response.json()['job'] == 'best student'


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.title('Успешная регистрация нового пользователя')
def test_register_successful_user():
    response = request_api(
        service,
        'post',
        url='/api/register',
        data={'email': 'eve.holt@reqres.in', 'password': 'pistol'}
    )

    assert response.status_code == 200
    assert response.json()['id'] == 4
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.title('Успешная авторизация')
def test_login_successful_user():
    response = request_api(
        service,
        'post',
        url='/api/login',
        data={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    )

    assert response.status_code == 200
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.title('Авторизация под невалидными данными ')
def test_login_unsuccessful_user():
    response = request_api(
        service,
        'post',
        url='/api/login',
        data={'email': 'peter@klaven'}
    )

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.title('Валидация схемы users')
def test_users_schema():
    schema = open_json_schema('get_users_schema.json')
    response = request_api(
        service,
        'get',
        url='/api/users'
    )
    validate(instance=response.json(), schema=schema)


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Получение информации о странице с пользователями')
def test_users_page_info():
    per_page = 6

    response = request_api(
        service,
        'get',
        url='/api/users',
        params={'per_page': per_page}
    )

    assert response.status_code == 200
    assert response.json()['page'] == 1
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Получение информации о одном пользователе')
def test_check_single_user():
    response = request_api(
        service,
        'get',
        url='/api/users/2'
    )

    assert response.status_code == 200
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert response.json()['data']['first_name'] == 'Janet'
    assert response.json()['data']['last_name'] == 'Weaver'
    assert response.json()['data']['avatar'] == 'https://reqres.in/img/faces/2-image.jpg'
    assert len(response.json()["data"]) == 5
    assert len(response.json()["support"]) == 2


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Получение информации о пользователе, которого нет в системе.')
def test_users_not_found():
    response = request_api(
        service,
        'get',
        url='/api/users/23',
    )

    assert response.status_code == 404


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Удаление данных о пользователе из системы')
def test_delete_user():
    response = request_api(
        service,
        'delete',
        url='/api/users/2'
    )

    assert response.status_code == 204


@allure.feature('Ресурс "Reqres.in"')
@allure.label('owner', 'Nikita')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Регистрация под невалидными данными')
def test_register_unsuccessful_user():
    response = request_api(
        service,
        'post',
        url='/api/register',
        data={'email': 'sydney@fife'}
    )

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
