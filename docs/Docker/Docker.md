### Docker

#### 组成

1. 镜像(image)

2. 容器(Container)

3. 仓库(Repository)
#### 安装步骤(centos7)
1. 能上网
2. yum -y install gcc
3. yum -y install gcc-c++
4. 安装需要的软件  yum install -y yum-utils device-mapper-persistent-data lvm2
5. 设置stable镜像仓库为阿里云仓库：yum-config-manage --add-repo  http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
6. 更新yum软件包索引 yum makecache fast
7. 安装Docker CE : yum -y install docker-ce
8. 启动docker：systemctl start docker
9. 测试：docker version  / docker run hello-world
10. 卸载：systemctl stop docker/yum -y remove docker-ce/rm -rf /var/lib/docker
#### 配置加速器
1. https://dev.aliyun.com/search.html
2. 登录获取加速器地址，下方有配置步骤，安装提示操作

#### 常用明令
- 帮助命令
  1. docker version
  2. docker info
  3. docker help
- 镜像命令
  1. docker images  列出本地镜像信息
   > REPOSITORY： 表示镜像的仓库源
   > TAG：镜像标签，表示版本
   > IMAGE ID：镜像ID
   > CREATED：镜像创建时间
   > SIZE：镜像大小
   > 参数OPTIONS说明：
   > -a： 列出本地所有的镜像(含中间映像层)
   > -q：值显示镜像ID
   > --digests：先许镜像的摘要信息
   > --no-trunc：显示完整的镜像信息
  2. docker search + image_name 搜索镜像
   > OPTIONS说明：
   > --no-trunc：显示完整的镜像信息
   > -s：列出收藏数不小于指定值的镜像
   > --automated：只列出automated build类型的镜像
  3. docker pull + image_name[:TAG] 下载镜像
  4. docker rmi + image_name_id(使用名字也可以)
   > -f :强制删除
   > 删除多个：镜像之间加空格即可 docker rmi image_name1 image_name2
   > 删除全部：docker rmi -f $(docker images -qa)

- 容器命令
  1. 新建并启动容器：docker run [OPTIONS] image [COMMAND] [ARG...]
   > OPTIONS参数说明：
   > --name="newname" 指定容器名称
   > -d：后台运行容器 注意：容器后台运行，必须有一个前台进程，否则会自动关闭容器，例如 docker run -d centos /bin/sh -c "while true; do echo hello; sleep 2; done"
   > -i：以交互模式运行容器，通常与-t同时使用
   > -t：为容器分配一个伪输入终端，通常与-i同时使用
   > -P：随机端口映射
   > -p：指定端口，格式为：ip:hostPort:containerPort / ip::containerPort / hostPort:containerPort
  2. 列出当前所有正在运行的容器：docker ps [OPTIONS]
   > OPTIONS参数说明：
   > -a：列出所有，正在运行+历史运行
   > -l：显示最近创建容器
   > -n：显示最近n个  docker ps -n 3
   > -q：静默显示，只显示容器编号
   > --no-trunc：不截断输出
  3. 退出容器：exit 停止并退出 / ctrl+P+Q 容器不停止退出
  4. 启动容器：docker start 容器ID或容器名
  5. 重启容器：docker restart 容器ID或容器名
  6. 停止容器：docker stop 容器ID或容器名
  7. 强制停止容器：docker kill 容器ID或容器名
  8. 删除已停止的容器：docker rm 容器ID / 删除多个 docker rm -f $(docker ps -qa)
  9. 查看容器日志：docker logs -f -t --tail 容器ID
   > -f：跟随最新日志打印
   > -t：加入时间戳
   > --tail 数字：显示最后多少条
  10. 查看容器内运行的进程：docker top 容器ID
  11. 进入运行的容器并以命令行交互：docker exec -it 容器ID  /bin/bash    // docker exec -it 容器ID ls -l /tmp
  12. 重新进入容器：docker attach 容器ID