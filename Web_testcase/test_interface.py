import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Interface:
    def test_01(self):
        driver.get('https://www.jd.com')#打开京东网站

    def test_02(driver):
        driver.find_element(By.CLASS_NAME,"link-login").click() #通过class属性定位，实现点击登录

    def test_03(driver):
        driver.find_element(By.LINK_TEXT,"账户登录").click() #通过文本属性定位

    def test_04(driver):
        driver.find_element(By.XPATH,'//input[@placeholder="邮箱/用户名/登录手机"]').send_keys("15239078904") #通过XPATH属性定位,输入账号

    def test_05(driver):
        driver.find_element(By.XPATH,'//input[@placeholder="密码"]').send_keys("123456") #通过XPATH属性定位,输入密码

    def test_06(self):
        driver.find_element(By.XPATH,'//input[text()="登录"]').click() #通过XPATH属性定位,实现点击登录

# #创建夹具
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()#启动浏览器
#     driver.maximize_window()#浏览器最大化



if __name__ == '__main__':
    pytest.main()