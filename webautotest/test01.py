from time import sleep

from selenium import webdriver

# ��ȡ���������
driver = webdriver.Firefox()

# ��URL
driver.get('http://www.baidu.com')

# ��ͣ3��
sleep(3)

# �ر����������
driver.quit()
