# map_file: map_creator


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from map_creator import search_and_create


class TestBasic:
	@classmethod
	def setup_class(cls):
		cls.driver = webdriver.Chrome()
		cls.url = "https://www.w3schools.com/"
		search_and_create(cls.url, "id", 'basic_map', 'w')
		cls.map_file_name = 'basic_map'
		from basic_map import Basic_map
		cls.basic_map = Basic_map(cls.driver)

	@pytest.fixture(autouse=True)
	def run_around_tests(self):
		self.driver.get(self.url)

	@staticmethod
	def get_function(type_of_element):
		from basic_map import Basic_map
		lst_a = dir(Basic_map)
		for func_name in lst_a:
			if type_of_element in func_name:
				return getattr(Basic_map, func_name)

	def test1(self):
		search_func = self.get_function('text')
		search_element = search_func(self.basic_map)
		search_element.send_keys('Python')
		search_element.send_keys(Keys.RETURN)
		time.sleep(2)
		assert 'Python' in self.driver.title

	def test2(self):
		search_func = self.get_function('text')
		search_element = search_func(self.basic_map)
		search_element.send_keys('HTML')
		button_func = self.get_function('button')
		button_element = button_func(self.basic_map)
		button_element.click()
		time.sleep(2)
		assert 'HTML' in self.driver.title

	def test3(self):
		a_func = self.get_function('_a')
		a_element = a_func(self.basic_map)
		assert a_element.is_displayed()

	def test4(self):
		a_func = self.get_function('_a')
		a_element = a_func(self.basic_map)
		assert a_element.is_enabled()
