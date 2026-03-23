---
title: 如何为本地计算机配置 GitHub SSH 密钥以便于上传到云端
date: 2025-07-02 00:00:00
updated: 2026-03-22 00:00:00
tags: [GitHub, SSH, 密钥配置，版本控制]
categories: 技术分享
---

## 前言

在深入操作之前，理解几个核心概念至关重要，这将有助于明晰每个步骤的目的。本指南将详细介绍如何将一个位于 Linux 环境下的本地项目文件夹，首次上传到一个空的 GitHub 远程仓库。

---

## 核心概念

### 1. Git 仓库
- **本地仓库**：本地计算机上的项目文件夹，包含 `.git` 子目录，用于存放所有 Git 元数据和历史记录
- **远程仓库**：GitHub 云端的仓库，用于代码备份和协作

### 2. SSH 密钥
- **公钥**：公开部分，添加到 GitHub 账户
- **私钥**：私有部分，保存在本地计算机
- **作用**：实现安全的身份验证，无需每次输入密码

---

## 配置步骤

### 1. 生成 SSH 密钥对

在终端中运行以下命令：

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

按提示操作，一般直接回车使用默认设置即可。

### 2. 查看并复制公钥

```bash
cat ~/.ssh/id_ed25519.pub
```

复制输出的全部内容（从 `ssh-ed25519` 开始到邮箱地址结束）。

### 3. 添加公钥到 GitHub

1. 登录 GitHub 账户
2. 点击右上角头像 → **Settings**
3. 选择 **SSH and GPG keys**
4. 点击 **New SSH key**
5. 粘贴公钥内容，添加标题（如 "My Laptop"）
6. 点击 **Add SSH key**

### 4. 测试 SSH 连接

```bash
ssh -T git@github.com
```

如果看到欢迎信息，说明配置成功。

---

## 上传项目到 GitHub

### 1. 初始化本地仓库

进入项目文件夹：

```bash
cd /path/to/your/project
```

初始化 Git 仓库：

```bash
git init
```

这会在当前目录下创建 `.git` 子目录，将此文件夹转换为一个 Git 仓库。

### 2. 添加文件到暂存区

```bash
git add .
```

此命令会将当前目录下所有文件的快照添加到"暂存区"，为下一次提交做准备。

### 3. 创建提交

```bash
git commit -m "Initial commit: 项目初始化"
```

此命令将暂存区中的所有内容创建为一个新的提交，并附加一条描述性信息。

### 4. 关联远程仓库

在 GitHub 上创建一个新的空仓库，然后关联：

```bash
git remote add origin git@github.com:username/repository-name.git
```

### 5. 推送到 GitHub

```bash
git branch -M main
git push -u origin main
```

操作成功后，刷新 GitHub 仓库页面，所有文件将显示在其中。

---

## 常用命令

### 查看远程仓库
```bash
git remote -v
```

### 查看状态
```bash
git status
```

### 添加特定文件
```bash
git add filename.txt
```

### 查看提交历史
```bash
git log
```

---

## 常见问题

### 1. Permission denied (publickey)
- 检查 SSH 密钥是否正确添加
- 确认使用的是私钥路径

### 2. 远程仓库已存在
- 使用 `git remote set-url origin` 更新远程地址

### 3. 推送被拒绝
- 检查分支名称是否正确
- 确认有写入权限

---

## 参考资料

- [GitHub SSH 密钥配置官方文档](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [Git 官方文档](https://git-scm.com/doc)

---

---

## 原文链接

本文原载于 CSDN：[如何为本地计算机配置 github-ssh 密钥以便于上传到云端](https://blog.csdn.net/weixin_43326110/article/details/146298348)

*最后更新：2026 年 3 月*
