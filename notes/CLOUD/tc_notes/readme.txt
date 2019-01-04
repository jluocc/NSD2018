QQ 群 172309459 

git 软件安装
yum install -y git

外地校区
git clone git://124.193.128.166/nsd1808.git

北京本地
git clone git://172.40.53.65/nsd1808.git

更新(必须进入 git 目录)
git  pull

yum 配置自定义源
1、创建一个文件夹
2、拷贝 rpm 包到文件夹 
3、createrepo . 创建包列表索引

yum 客户端
baseurl 配置的地址路径是 repodata 所在的路径

时间服务器
与 ntp.aliyun.com 同步
