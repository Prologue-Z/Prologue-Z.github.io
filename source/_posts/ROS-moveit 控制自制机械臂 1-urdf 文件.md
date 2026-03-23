---
title: 【ROS】利用 moveit 控制自制机械臂（1）——URDF 文件编写
date: 2023-12-21 00:00:00
updated: 2026-03-22 00:00:00
tags: [ROS, MoveIt, 机械臂控制，URDF]
categories: 技术分享
---

## 前言

建立机械臂的 urdf 文件为利用 moveit 驱动自制机械臂的基础，但是相关资料已有很多相关大佬进行过说明，方法通用，无需重复造轮子，这里给一些参考资料即可。

---

## URDF 编写要点

### 1. 连杆定义

```xml
<link name="base_link">
  <visual>
    <geometry>
      <cylinder length="0.1" radius="0.05"/>
    </geometry>
  </visual>
  <collision>
    <geometry>
      <cylinder length="0.1" radius="0.05"/>
    </geometry>
  </collision>
  <inertial>
    <mass value="1.0"/>
    <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
  </inertial>
</link>
```

### 2. 关节定义

```xml
<joint name="joint1" type="revolute">
  <parent link="base_link"/>
  <child link="link1"/>
  <origin xyz="0 0 0.1" rpy="0 0 0"/>
  <axis xyz="0 0 1"/>
  <limit lower="-3.14" upper="3.14" effort="10" velocity="1.0"/>
</joint>
```

---

## 参考资料

- [URDF 官方教程](http://wiki.ros.org/urdf/Tutorials)
- [MoveIt 配置教程](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_moveit/quickstart_in_moveit_tutorial.html)

---

---

## 原文链接

本文原载于 CSDN：[【ROS】利用 moveit 控制自制机械臂（1）](https://blog.csdn.net/weixin_43326110/article/details/135128138)

*最后更新：2026 年 3 月*
