from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # ��ʼ��
    def __init__(self, driver):
        """���driver"""
        self.driver = driver

    # ���� ������װ locһ���Ǹ��б����Ԫ��
    def base_find(self, loc, timeout=30, poll=0.5):
        """

        :param loc: ��ʽΪ�б��Ԫ�飬���ݣ�Ԫ�ض�λ��Ϣʹ��By��
        :param timeout: ����Ԫ�س�ʱʱ�䣬Ĭ��30��
        :param poll: ����Ԫ�ص�Ƶ�� Ĭ��Ϊ0.5��
        :return: Ԫ��
        """
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))  # ��������
        """
        �������ͣ�
            loc ��ΪԪ����б�*locΪ���==loc[0],loc[1]�� 
            lambda x: x.find_element(*loc)  �� ����������xΪdriver
        
        """

    # ���� ������װ
    def base_input(self, loc, value):
        """

        :param loc: Ԫ�صĶ�λ��Ϣ
        :param value: Ҫ�����ֵ
        """
        # 1����ȡԪ��
        el = self.base_find(loc)

        # 2����ղ���
        el.clear()

        # 3���������
        el.send_keys(value)

    # ��� ������װ
    def base_click(self, loc):
        """

        :param loc: Ԫ�ض�λ��Ϣ
        """
        # 1����ȡԪ��
        self.base_find(loc).click()
        # 2�������ť

    # ��ȡ Ԫ���ı�
    def base_get_text(self, loc):
        """

        :param loc: Ԫ�ض�λ��Ϣ
        :return: ����Ԫ�ص��ı�ֵ
        """
        return self.base_find(loc).text


"""
baseģ������������
    ģ������д��base.py
    ������д�����շ巽ʽ��ģ���������������»���ȥ���»���
    ��������д��base+�»���+����+[����] ����base_input��
"""