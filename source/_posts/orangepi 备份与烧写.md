---
title: 【香橙派】如何备份与烧写香橙派的系统
date: 2024-03-20 00:00:00
updated: 2026-03-22 00:00:00
tags: [香橙派，系统备份，系统烧写，RKDevTool]
categories: 技术分享
---

## 前言

项目中使用香橙派作为工控主机，在香橙派提供的默认 Ubuntu 系统基础上安装了许多适配的软件和自己的代码，每交付一次就重新折腾一次有些太麻烦，这里进行一个备份与烧写的操作复制自己的香橙派。

---

## 配置

- **型号**: 香橙派 5 Plus eMMC 64GB
- **系统**: 在官方提供的 Orangepi5plus_1.0.8_ubuntu_focal_desktop_xfce_linux5.10.160.img 基础上进行了各种软件的安装与修改

---

## 操作步骤

### 备份

1. **准备一个 TF 卡**，可存储即可，作为备份的载体

2. **cd 进入 TF 卡目录**

3. **简易指令**：

```bash
sudo dd if=/dev/mmcblk1 of=./myimg.img status=progress
```

其中：
- `if` 为输入的目录
- `of` 为输出的目录

4. **复杂指令**：

```bash
sudo dd if=/dev/mmcblk1 conv=sync,noerror bs=1M status=progress | gzip -c > ./myimg.img.gz
```

相对于简易指令，复杂指令多了一些设定：
- `bs` 为块的大小
- `status=progress` 表示显示进度
- `| gzip -c > ./mycard1.img.gz` 表示对镜像进行压缩，可压缩也可以不压缩

---

## 烧录

参考香橙派官方用户手册 2.5.1，使用"使用 RKDevTool 烧录 Linux 镜像到 eMMC 中的方法"。

![RKDevTool 烧录界面](/images/posts/orange-pi-backup/01-rkdevtool.jpg)

*RKDevTool 烧录工具界面，显示设备连接状态和烧录选项*

### 注意事项

⚠️ **文件路径不要有中文！**

---

## 总结

通过备份与烧写操作，可以：
- ✅ 快速复制已配置好的系统
- ✅ 避免每次交付都重新安装软件
- ✅ 提高工作效率

---

## 参考资料

- 香橙派官方用户手册 2.5.1
- [使用 RKDevTool 烧录 Linux 镜像到 eMMC 中的方法](https://wiki.orangepi.cn/zh-cn/OrangePi5Plus)

---

---

## 原文链接

本文原载于 CSDN：[【香橙派】如何备份与烧写香橙派的系统](https://blog.csdn.net/weixin_43326110/article/details/136852823)

*最后更新：2026 年 3 月*
