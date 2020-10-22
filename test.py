import os

# print("hello world")
# print("谢谢大家")


import pytest
import allure

# @allure.step("步骤1 ==>> 登录用户")
# def step_1(username):
#     print(("步骤1 ==>> 登录用户：{}"))


@allure.severity(allure.severity_level.NORMAL) #设置bug的重要级别
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")    #功能
class TestMubuLogin():
    @allure.story("用例--登录用户") #子功能
    @allure.description("该用例是针对获取用户登录接口的测试") #描述
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址") #标注：可加入Url
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")  #标注：可加入url
    @allure.title("测试数据")
    @pytest.mark.single
    def test_login_mubu(self):
        print("测试")


