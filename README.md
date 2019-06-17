## Python3 学习笔记
此版本库记录了自己学习Python3 版本的过程，还有自己的写的一些小demo的例子，python 是未来的趋势，学习python是开发者必不可少的一种技能；

### 一、Python3的升级安装
本人的服务器是 CentOS Linux release 7.2.1511 (Core),系统默认会安装python 大家可以看下自己的python 版本 python -V  如果是python 2.xx版本，需要升级到Python 3.0以上的版本，具体的升级教程本人也整理了一份：https://www.kancloud.cn/zhangshl/echophp/853608
### 二、学习的Python3内容：
* 基本语法
* 条件判断
* 集合
* 递归
* 函数的参数
* 定义函数
* 函数调用
* 函数返回值
* python list - 列表生成式
* python - tuple元组
* python - str 字符串
* python - 列表和元组tuple 的切片

### Python3 爬虫使用到的类库
* json 
* requests
* codecs


### Git 常用命令：
Git 是必不可少的版本控制工具，相比较SVN更加灵活，注重版本控制；
#### Git初始化设置

      git config --global user.name "xxx" 
      git config --global user.email "xxx@phpren.com"
      ssh-keygen -t rsa -C "xxx@phpren.com"
      cat ~/.ssh/id_rsa.pub 复制公钥到下面链接点击Add Key完成添加
 #### Git克隆项目 

      git clone git@gitlab.phpren.com:rd/phpren.git
#### git常用命令
      git add xxx 添加文件到暂存区
      git rm xxx 删除文件，替代物理删除文件，然后提交
      git commit -m "xxx" 提交更改到本地仓库
      git push 推送更改到远程分支
      git pull 从远程分支拉取更改
      git reset HEAD xxx 如果某个文件被add了，但不想commit可以恢复
      git branch xxx 创建某个分支
      git checkout xxx 切换到某个分支
      git checkout -b xxx 新建某个分支并切换过去
      git branch -av 查看所有本地分支+远程分支及对应版本号
      git merge --no-ff xxx 合并分支
      git branch -d/-D xxx 删除本地分支（区别是是否被merged）
      git diff xxx 查看文件改动
      git log xxx 查看文件变动日志
	  git status 查看当前分支状态

