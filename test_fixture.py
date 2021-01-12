# encoding = utf-8

import pytest


@pytest.fixture
def conn_db():
    print("完成数据库连接")
    yield
    print('22222')


@pytest.fixture(autouse=True, scope="function")
def login():
    print("登陆操作")
    yield ['zoe', 'mia']
    # yield之后方法相当于teardown操作
    print("登出操作")


# fixture写法一，有参数传递的，记得传参到函数：test_case1(login)。
# def test_case1(login):
#     print(login)
#     print("用例1")

# fixture写法二，缺点：无法使用到setup函数的返回值。需要入参的方法不能使用装饰器
@pytest.mark.usefixtures("login")
def test_case1(login):
    print(login)
    print("用例1")


# autouse开关设置为true，scope为默认"function"，则case2也自动被应用这个fixtrue。
def test_case2():
    print("用例2")


def test_case3(login, conn_db):
    print(login)
    print(conn_db)
    print("用例3")
