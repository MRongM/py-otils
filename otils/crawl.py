"""
selenium requests 相关封装模块
"""

def sdriver(path=None,head=True,img=True):
    from selenium import webdriver
    from selenium.webdriver import ChromeOptions
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    if not img:
        prefs = {'profile.default_content_setting_values': {'images': 2,}}
        option.add_experimental_option('prefs', prefs)
    if not head:
        option.add_argument('--headless')
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