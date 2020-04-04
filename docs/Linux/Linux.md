#### vim
1. 正常模式
    > 可以使用快捷键
    > 1. 拷贝当前行:yy ,拷贝当前行向下5行:5yy, 粘贴:p
   > 2. 删除当前行:dd,删除当前行向下5行:5dd
   > 3. 在文件中查找某个单词: / 回车查找，输入n查找下一个 或？向前查找
   > 4. 设置文件行号:set nu ,取消行号:set nonu
   > 5. 到文件最末行:G, 最首行号:gg
   > 6. 在插入模式输入后想撤回: 回到正常模式然后输入u
   > 7. 移动光标到指定行:先输入行号，然后在输入shift+g 或nG也可以到n行
   > 8. 移动到行首:0 
   > 9. 移到光标所在屏幕行行首:g0
   > 10. 移动到行尾:$
   > 11. 移动光标所在屏幕行行尾:g$ 
   > 12. 复制在可视模式下选中的文本:y
   > 13. 删除（剪切）在可视模式下选中的文本:d
2. 插入模式/编辑模式
   
    > 可以进行编辑输入
3. 命令模式
   
    > 通过指令完成相关操作

#### 指令
1. mkdir 创建文件夹
   
    > -p:多级目录创建

2. touch 创建空文件，可以一次创建多个
3. cp 拷贝
    > cp source dest 单个文件
    > -r:递归复制整个文件夹: cp -rf  source dest 拷贝文件夹
4. cat 查看文件，会一次性全部输出，一般与more结合使用
5. more 查看文件，分页显示，但是整个文件读到内存
    > 空格：下翻一页
    > 回车：一行一会
    > ctrl+B: 返回上一屏
    > ctrl+F:向下滚动一屏
    > q:退出
6. less 查看文件，分页显示，但不是一次性整个文件加载进内存
    > 空格：下翻一页
    > pagedown:下翻一页
    > pageup:上翻一页
    > / :向下搜索, n向下查找, N向上查找
    > ?:向下搜索, n向下查找, N向上查找
    > q:退出
7. find:将从指定目录向下递归地遍历其各个子目录，将满足条件的文件或目录显示在终端
    > find /home -name hello.txt：按名字查找
    > find /opt -user nobody：按用户归属查找
    > find / -size +20M: 按文件大小查找（+大于 -小于 不加为等于）
8. locate:快速定位文件路径
    > 第一次运行前必须先执行 updatedb创建locate数据库
    > locate hello.txt
9. grep 过滤查找
    > cat hello.txt | grep -n yes :会显示出行号
    > cat hello.txt | grep -i yes :忽略大小写
10. gzip/gunzip 压缩
    > gzip hello.txt ：压缩hello.txt文件为hello.txt.gz（不会保留源文件）
    > gunzip hello.txt.gz：解压
11. zip/unzip 压缩
    > zip -r hello.zip /home: -r递归压缩，将/home压缩为hello.zip
    > zip -d /opt hello.zip: -d指定文件夹，将hello.zip解压到/opt
12. tar 打包
    > 压缩 tar -zcvf xxx.tar.gz dirName
    > 解压 tar -zxvf xxx.tar.gz
    > 指定目录解压 tar -zxvf xxx.tar.gz -C dirName
13. df -h 查看磁盘空间使用
14. du -h /目录：查询指定目录使用情况
    > -s:指定目录占用大小汇总
    > -h:带计量单位
    > -a:含文件
    > --max-depth=1:子目录深度
    > -c:列出明细的同时，增加汇总值
15. ls -l /home | grep "^-" |  wc -l:统计文件夹下文件个数
16. ls -lR /home | grep "^-" |  wc -l:统计文件夹下及其文件夹下文件个数
17. ls -l /home | grep "^d" |  wc -l:统计文件夹个数
18. tree:显示目录树 如果无法使用需要安装 yum install tree
19. ps 查看进程
    > -a 显示当前终端所有进程信息
    > -u 以用户的格式显示进程信息
    > -x 显示后台进程运行的参数
    > -e 显示所有进程
    > -f 全格式

#### crond任务调度
1. crontab [选项]
    > 1. -e 编辑定时任务：crontab -e 然后在里边输入：*/1 * * * * /home/mytask.sh
    > 2. -l 查询定时任务
    > 3. -r 删除当前用户所有定时任务

#### 服务管理
1. service管理指令
    > service 服务名 [start | stop | restart | reload | status]
    > 在CentOS7.0后，不再使用service，而是systemctl
2. 查看系统有哪些服务
   
    > ls -l /etc/init.d/
3. chkconfig 可以给每个服务的各个运行级别设置自启动/关闭(需要重启才会生效)
    > chkconfig --list | grep xxx:查看某个服务
    > chkconfig 服务名 --list:查看某个服务
    > chkconfig --level 5 服务名 on/off: 设置某个服务在5级别的开启或关闭

#### 监控服务
1. 动态监控进程top
    > -d 秒数 : 指定top命令每隔几秒更新，默认为3秒在top命令的交互模式当中可以执行的命令
    > -i: 使top不显示任何闲置或僵死的进程
    > -p: 通过指定监控进程ID来仅仅监控某个进程的状态
    > 交互命令
    > > P : 以CPU使用率排序，默认就是此项
    > > M:以内存使用率排序
    > > N:以PID排序
    > > u:查找某个用户的进程
    > > k:杀死某个进程
    > > q:退出top
2. 查看网络情况netstat
    > -an:按一定顺序排列输出
    > -p:显示哪个进程在调用

#### RPM包管理器
1. 查看以安装rpm列表：rpm -qa | grep xxx
2. 查看软件是否安装：rpm -q 软件包名
3. 查看软件包信息：rpm -qi 软件包名
4. 查询软件包中的文件：rpm -ql 软件包名
5. 查询文件所属的软件包: rpm -qf 文件全路径名
6. 卸载：rpm -e 软件包名（有时会提示有依赖，如果强制删除加 --nodeps 参数）
7. 安装：rpm -ivh 软件包全路径名

#### YUM
1. yum list | grep xx:查询yum服务器是否有需要安装的软件
2. yum install xxx:安装指定的yum包
3. yum remove xxx:卸载指定安装包

#### Shell
1. 格式要求
    > 以#!/bin/bash开头
    > 文件要有可执行权限
    > 如无可执行权限，也可以用sh 脚本，来执行
2. shell变量
    1. 系统变量
       
        > $HOME、$PWD、$USER等等 
    2. 用户自定义变量
        > 定义变量： 变量=值
        > 撤销变量：unset 变量
        > 声明静态变量(不能unset)：readonly 变量=值
    3. 定义变量规则
        > 可以由字母、数字和下划线组成，但不能以数字开头
        > 等号两侧不能有空格
        > 变量名称一遍习惯为大写
    4. 将命令返回值赋值给变量
        > A=\`ls -la\` 反引号
        > A=$(ls -la)
    5. 位置参数变量
        > $n：n为数字， $0代表命令本身，$1-$9代表第一到第九个参数，${10}要加大括号
        > $*: 命令行中所有的参数，即把所有参数都看成一个整体
        > $@:命令行中所有的参数,但是把每个参数区分对待
        > $#:命令行中所有参数的个数
    6. 预定义变量
        > 1. $$ : 当前进程的进程号（PID）
        > 2. $! : 后台运行的最后一个进程的进程号(PID)
        > 3. $? : 最后一次执行命令的返回状态；0 上一个命令正确执行，非0上一个命令不正确执行
3. 运算符
    > $((运算式)) 或 $[运算式]
    > expr m + n
    > expr m - n
    > expr  \\*, /, %
4. 条件判断
    > [ conndition ] : 注意condition前后要有空格
    > 非空返回true， 可使用 $?验证 (0为true, 非0为false)
    > = 字符串判断
    > -lt 小于
    > -le 小于等于
    > -eq 等于
    > -gt 大于
    > -ge 大于等于
    > -ne 不等于
    > -r 有读的权限
    > -w 有写的权限
    > -x 有执行的权限
    > -f 文件存在并且是一个常规文件
    > -e 文件存在
    > -d 文件存在并且是一个目录
5. 流程控制
    > 1. if else 语法格式
    > ```shell
    >  if condition
    >  then
    >      command1 
    >      command2
    >      ...
    >      commandN 
    >  fi
    > ```

    > 2. if else-if else 语法格式
    > ```shell
    > if condition1
    > then
    >     command1
    > elif condition2
    > then
    >     command2
    > else
    >     commandN
    > fi
    > ```

    > 3. for 循环
    > ```shell
    > for var in item1 item2 ... itemN
    > do
    >     command1
    >     command2
    >     ...
    >     commandN
    > done
    > ```

    > 4. while 语句
    > ```shell
    > while condition
    > do
    >    command
    > done
    > ```

    > 5. case
    > ```shell
    > case 值 in
    > 模式1)
    >      command1
    >      command2
    >      ...
    >      commandN
    >      ;;
    > 模式2)
    >      command1
    >      command2
    >      ...
    >      commandN
    >      ;;
    > esac
    > ```

6. 读取控制台输入read
    > read(选项)(参数)
    > -p:指定读取值时的提示符；read -p "请输入一个数"
    > -t:指定读取值时等待的时间(秒)，超时不再等待

7. 函数
    1. 系统函数
        > basename /home/aaa/test.txt : 会返回test.txt
        > basename /home/aaa/test.txt .txt : 会返回test
        > dirname /home/aaa/test.txt : 会返回/home/aaa
    2. 自定义函数
        > ```shell
        > [ function ] funname [()]
        > {
        >     action;
        >     [return int;]
        > }
        > ```
        > 1. 注意：可以带function fun() 定义，也可以直接fun() 定义,不带任何参数
        > 2. 参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255)
