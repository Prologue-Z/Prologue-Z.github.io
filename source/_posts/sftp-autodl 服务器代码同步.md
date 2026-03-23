---
title: 通过 SFTP 将本地代码在 Autodl 服务器上运行的工作流
date: 2025-07-11 00:00:00
updated: 2026-03-22 00:00:00
tags: [SFTP, VS Code, AutoDL, 服务器配置]
categories: 技术分享
---

## 目标

配置 Visual Studio Code，实现本地项目文件与 AutoDL 服务器之间的高效、自动同步，让你可以在本地舒适地编写代码，同时代码能够即时在服务器上更新，为运行和调试做好准备。

---

## 核心技术栈

### 编辑器
- **Visual Studio Code (VS Code)**

### VS Code 扩展
- **Remote - SSH** (用于在 VS Code 中打开服务器终端)
- **SFTP (by Natizyskunk)** (用于文件同步)

---

## 第一步：在本地 VS Code 中安装必备扩展

1. 打开你的本地 VS Code
2. 点击左侧的扩展图标
3. 搜索并安装以下两个扩展：
   - **Remote - SSH**: 提供远程连接和终端功能
   - **SFTP**: 负责文件的上传、下载和同步

---

## 第二步：在本地项目文件夹中配置 SFTP

这个配置是针对特定项目的，你需要为你希望同步的每一个本地项目都进行一次配置。

### 生成 SFTP 配置文件

1. 用 VS Code 打开你的本地项目文件夹（例如，包含你的 PyBullet 代码的那个文件夹）
2. 按 `Ctrl+Shift+P`（或者 `Cmd+Shift+P` on macOS）打开命令面板
3. 输入 `SFTP: Config` 并回车
4. 这会在你的项目根目录下自动创建一个 `.vscode` 文件夹，并在其中生成一个名为 `sftp.json` 的文件

### 编辑 sftp.json 文件

将文件内容修改为以下模板，并根据你的 AutoDL 实例信息填写：

```json
{
  // --- 核心连接配置 ---
  "name": "AutoDL Server", // 连接的别名，可自定义
  "host": "ssh.autodl.com", // AutoDL 的 SSH 主机名
  "protocol": "sftp", // 使用 SFTP 协议
  "port": 12345, // 你的实例的 SSH 端口号
  "username": "root", // 用户名
  "password": "your_server_password", // 你的服务器密码 (见下方安全提示)
  "remotePath": "/root/my_pybullet_project", // 你希望代码同步到服务器的哪个目录

  // --- 自动化与同步配置 ---
  "uploadOnSave": true, // 关键！在本地保存文件时，自动上传。
  "watcher": {
    "files": "**/*",
    "autoUpload": true,
    "autoDelete": true
  },

  // --- 忽略文件配置 (非常重要！) ---
  // 避免上传不必要或敏感的文件
  "ignore": [
    "**/.vscode/**", // 忽略 VS Code 自身的配置文件
    "**/.git/**", // 忽略整个 Git 仓库历史
    "**/__pycache__/**", // 忽略 Python 缓存文件
  ]
}
```

### 安全提示

- 直接在 `sftp.json` 中明文存储密码虽然方便，但有安全风险
- 更安全的替代方案是使用 SSH 密钥对进行免密登录。配置好免密登录后，你可以从 `sftp.json` 中移除 `"password": "..."` 这一行。SFTP 扩展会自动尝试使用你的 SSH 密钥

---

## 第三步：日常开发工作流

配置完成后，你的开发流程将变得非常顺滑。

### 编写代码

在本地 VS Code 中像往常一样打开、编辑你的项目文件。

### 自动同步

当你按下 `Ctrl+S`（或 `Cmd+S`）保存文件时，SFTP 扩展会在右下角状态栏显示一个小的加载动画，并在几秒内将修改过的文件自动上传到你在 `remotePath` 中指定的服务器目录。

### 运行与调试（结合 VNC 教程）

1. 在 SFTP 插件中右键在本界面打开 SSH 终端，或新打开一个 VScode 使用 Remote - SSH 扩展连接到你的 AutoDL 服务器，在 VS Code 中打开一个服务器终端
2. 在这个终端里，`cd` 到你之前配置的 `remotePath`（例如 `cd /root/my_pybullet_project`）
3. 现在，你可以运行你的 Python 脚本了。因为本地文件已自动同步，所以你总是在运行最新版本的代码

```bash
# 激活环境
conda activate myenv

# 设置显示器
export DISPLAY=:1

# 直接运行（因为你的环境已原生支持硬件加速）
python your_updated_script.py
```

4. 切换到你的 TurboVNC 客户端窗口，观察程序的图形化输出

### 手动同步与下载结果

**上传整个项目**: 如果你想一次性上传整个项目，可以在 VS Code 的文件浏览器中右键点击项目根目录，选择 `SFTP: Upload Folder`

**下载训练结果**:
1. 在 VS Code 左侧边栏找到 SFTP 视图并展开
2. 浏览到服务器上存放结果的文件夹（如 `results/` 或 `checkpoints/`）
3. 右键点击该文件夹，选择 `Download`。文件将被下载到你本地项目的对应位置

---

---

## 原文链接

本文原载于 CSDN：[通过 SFTP 将本地代码在 Autodl 服务器上运行的工作流](https://blog.csdn.net/weixin_43326110/article/details/136904763)

*最后更新：2026 年 3 月*
