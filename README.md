# webcrack_demo
## 通过模拟浏览器点击定位登陆框去爆破密码，从而绕过js加密，vue等抓不到包的登陆框网站
## 识别原理
偶然间发现大多数网站登陆框xpath是通用的，通过互联网+遇到过的网站(总计2w+)抓取name元素与xpath元素做字典爆破登陆框的By.NAME元素
## 登陆框识别
先无脑识别css元素下的button与input点击，面对多个button的网站(如nps登陆页面)选择遍历button按钮，遇到关于“登陆，login“关键字再去点击 暂未解决那种按钮是图片贴上去的暂时放弃了
## 效果
![image](​https://github.com/SoryegeToon/webcrack/blob/main/pic/1.jpg​​)
