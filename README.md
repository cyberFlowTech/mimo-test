UI自动化脚本使用指南

1、启动appium inspector时手机上的webDriverAgent被删除

未知原因：WebDriverAgent有时候无法启动app

解决方案：手机安装好Automation Running后，等一会在启动Appium Inspector，多尝试几次

2、脚本无法打开app，链接appium服务时报错

a、appium-python-client版本不低于3.0.0需要用Options（）设置参数；

b、过低也会报错：TypeError: missing 1 required keyword-only argument: 'options' (instance of driver `options.Options` class)；

C、2.11.1版本可正常使用

3、缺少driver对象

appium-python-client跟pytest版本不兼容，建议安装低版本的pytest库

4、报错：无driver对象。可能是无法正常运行setup

解决方案：在用例中引用setup，或者使用fixtrue装饰器
