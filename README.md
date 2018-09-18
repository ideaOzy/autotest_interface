## 1 框架简介
### 1.1 简介
该框架可以自动运行excel表中的测试用例，在数据层面模拟界面操作产生的业务流，进行数据的自动化比对判断，并将所用测试用例的运行结果自动汇总生成测试报告（html），发邮件通知给相关人员。

#### 各分支介绍
master：主分支

dev：开发中分支

feature/base：框架原型

### 1.2 应用技术
#### 1.2.1 语言
- [python3](https://docs.python.org/3/)
#### 1.2.2 IDE
- [Spyder](https://www.anaconda.com/)
#### 1.2.3 单元测试框架
- unittest
#### 1.2.4 http请求库
- [requests](http://docs.python-requests.org/en/master/)
#### 1.2.5 各种解析库
- json
- xlrd 
#### 1.2.6 报告生成
- HTMLTestRunner
#### 1.2.7 邮件通知
- email
- [smtplib](https://docs.python.org/3/library/smtplib.html?highlight=smtplib)

### 1.2 功能说明
测试用例excel表维护
测试用例自动运行
测试结果excel报表
日志模块
邮件发送模块
自动生成Html测试结果报告

### 1.3 使用说明
- 下载源码，自行加载成工程
- 安装好相应的库
- 维护data/testcase.xlsx测试用例文件
- 运行src/test/run.py 文件
- 结果报告请查看report/xxx.html文件



## 2 框架目录结构
分层如下：
- config层：放配置文件，把所有的项目相关的配置均放到这里，实现配置与代码分离。

- data层：放数据文件，可以把所有的testcase的参数化相关的文件放到这里，一般可采用xlsx格式。实现数据与代码分离。

- lib层：放项目所需的库。

- log层：所有生成的日志均存放在这里，可将日志分类，如运行时日志test log，错误日志error log等。

- report层：放项目生成的报告，一般可有html报告、excel报告等。

- src源码层：放所有程序代码。更进一步的分层如下： 
    - case层：放所有测试用例相关的文件，如case——测试用例。
    - common层: 项目封装的公共类和方法。
    - utils层：所有工具类代码都在这里，包括读取config的类、写log的类、读取excel、xml的类、发送邮件等类和方法，都在这里。
    - runner.py：程序启动模块。

### 参考资料
#### BLOG
- [怎样从0开始搭建一个测试框架](https://blog.csdn.net/huilan_same/article/details/76572411)
