
def get_driver():
	from selenium import webdriver
	from selenium.webdriver import ChromeOptions
	option = ChromeOptions()
	option.add_experimental_option('excludeSwitches', ['enable-automation'])
	driver = webdriver.Chrome(options=option)
	return driver

def scroll(driver, distance):
	driver.execute_script(f"var q=document.documentElement.scrollTop={distance}")
	

def find_element(driver, xpath):
	return driver.find_elements_by_xpath(xpath)


def get_element_value(elements,key):
	return [i.get_attribute(key) for i in elements]


def write(res,filename='item.txt'):
	with open(filename,'a',encoding='utf8') as f:
		f.write('\n'.join(res))
		f.write('\n')


