from interactions.selenium_driver import SeleniumDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.custom_logger import CustomLogger
from utilities.verify import Verify
from basic_map import Basic_login


class TestBasicLogin:
	driver = None
	login = None
	sd = None
	verify = None
	username = 'gocelax227@loongwin.com'
	c_password = 'hackaTon2023!'
	i_password = c_password + '$'

	@classmethod
	def setup_class(cls):
		service = Service(executable_path='C://Users//swuser//PycharmProjects//TemplateProject9//chromedriver.exe')
		cls.driver = webdriver.Chrome(service=service)
		cls.logger = CustomLogger('template test', 'logs')
		cls.sd = SeleniumDriver(driver=cls.driver, logger=cls.logger)
		cls.driver.get(https://profile.w3schools.com/)
		cls.login = Basic_login(cls.sd)
		cls.verify = Verify(cls.sd)
		cls.logger.debug('setup')

	def test1(self):
		# incorrect credentials check
		self.sd.clear_input_field(element=self.login.email_text())
		self.sd.send_keys(element=self.login.email_text(), data=self.username)
		self.sd.clear_input_field(element=self.login.current_password_password())
		self.sd.send_keys(element=self.login.current_password_password(), data=self.i_password)
		self.sd.element_click(element=self.login.login_btn())
		self.sd.wait(10)
		self.verify.verify_values_match(expected='https://profile.w3schools.com/', actual=self.sd.get_current_url())

	def test2(self):
		# correct credential check
		self.sd.clear_input_field(element=self.login.email_text())
		self.sd.send_keys(element=self.login.email_text(), data=self.username)
		self.sd.clear_input_field(element=self.login.current_password_password())
		self.sd.send_keys(element=self.login.current_password_password(), data=self.c_password)
		self.sd.element_click(element=self.login.login_btn())
		self.sd.wait(10)
		self.verify.verify_values_match(expected='https://my-learning.w3schools.com/', actual=self.sd.get_current_url())

	@classmethod
	def teardown_class(cls):
		cls.sd.close_browser()
		cls.logger.debug('teardown')
