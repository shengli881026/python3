## Python3 学习笔记
```html
记录学习Python3 的过程，还有自己的一些经验，之前一直从事PHP开发，python 是未来的趋势，学习python是开发者必不可少的一种技能；
```
### Python3的升级安装
本人的服务器是 CentOS Linux release 7.2.1511 (Core),系统默认会安装python 大家可以看下自己的python 版本 python -V  如果是python 2.xx版本，需要升级到Python 3.0以上的版本，具体的升级教程本人也整理了一份：https://www.kancloud.cn/zhangshl/echophp/853608


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

