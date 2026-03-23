---
title: 使用 Cpolar 异地组网，在 VSCode 上 SSH 远程开发 Ubuntu 主机
date: 2024-03-21 00:00:00
updated: 2026-03-22 00:00:00
tags: [Cpolar, SSH, VSCode, 异地组网，远程开发]
categories: 技术分享
---

## 前言

在机器人被搬到另一个屋之后，通过局域网进行 SSH 开发就变成了个困难的问题。因此尝试了异地组网来解决这个问题，看了一些资料后发现基于 Cpolar 进行异地组网也不困难，这里记录一下步骤。

---

## 开发环境

- **硬件**: 香橙派 5 Plus，NUC13
- **系统**: Ubuntu 20.04

---

## 操作流程

### 1. 安装 Cpolar 软件

首先安装 Cpolar 软件：

```bash
# 安装 curl（前置软件）
sudo apt install curl

# 安装 cpolar
curl -L https://www.cpolar.com/static/downloads/install-release-cpolar.sh | sudo bash
```

查看 Cpolar 版本号可以验证是否安装成功：

```bash
cpolar version
```

### 2. 添加并启动 Cpolar 服务

在系统中添加 Cpolar 服务并启动：

```bash
sudo systemctl enable cpolar
sudo systemctl start cpolar
```

### 3. 进入 Cpolar 控制面板

安装完成后打开浏览器进入 Cpolar 控制面板，输入：

```
localhost:9200
```

进入 Cpolar 控制面板登录后，会是如下界面：

![Cpolar 隧道管理界面](/images/posts/cpolar-ssh/01-cpolar-tunnel-settings.jpg)

*Cpolar 隧道管理界面，添加新的 SSH 隧道，名称自定义，协议选择 tcp，本地地址填写 22，端口类型选择随机临时 TCP 端口，地区选择 China Top*

### 4. 添加 SSH 隧道

添加一个新的隧道，配置如下：
- **隧道名称**: ssh（可自定义）
- **协议**: tcp
- **本地地址**: 22
- **端口类型**: 随机临时 TCP 端口
- **地区**: China Top

然后点击"更新"按钮保存配置。

### 5. 查看公网隧道

打开在线隧道列表，发现这里实现了一个公网隧道：

![Cpolar 在线隧道列表](/images/posts/cpolar-ssh/02-cpolar-tunnel-list.jpg)

*Cpolar 在线隧道列表，显示隧道名称、公网地址、协议、本地地址和创建时间*

记录下公网地址，后续 SSH 连接会用到。

---

## SSH 配置

### 1. 配置 SSH 客户端

在本地计算机上编辑 SSH 配置文件（`~/.ssh/config`），添加以下内容：

![SSH 配置文件](/images/posts/cpolar-ssh/03-ssh-config.jpg)

*SSH 配置文件，包含 Host、HostName、Port、User 配置*

```
Host 12.tcp.cpolar.top
    HostName 12.tcp.cpolar.top
    Port <你的端口号>
    User <你的用户名>
```

### 2. VSCode SSH 连接

打开 VSCode，安装 Remote - SSH 扩展，然后添加 SSH 连接：

![VSCode SSH 连接界面](/images/posts/cpolar-ssh/04-vscode-ssh.jpg)

*VSCode SSH 连接界面，显示已连接的 SSH 主机和远程文件夹*

连接成功后，就可以在 VSCode 上进行远程开发了。

---

## 使用技巧

### 1. 固定隧道地址

如果需要长期使用，建议在 Cpolar 官网注册账号并购买基础套餐，这样可以获得固定的公网地址，避免每次重启都要重新配置。

### 2. 开机自启动

Cpolar 服务已经通过 systemd 配置为开机自启动，无需额外配置。

### 3. 安全注意事项

- 使用 SSH 密钥认证代替密码认证
- 定期更换 SSH 密钥
- 限制 SSH 登录用户
- 使用防火墙限制访问

---

## 参考资料

- [Cpolar 官方文档](https://www.cpolar.com/)
- [VSCode Remote SSH 文档](https://code.visualstudio.com/docs/remote/ssh)

---

---

## 原文链接

本文原载于 CSDN：[使用 Cpolar 异地组网，在 vscode 上 ssh 远程开发 ubuntu 主机](https://blog.csdn.net/weixin_43326110/article/details/136904763)

*最后更新：2026 年 3 月*
