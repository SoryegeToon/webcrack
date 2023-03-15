requests_timeout = 10
thread = 10
fail_words = ['密码错误', '重试', '不正确', '密码有误', '不成功', '重新输入', '不存在', '登录失败', '登陆失败', '密码或安全问题错误', 'history.go',
              'history.back',
              '已被锁定', '安全拦截', '还可以尝试', '无效', '攻击行为', '创宇盾', 'http://zhuji.360.cn/guard/firewall/stopattack.html',
              'D盾_拦截提示', '用户不存在',
              '非法', '百度云加速', '安全威胁', '防火墙', '黑客', '不合法', 'Denied', '尝试次数',
              'http://safe.webscan.360.cn/stopattack.html', "Illegal operation", "服务器安全狗防护验证页面"]
captcha_keyword_list = [
    "验证码",
    "captcha",
    "验 证 码",
    "点击更换",
    "点击刷新",
    "看不清",
    "认证码",
    "安全问题"
]
username_flag = {'str': ['userName', 'login_username', 'WG_username_input', 'username', 'UserAccount', 'user', 'name',
                         'account', 'txtBianhao', 'txtUser', 'passport', 'TxtUserName', 'LoginForm[username]',
                         'UserName', 'TextBox_name', 'userid', 'adminname'],
                 'xpath': ['//*[@id="userName"]', '//*[@id="login_username"]', '//*[@id="WG_username_input"]',
                           '//*[@id="username"]', '//*[@id="UserAccount"]', '//*[@id="user"]', '//*[@id="name"]',
                           '//*[@id="account"]', '//*[@id="txtBianhao"]', '//*[@id="txtUser"]', '//*[@id="adminname"]',
                           '/html/body/div/div/form/div[1]/div/div/input',
                           '/html/body/div/div/div[2]/form/div[1]/div/div/input',
                           '/html/body/div/div/form/p[1]/input[1]']}
password_flag = {'str': [  # 检测登录页面关键字
    "passWord",
    "login_password",
    "password",
    "pass",
    "mima",
    "txtPwd",
    "TxtUserPwd",
    "LoginForm[password]",
    "TextBox_pwd",
    "userpwd",
    "pwd"
],
    'xpath': ['//*[@id="passWord"]', '//*[@id="login_password"]', '//*[@id="password"]', '//*[@id="pass"]',
              '//*[@id="mima"]', '//*[@id="txtPwd"]', '/html/body/div/div/form/div[2]/div/div/input',
              '/html/body/div/div/div[2]/form/div[2]/div/div/input', '//*[@id="userpwd"]',
              '/html/body/div/div/form/p[1]/input[2]']}

login_flag = ['登', 'Login', 'login', 'sign up', 'Sign Up']
