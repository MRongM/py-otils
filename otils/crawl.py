"""
selenium requests 相关封装模块
"""

def sdriver(path=None,head=True):
    from selenium import webdriver
    from selenium.webdriver import ChromeOptions
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    if not head:
        chrome_options.add_argument('--headless')
    if path:
        return webdriver.Chrome(options=option,executable_path=path)
    else:
        return webdriver.Chrome(options=option)


def sfinde(driver,xpath):
    el = None
    try:
        el = driver.find_element_by_xpath(xpath)
    except Exception as e:
        print(f"finde error:{e}")
    return el

def sfindes(driver,xpath):
    el = []
    try:
        el = driver.find_elements_by_xpath(xpath)
    except Exception as e:
        print(f"findes error:{e}")
    return el

def sget_attr(ele,name):
    attr = ''
    try:
        attr = ele.get_attribute(name)
    except Exception as e:
        print(f"get_attr error:{e}")
    return attr
    
def sclick(ele):
    try:
        ele.click()
        return True
    except Exception as e:
        print(f"click error:{e}")
    return False

def sinput(ele,value):
    try:
        ele.send_keys(value)
        return True
    except Exception as e:
        print(f"click error:{e}")
    return False

def stext(ele):
    text = ''
    try:
        text = ele.text
    except Exception as e:
        print(f"text error:{e}")
    return text

def sscroll(driver,distance=1000):
    try:
        driver.execute_script(f"var q=document.documentElement.scrollTop={distance}")
        return True
    except Exception as e:
        print(f"scroll error:{e}")
    return False 

def sclose(driver):
    driver.close()


def rheader(content='json'):
    if content == 'stream':
        content_type='application/octet-stream'
    else:
        content_type='application/json'

    head = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        'content-type': content_type,
    }
    return head

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

