"""
����ļ������ã�����ֱ��ͨ������.�������߰���.�����ķ�ʽ��ȡֵ
"""
from selenium.webdriver.common.by import By

"""��������Ϊ��ý��ģ����������"""
# �û���
mp_username = (By.CSS_SELECTOR, "[placeholder='�������ֻ���']")
# ��֤��
mp_code = (By.CSS_SELECTOR, "[placeholder='��֤��']")
# ��¼��ť
mp_login_btn = (By.CSS_SELECTOR, '.el-button--primary')  # .XXX css�е���ѡ����
# �ǳ�
mp_nickname = (By.CSS_SELECTOR, '.user-name')


"""
��С���ܽ᣺
    1��Ԫ��������Ϣͳһ��Ź���__init__.py��
    2����ʹ��cssѡ������λ����ʹ��xpath��λ
    3��cssѡ������[������='����ֵ']Ϊ����ѡ�������������������@���Ρ�[.XXX]Ϊclassѡ������
P17����
"""