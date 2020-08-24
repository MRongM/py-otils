
'''
爬虫工具封装
'''

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

def get_agent():
	return "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"

def get_content_type(tag='json'):
	if tag == 'json':
		return 'application/json'
	
	if tag == 'stream':
		return 'application/octet-stream'

def shot_element(driver, xpath):
	from PIL import Image
	import time
	import os

	e = find_element(driver, xpath)[0]
	x = e.location['x']
	y = e.location['y']
	e_width = x + e.size['width']
	e_height = y + e.size['height']
	png = 'webdriver.png'
	driver.save_screenshot(png)
	pic = Image.open(png)
	pic = pic.crop((x,y,e_width,e_height))
	pic.save(f'crop_{int(time.time())}.png')
	os.remove(png)

