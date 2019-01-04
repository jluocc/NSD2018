hadoop 高可用
 192.168.1.10   nn01  namenode,resourcemanager
 192.168.1.20   nn02  namenode,resourcemanager 
 192.168.1.11	node1 datanode nodemanager
 192.168.1.12	node2 datanode nodemanager
 192.168.1.13	node3 datanode nodemanager
 192.168.1.21	zk1   zookeeper, journalnode
 192.168.1.22	zk2   zookeeper, journalnode
 192.168.1.23	zk3   zookeeper, journalnode
#----------------------------------------------
1 准备机器，清空所有配置
  停止所有服务
  清空 rm -rf /var/hadoop/* (所有机器)
  启动  zookeeper  集群
  配置 /etc/hosts  (所有机器)
  安装 java 环境， 配置 ssh 秘钥登录
  nn01,nn02 能登录所有机器，包括本机
#----------------------------------------------
安装配置
    hadoop-env.sh
    core-site.xml
    hdfs-site.xml
    mapred-site.xml
    yarn-site.xml
    slaves
#----------------------------------------------
初始化启动集群
ALL: 所有机器 node{1..3} zk{1..3} nn01 nn02
nodeX： node1    node2    node3
zkX:    zk1      zk2      zk3
NN1: nn01
NN2: nn02
#----------------------------------------------
ALL: 同步配置到所有集群机器
NN1: 初始化ZK集群  ./bin/hdfs zkfc -formatZK
zkX:  启动 journalnode 服务 
  ./sbin/hadoop-daemon.sh start journalnode

NN1: 格式化  ./bin/hdfs  namenode  -format
NN2: 数据同步到本地 /var/hadoop/dfs
NN1: 初始化 JNS
  ./bin/hdfs namenode -initializeSharedEdits

zkX: 停止 journalnode 服务
  ./sbin/hadoop-daemon.sh stop journalnode
启动集群
NN1:./sbin/start-all.sh
NN2:./sbin/yarn-daemon.sh start resourcemanager
#----------------------------------------------

查看集群状态
./bin/hdfs haadmin -getServiceState nn1  
./bin/hdfs haadmin -getServiceState nn2
./bin/yarn rmadmin -getServiceState rm1
./bin/yarn rmadmin -getServiceState rm2

./bin/hdfs dfsadmin -report
./bin/yarn node  -list

访问集群：
./bin/hadoop  fs -ls  /
./bin/hadoop  fs -mkdir hdfs://nsdcluster/input

验证高可用，关闭 active namenode
./sbin/hadoop-daemon.sh stop namenode
./sbin/yarn-daemon.sh stop resourcemanager

恢复节点
./sbin/hadoop-daemon.sh stop namenode
./sbin/yarn-daemon.sh stop resourcemanager

