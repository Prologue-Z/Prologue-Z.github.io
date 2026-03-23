---
title: 【ROS】ROS 局域网下多机通讯方法
date: 2024-10-19 00:00:00
updated: 2026-03-22 00:00:00
tags: [ROS, 多机通讯，局域网配置]
categories: 技术分享
---

## 目录

1. [网络配置](#一网络配置)
2. [修改两个设备的 hosts 文件](#二修改两个设备的 hosts 文件)
3. [修改两个 ROS 设备的.bashrc](#三修改两个 ros 设备的 bashrc)
4. [launch 文件中给节点设定运行的设备](#四 launch 文件中给节点设定运行的设备)

---

## 一、网络配置

首先确保两个 ROS 设备连接到同一局域网下，然后查询两个设备的在这个局域网内的 IP 地址，运行：

```bash
ifconfig
```

这里举个例子，主机的 IP 地址为 `192.168.1.127`，从机的 IP 地址为 `192.168.1.126`；之后可测试一下能否互相 ping 通，成功后进行下一步。

将两个电脑用网线直连可以构建一个简易的局域网（而且速度快），但是需要在两个电脑上设置一下为 ipv4 设置为手动模式，然后设置到统一的子网地址，网关也要一致，例如网关都设置为 `192.168.1.200`，主机和从机的 ip 地址分别为 `192.168.1.127`，`192.168.1.126`。

---

## 二、修改两个设备的 hosts 文件

这里需要在主机和从机的 hosts 文件中分别添加对方的 IP 和用户名。

### 主机端

```
192.168.1.126 ros_cv
```

### 从机端

```
192.168.1.127 camar
```

---

## 三、修改两个 ROS 设备的.bashrc

在 ROS 的使用中 `.bashrc` 是一个比较常见的配置文件，主要是修改终端的配置。这里我们需要对两设备分别添加 ROS 多机通讯的环境变量。

### 主机端

在 `~/.bashrc` 文件末尾添加：

```bash
export ROS_MASTER_URI=http://192.168.1.127:11311
export ROS_HOSTNAME=192.168.1.127
```

### 从机端

在 `~/.bashrc` 文件末尾添加：

```bash
export ROS_MASTER_URI=http://192.168.1.127:11311
export ROS_HOSTNAME=192.168.1.126
```

添加完成后，运行以下命令使配置生效：

```bash
source ~/.bashrc
```

---

## 四、launch 文件中给节点设定运行的设备

在 launch 文件中，可以通过 `machine` 标签来指定节点运行的设备：

```xml
<launch>
    <!-- 在主机上运行的节点 -->
    <node pkg="package_name" type="node_name" name="node_name" />
    
    <!-- 在从机上运行的节点 -->
    <machine name="remote_machine" address="192.168.1.126" default="true"/>
    <node machine="remote_machine" pkg="package_name" type="node_name" name="node_name" />
</launch>
```

---

## 测试验证

配置完成后，可以通过以下方式测试多机通讯是否成功：

1. **在主机上运行 roscore**
2. **在从机上运行** `rostopic list` **查看是否能列出主机上的 topic**
3. **在从机上运行** `rosrun` **启动节点，观察是否能在主机上看到**

---

---

## 原文链接

本文原载于 CSDN：[【ROS】ROS 局域网下多机通讯方法](https://blog.csdn.net/weixin_43326110/article/details/143085572)

*最后更新：2026 年 3 月*
