### 初始化
git config --global user.name "testname"
git config --global user.eamil "testname@exampl.com"
### 命令配置别名
git config --global alias.co checkout: 将checkout 别名配置为co
### 区域
- 工作区
- 暂存区
- 版本库
### 对象
- Git对象
    > 1. echo 'test content' | git hash-object -w(存储) --stdin(从标准输入读取内容)
    > 2. git hash-object -w 文件路径：存文件
    > 3. git hash-object 文件路径： 返回文件对应的键值
    > 4. git cat-file -p 哈希值：返回对应文件内容
    > 5. git cat-file -t 哈希值：查看内部存储类型，会返回blob
- 树对象
    >可以通过update-index；write-tree；read-tree等命令来构建树对象并存入暂存区
- 提交对象
### .Git目录介绍
- hooks:目录包含客户端或服务器端的钩子脚本
- info:包含一个全局性排除文件
- logs:日志信息
- objects:目录存储所有数据内容
- refs:目录存储指向数据（分支）的提交对象的指针
- config:文件包含项目特有的配置选项
- description:用来显示对仓库的描述信息
- HEAD:文件指示目前被检出的分支
- index:文件保存暂存区信息

### git基本操作流程
#### git CRUD命令
   - git init:初始化仓库
   - git add .:将修改的添加到暂存区（但不包含被删除的文件）  
     
       > 1. git add -u:仅监控已经被add的文件（即tracked file），他会将被修改的文件提交到暂存区(不包含新文件)
       > 2. git add -A:git add --all的缩写，全部文件添加到暂存区
   - git commit -m "说明":将暂存区提交到版本库
     
       > 1. 如果说明信息较多，可以不加-m，此时会出现对话框，填入说明信息。
       > 2. git commit -a -m '提交信息':可以对已跟踪文件跳过git add 直接提交(新文件不行)
       > 3. git commit --amend:可以修改上一次的提交信息,可以将最近的修改追加到上一次的提交上

   - git sttaus:查看当前文件状态
   - git diff:查看有哪些更新还未暂存
   - git diff --cached:查看哪些更新在暂存区还未提交  
     
       > 1. git diff --staged也可以
   - git log:查看提交记录
       > 1. git log --pretty=oneline:一行显示
       > 2. git log --onelne:一行显示
       > 3. git log --oneline --decorate --graph --all: 查看项目分叉历史
   - git rm 文件名:删除工作目录的一个文件，再将修改添加到暂存区
   - git mv 原文件名 新文件名:将工作目录文件重命名，再将修改添加到暂存区

#### git 分支命令

   - git branch 分支名:创建新分支并不会自动切换到新分区中去
     
       > git branch 分支名 commitHash:从对应提交点创建分支
   - git branch:显示所有分支
   - git branch -d 分支名：删除分支
       > 1. 最佳实践:每次切换分支前，当前分支一定得是干净的(已提交状态)
       > 2. 坑:在切换分支时，如果当前分支上有未暂存的修改（第一次） 或 有未提交的暂存（第一次），分支可以切换成功，但是会把相应内容带入到切换后的分支，污染分支，如果是已提交过的文件再次修改后，然后直接切换分支将切换不成功。
       > 3. git branch -D 强制删除
   - git checkout 分支名:切换分支
       > 1. git checkout -b 分支名:创建分支并切换
       > 2. git checkout -b dev(本地分支名称) origin/dev(远程分支名称)  注：一般要先fetch下
       > 3. git checkout --track orgin/branch_name 来在本地创建一个与 branch_name 同名分支跟踪远程分支
   - git merge 分支名：合并分支
     
       > 1. 解决冲突：打开对应文件修改相应内容，然后add,commit

#### Git存储
   - git stash:将未完成的修改保存到一个栈上
       > 1. git stash save "save message"  : 执行存储时，添加备注，方便查找，只有git stash 也要可以的，但查找时不方便识别。
       > 2. 新增的文件，直接执行stash是不会被存储的
   - git stash list  ：查看stash了哪些存储
   - git stash show ：显示做了哪些改动，默认show第一个存储,如果要显示其他存贮，后面加stash@{$num}，比如第二个 git stash show stash@{1}
   - git stash show -p : 显示第一个存储的改动，如果想显示其他存存储，命令：git stash show  stash@{$num}  -p ，比如第二个：git stash show  stash@{1}  -p
   - git stash apply :应用某个存储,但不会把存储从存储列表中删除，默认使用第一个存储,即stash@{0}，如果要使用其他个，git stash apply stash@{$num} ， 比如第二个：git stash apply stash@{1} 
   - git stash pop ：命令恢复之前缓存的工作目录，将缓存堆栈中的对应stash删除，并将对应修改应用到当前的工作目录下,默认为第一个stash,即stash@{0}，如果要应用并删除其他stash，命令：git stash pop stash@{$num} ，比如应用并删除第二个：git stash pop stash@{1}
   - git stash drop stash@{$num} ：丢弃stash@{$num}存储，从列表中删除这个存储
   - git stash clear ：删除所有缓存的stash

#### 撤销与重置
   - git checkout -- 文件名：撤销已修改的文件
   - git reset HEAD 文件名：撤销暂存区已修改的文件
   - git commit --amend：既可以对上次提交的内容进行修改，也可以修改提交说明
   - git reset
       > 1. git reset --soft HEAD~: 移动HEAD指向的分支到上一次提交点
       > 2. git reset --mixed HEAD~:撤销上一次提交，并取消暂存区的提交，回到了git add 和git commit 之前	
       > 3. git reset --hard HEAD~:撤销上一次提交，git add和git commit以及工作区所有内容。注意：该命令强制覆盖工作区的文件，如果找回可以通过reflog，但是未提交的文件将不能找回。
#### 数据恢复
   - git reflog:所有的操作历史
     
       > git log -g:显示信息更全
   - 恢复：可以reset --hard 或基于要恢复的提交点创建分支,建议使用创建分支的策略
#### 打tag
   - git tag：打标签
       > 1. git tag -l "v1.0.1":带注解的
       > 2. git tag v1.0.1 commitHash:基于某个提交点打tag
       > 3. git show v1.0.1:展示对应tag信息
       > 4. git push origin v1.0.1:推送tag到远程分支
       > 5. git push otigin --tags:推送全部tag
       > 6. git tag -d v1.0.1:删除本地tag
       > 7. git push origin :refs/tags/v1.0.1:删除远程tag
#### 远程协作
   - git remote -v:查看远程仓库的别名及URL
   - git remote add <name> <url>:添加远程仓库并制定一个可以引用的名字
   - git remote show [name]:查看远程仓库更多信息
   - git remote rename oldName newName:重命名
   - git remote rm name:移除远程仓库
   - git push origin branch_name等同于git push origin branch_name[本地分支名]:branch_name[远程分支名]:本地和远程可以不同
   - git merge origin/branch_name::本地合并远程分支代码
   - git branch -u origin/branch_name:设置本地分支跟踪的远程分支
   - git branch -vv:查看设置的所有跟踪分支
   - git push origin --delete branch_name:删除远程分支
   - git remote prune origin --dry-run:列出仍在远程跟踪但是远程已被删除的无用分支
   - git remote prune origin:清除上面命令列出的远程跟踪
   - git pull --rebase:不会出现合并分支的提交信息 
     