---
title: 在 Ubuntu 中固定 USB 设备的串口号
date: 2025-07-02 00:00:00
updated: 2026-03-22 00:00:00
tags: [Ubuntu, USB, 串口，udev 规则]
categories: 技术分享
---

## 问题背景

在 Ubuntu 系统中，USB 串口设备的设备名（如 `ttyUSB0`、`ttyUSB1`）可能会在每次插拔或重启后发生变化，这给需要固定串口号的应用程序带来不便。通过创建 udev 规则，可以根据 USB 设备的 Vendor ID 和 Product ID 来固定串口号。

---

## 步骤一：获取设备信息

### 1. 查看 USB 设备列表

```bash
lsusb
```

记录设备的 Vendor ID 和 Product ID（例如：`ID 0403:6001`）

### 2. 获取详细属性

```bash
udevadm info -a /dev/ttyUSBX
```

替换 `X` 为实际设备号。结果一般如下。

---

## 步骤二：创建 udev 规则文件

```bash
sudo gedit /etc/udev/rules.d/usb-serial.rules
```

其中 `usb-serial.rules` 文件名可以自定义。

---

## 步骤三：编写规则模板

### 示例规则

```bash
# 设备 1 规则（示例：绑定到 ttyUSB_CAMERA）
KERNEL=="ttyUSB*", SUBSYSTEMS=="usb", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", MODE="0666", SYMLINK+="ttyUSB_CAMERA"

# 设备 2 规则（示例：绑定到 ttyUSB_SENSOR）
KERNEL=="ttyUSB*", SUBSYSTEMS=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", MODE="0666", SYMLINK+="ttyUSB_SENSOR"
```

### 规则说明

- `SUBSYSTEMS=="usb"` 也是一个过滤条件。
- `KERNEL=="ttyUSB*"` 是正确的，表示无论是 `ttyUSB*`，符合后续芯片型号的就可以被指向 `SYMLINK+="ttyUSB_SENSOR"`。
- 但是如果给定了 `ttyUSB1` 或 `0`，那就只有满足上述条件才能通过 `ttyUSB_SENSOR` 找到。

---

## 步骤四：生效规则

### 1. 重新加载规则

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

### 2. 查看设备名称更改状况

```bash
ls -l /dev | grep ttyUSB
```

---

## 参考资料

- [Ubuntu18.04 绑定 USB 串口设备 ttyUSBx - 知乎](https://zhuanlan.zhihu.com/p/664267108)
- [ubuntu 下绑定 USB 设备的串口名称（KERNELS 硬件端口号绑定）-CSDN 博客](https://blog.csdn.net/weixin_40639095/article/details/108490329)

上述是通过识别目标 usb 设备芯片以及相关信息来固定串口，或者也可以通过 pc 端固定物理串口。

---

---

## 原文链接

本文原载于 CSDN：[在 Ubuntu 中固定 USB 设备的串口号](https://blog.csdn.net/weixin_43326110/article/details/146723938)

*最后更新：2026 年 3 月*
