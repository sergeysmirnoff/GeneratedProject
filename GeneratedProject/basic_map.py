from selenium.webdriver.common.by import By
# this is a mapper for page: https://www.w3schools.com/
class Basic_map:

	def __init__(self, sd):
		self.sd = sd

	def googleSearch_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='googleSearch']")

	def google_translate_element_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='google_translate_element']")

	def navbtn_tutorials_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='navbtn_tutorials']")

	def navbtn_references_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='navbtn_references']")

	def navbtn_exercises_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='navbtn_exercises']")

	def navbtn_menu_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='navbtn_menu']")

	def mypagediv_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='mypagediv']")

	def loginactioncontainer_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='loginactioncontainer']")

	def cert_navbtn_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='cert_navbtn']")

	def sectionxs_tutorials_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='sectionxs_tutorials']")

	def sectionxs_references_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='sectionxs_references']")

	def sectionxs_exercises_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='sectionxs_exercises']")

	def myAccordion_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='myAccordion']")

	def nav_tutorials_nav(self):
		return self.sd.find_element(By.XPATH, "//*[@id='nav_tutorials']")

	def nav_references_nav(self):
		return self.sd.find_element(By.XPATH, "//*[@id='nav_references']")

	def nav_exercises_nav(self):
		return self.sd.find_element(By.XPATH, "//*[@id='nav_exercises']")

	def nav_search_btn_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='nav_search_btn']")

	def nav_translate_btn_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='nav_translate_btn']")

	def radio_theme_mode_checkbox(self):
		return self.sd.find_element(By.XPATH, "//*[@id='radio_darkpage']")

	def radio_theme_mode_checkbox(self):
		return self.sd.find_element(By.XPATH, "//*[@id='radio_darkcode']")

	def darkmodemenu_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='darkmodemenu']")

	def search2_text(self):
		return self.sd.find_element(By.XPATH, "//*[@id='search2']")

	def learntocode_searchicon_i(self):
		return self.sd.find_element(By.XPATH, "//*[@id='learntocode_searchicon']")

	def learntocode_searchbtn_button(self):
		return self.sd.find_element(By.XPATH, "//*[@id='learntocode_searchbtn']")

	def listofsearchresults_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='listofsearchresults']")

	def wavepath_path(self):
		return self.sd.find_element(By.XPATH, "//*[@id='wavepath']")

	def Frontend_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='Frontend']")

	def Backend_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='Backend']")

	def img_mylearning_img(self):
		return self.sd.find_element(By.XPATH, "//*[@id='img_mylearning']")

	def myLearningFromDefault_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='myLearningFromDefault']")

	def proFromDefault_a(self):
		return self.sd.find_element(By.XPATH, "//*[@id='proFromDefault']")

	def w3_cert_arrow_svg(self):
		return self.sd.find_element(By.XPATH, "//*[@id='w3_cert_arrow']")

	def w3_cert_badge_svg(self):
		return self.sd.find_element(By.XPATH, "//*[@id='w3_cert_badge']")

	def getdiploma_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='getdiploma']")

	def howto_iframe_iframe(self):
		return self.sd.find_element(By.XPATH, "//*[@id='howto_iframe']")

	def howto_padding_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='howto_padding']")

	def popupDIV_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='popupDIV']")

	def fblikeframe_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='fblikeframe']")

	def main_div(self):
		return self.sd.find_element(By.XPATH, "//*[@id='main']")

