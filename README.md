#### 简介

> 使用 Python 编程语言，结合 Selenium 与 unittest 框架，根据 PO 模型结构，设计贝壳找房网的自动化测试框架。此次主要针对 登录页面 及 访问租房详情页 进行 UI 自动化测试，最终输出测试执行日志，HTML 测试报告（通过 HTMLTestRunner_PY3 形成），并将相关的费用信息保存到 MySQL 数据库中。

- **[视频：多线程操控远程浏览器执行过程](https://www.bilibili.com/video/BV1S5411x7M2/)**



#### 整体开发架构

> 项目整体结构
>
> - config：配置文件
> - cookies：保存 cookies 信息
> - logs：日志系统
> - model/orm：数据库模型
> - pages：获取测试页面
>   - 登陆页面
>   - 租房信息列表页面
>   - 租房详情页面
> - report：测试报告
> - test_case：测试用例
> - utils：工具配件
>   - 启动浏览器
>   - 连接数据库
> - run_case.py：测试启动文件
>
> 开发技术栈：
>
> - Python
> - Selenium
> - unittest
> - MySQL
>   - PyMySQL
>   - DBUtils
> - HTMLTestRunner_PY3
>
> 测试环境
>
> - Windows
> - Linux
> - 多线程：Thread 模块
> - 远程启动
>   - selenium-server
>   - Java 环境
> - 无界面启动
> - Chrome 浏览器

> ![image](https://github.com/Leofighting/beike_UI_autotest/blob/master/utils/01.png)
>
> 

> [如图片无法展示，请点击](https://mubu.com/doc/ogGgxxTAX0)
