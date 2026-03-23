---
title: 制作 Ubuntu 镜像及烧录教程
date: 2024-04-03 00:00:00
updated: 2026-03-22 00:00:00
tags: [Ubuntu, Systemback, 系统备份，镜像制作，烧录]
categories: 技术分享
---

## 前言

最近更换了 NUC 主机作为机器人的控制主机，为了避免之前在安装操作系统过程中把系统搞崩了的惨状，决定养成定期备份系统的好习惯，这就需要掌握制作系统镜像及烧录的能力。

### 工作环境

- **电脑**: NUC13 竞技场峡谷 i7-1360P 薄款
- **系统版本**: Ubuntu 20.04

---

## 1. 安装 Systemback 软件

这里使用的是韩国人的 Systemback 1.9.4 版本，亲测可用。

### 1.1 添加 APT 仓库并安装

```bash
# Add APT
curl -sL https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash

# Install package
sudo apt install systemback
```

### 1.2 卸载其他版本（如有）

如果安装了别的版本的 systemback，可以先卸载：

```bash
sudo apt purge systemback
```

然后修改一下 apt 仓库源，把之前的 systemback 源给删掉：

```bash
sudo gedit /etc/apt/sources.list
```

然后 update 一下重新安装即可。这样我们就完成了 Systemback 的安装。用管理员身份启动：

```bash
sudo systemback
```

如上图所示，这个软件除了制作镜像还可以设定还原点进行系统的还原操作，十分实用。

---

## 2. 备份 sblive 系统

下面开始基于这个软件进行系统镜像的制作，点击创建 Live 系统。

然后选上包含用户数据，点击创建新的。在系统名称处也可以自定义导出的 sblive 文件的名称，如果 auto 就会是如右上角一样（右上角是我已经进行了一次备份）以前缀 + 时间进行命名。

如图所示，开始了 Live 系统的备份，最终会导出一个 sblive 格式的文件。其实这一文件在 Systemback 上就可以制作系统启动 U 盘了，但是为了方便系统完全崩到开不了机的情况，还是转换为更通用的 iso 文件。

---

## 3. 安装 cdrtools

为了将在转换之前需要进行 cdrtools 软件的安装，这里完全复制自参考资料。

这里直接贴出指令，挨个运行即可：

```bash
sudo apt install aria2

aria2c -s 10 https://nchc.dl.sourceforge.net/project/cdrtools/alpha/cdrtools-3.02a07.tar.gz

tar -xvf cdrtools-3.02a07.tar.gz

cd cdrtools-3.02

make

sudo make install
```

中间会有一些 warning 啥的，但是最后运行时候似乎也不影响。

---

## 4. 转换为 iso 格式

下面开始真正进行格式的转换。

### 4.1 解压 .sblive 文件

```bash
mkdir sblive

tar -xf /home/systemback_live_2018-10-15.sblive -C sblive
```

其中那个 `systemback_live_2018-10-15.sblive` 换成你自己的 sblive 文件名即可。

### 4.2 重命名文件

然后重命名解压出来的部分文件，虽然也不知道为啥，但是照做就是：

```bash
mv sblive/syslinux/syslinux.cfg sblive/syslinux/isolinux.cfg

mv sblive/syslinux sblive/isolinux
```

### 4.3 生成 iso 文件

最后直接生成即可：

```bash
/opt/schily/bin/mkisofs -iso-level 3 -r -V sblive -cache-inodes -J -l -b isolinux/isolinux.bin -no-emul-boot -boot-load-size 4 -boot-info-table -c isolinux/boot.cat -o sblive.iso sblive
```

这里 `sblive.iso` 是生成的 iso 文件名，可以自定义。

至此我们就完成了 iso 的转换，然后过程中一些无用的文件就可以删除了。比如解压出的 sblive 文件夹。sblive 文件也可以删除，留着作为备份也行。另外把下载的 cdrtools 的压缩包给删了可以。

---

## 5. 烧录启动硬盘

首先制作 Ventoy 启动 U 盘，这里不再赘述，没有什么值得注意的点。

然后把自己上面做好的镜像拷进去就完成了启动硬盘的制作。

---

## 6. 安装系统

### 6.1 启用安全引导支持

对于系统盘是完全干净的新盘情况下，大概率摁 F10 U 盘启动是不起作用的，需要先摁 F12 进入 BIOS 界面。

然后参照参考资料完成为 Ventoy 启用安全引导支持之后，进行下一步骤。

### 6.2 选择启动盘

把启动硬盘插到 NUC 主机上，启动时候摁 F10，选择 U 盘作为启动盘。

然后会进入这个界面，选择自己的目标 iso 进入。然后 Ventoy 会提供多个启动项选择，这里**一定要注意选择 grub 启动模式**！很多教程都让选择 normal 启动模式，但是根据我测试，使用 Systemback 制作的镜像在 NUC 主机上启动会黑屏卡住不动。

### 6.3 进入系统安装器

然后会进入 Systemback 的引导界面，这里选择系统安装器。

然后会直接进入系统，和你拷贝的系统其实一模一样，输入密码进入后会直接打开 Systemback 的安装系统界面。

### 6.4 解决无法格式化硬盘的 Bug

这里会遇到一个大坑，正常情况（也许很多电脑和版本都是正常情况）直接安装就行，但是我这个经过测试会遇到一个蛋疼的 Bug——无法格式化硬盘。

最终我们也参照参考资料解决了这个问题，也就是手动格式化硬盘。

打开 GParted 软件（没有自己安装，这个很简单），然后把硬盘分区并进行格式化：

- **fat32**，512MiB
- **linux-swap**，32000MiB（和内存大小一致）
- **ext4**，其他所有空间

点对号保存我们就完成了硬盘的格式化。然后我们终于可以愉快的安装系统了。**这里需要重新启动一下主机，重新选择系统安装器**，否则可能会出一些问题。

### 6.5 系统安装

打开 Systemback 软件，点击安装系统，首先是设定用户名密码啥的，这个按照自己需求设定即可。

然后就进入了分区环节，这里我们已经在上面用 GParted 分区并格式化了，所以这里其实只需要设定一下挂载点即可，而且**必须注意一定不要选择格式化**，也就是所有分区下格式一栏不打勾！

挂载点的具体设定为（**一定不要点格式**）：

- **EFI 系统分区**（主分区）512MiB → `/boot/efi`
- **交换空间**（逻辑分区）32000MiB → `SWAP`
- **挂载点/**（主分区）剩余所有容量 → `/`

另外记得选择**传递用户配置文件及用户数据**。点击下一步就可以开始系统的安装，等待进度条结束重启就 ok 啦。

### 6.6 安装后配置

安装完系统开机后可能会找不到 wifi，这是由于没有关闭安全模式，启动的时候摁 F2 进入 BIOS 关闭 Secure Boot 即可。

然后可以顺便把通电自启也打开。

---

## 参考资料

- [Systemback 制作大于 4G 的 Ubuntu 系统镜像 - 冰柠檬的夏天 - 博客园](https://www.cnblogs.com/Pan-xi-yi/p/11830789.html)
- [使用 Systemback 克隆 Ubuntu 系统 - 知乎](https://zhuanlan.zhihu.com/p/375912899)
- [第六课：UBUNTU 的安装 - 哔哩哔哩](https://www.bilibili.com/video/BV1WZ4y167me?p=7)
- [使用 systemback 写入 U 盘-CSDN 博客](https://blog.csdn.net/weixin_39852953/article/details/112769508)
- [Ubuntu18.04 制作系统 ISO 镜像并物理机还原（Systemback） - 知乎](https://www.zhihu.com/tardis/bd/art/576420693)
- [ventoy 启动盘提示 (0x1A) Security Violation 的解决方法 - 微控圈](https://www.mculoop.com/thread-201-1-1.html)

---

---

## 原文链接

本文原载于 CSDN：[制作 ubuntu 镜像及烧录](https://blog.csdn.net/weixin_43326110/article/details/137355778)

*最后更新：2026 年 3 月*
