---
title: 【ROS】利用 moveit 控制自制机械臂（2）——通过 MoveIt Setup Assistant 生成机械臂的配置文件
date: 2024-01-13 00:00:00
updated: 2026-03-22 00:00:00
tags: [ROS, MoveIt, 机械臂控制，运动规划]
categories: 技术分享
---

## 启动 MoveIt Setup Assistant

通过 rviz 测试 xacro 文件无误之后，准备开始进行 moveit 的设置，首先安装 moveit（这里我的版本是 ubuntu20.04，所以 ros 版本是 noetic）：

```bash
sudo apt-get install ros-noetic-moveit
```

打开 MoveIt Setup Assistant（运行前先运行 roscore）：

```bash
rosrun moveit_setup_assistant moveit_setup_assistant
```

然后导入之前设定好的 xacro。

---

## 配置步骤

### 1. 碰撞检测矩阵

设定碰撞检测矩阵，直接点生成就好，默认的参数基本可以满足大多数场景。

### 2. 虚拟关节

添加一个虚拟关节，用来把机械臂底端固定在世界坐标系。

### 3. Planning Groups

添加 planning groups。

### 4. 添加 arm group

起个名字然后，选 kdl 运动学 solver，ompl planning 选 rrt，其他的默认。

这里选择 kin.chain 也是一样的，选上所有在 arm 的 joint 即可，这里选添加 joint，把所有臂上的 joint 都加上去即可，先不用管 mimic 之类的设定。

### 5. 夹爪配置

夹爪参照机械臂部分进行同样的设定。

### 6. 机器人 Pose

添加几个定义的机器人 pose 方便后续的调试与使用。

- **臂的 base_pose**（竖直状态）
- **臂的 test_pose**（随机给的后续用来测试）
- **夹爪的 open_pose**
- **夹爪的 close_pose**

### 7. 末端执行器

注意这里，parent link 选择臂的末端 link，parent group 就是空白。

### 8. 被动关节

添加被动关节，本例有大量被动关节，例如 mimic 中的，（经过测试，添加与否都不影响后续的使用，避免多余的麻烦，这里之后都不添加被动关节）。

### 9. 控制器配置

生成 ros controller。

simulation 不用管。

3d perception 暂时也不选，之后可考虑加上深度相机后选上。

### 10. 生成配置文件

点击生成配置功能包，包的名字填成臂的名称_moveit_config 即可。

---

## 测试验证

运行生成的 demo 测试生成的 moveit 配置文件有没有问题：

```bash
roslaunch carm_6dof_moveit_config demo.launch
```

选择 goal state 为 test_pose，点击 plan&execute 可以看到规划并运动成功。当然这里还没有连结真实机械臂，所以只是通过一个虚拟的 joint publisher 来模仿机械臂已经运动了。后面我们会通过修改 moveit 的文件来使之能驱动真实机械臂。

---

## 参考资料

- [【学习笔记】ROS2 纯小白 - MoveIt! (humble) 引入新的机器人模型 - 知乎](https://zhuanlan.zhihu.com/p/616711291?utm_id=0)
- [ROS 运动规划 (Motion Planning): MoveIt! 与 OMPL_ros 运动控制世界排名-CSDN 博客](https://blog.csdn.net/improve100/article/details/50619925)
- [ROS-Moveit! 配置 (一)_moveit! 里必须配置夹爪吗-CSDN 博客](https://blog.csdn.net/weixin_51002159/article/details/131600920)
- [moveit_setup_assistant - 知乎](https://zhuanlan.zhihu.com/p/575907270)

---

---

## 原文链接

本文原载于 CSDN：[【ROS】利用 moveit 控制自制机械臂（2）——通过 MoveIt Setup Assistant 生成机械臂的配置文件](https://blog.csdn.net/weixin_43326110/article/details/135319255)

*最后更新：2026 年 3 月*
