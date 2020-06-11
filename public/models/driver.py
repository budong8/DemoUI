#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from selenium.webdriver import Remote
import warnings
from selenium import webdriver


def browser():
    """
    启动浏览器驱动
    :return: 返回浏览器驱动URL
    """
    try:
        warnings.simplefilter('ignore',ResourceWarning)
        host = '127.94.0.1:4444'
        driver = Remote(command_executor='http://' + host + '/wd/hub',
                        desired_capabilities={ 'platform': 'ANY',
                                               'browserName': 'chrome',
                                               'version': "",
                                               'javascriptEnabled': True
                                            }
                        )
        # driver = webdriver.Chrome()
        return driver
    except Exception as msg:
        print("驱动异常-> {0}".format(msg))
