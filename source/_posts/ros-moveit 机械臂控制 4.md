---
title: 【ROS】利用 moveit 控制自制机械臂（4）——修改 moveit 配置助手生成的配置文件
date: 2024-01-13 00:00:00
updated: 2026-03-22 00:00:00
tags: [ROS, MoveIt, 机械臂控制，配置文件]
categories: 技术分享
---

## 前言

在之前我们已经使用 moveit 配置助手生成了自制的机械臂的配置文件，但是由于缺少驱动，因此只能使用他的 demo 界面来控制虚拟的 rviz 中的机械臂，而无法控制实体机械臂。

因此这一部分我们就要把在（3）中建立的机器人驱动嵌入 moveit 生成的配置文件中，从而达成用 moveit 配置助手生成的 demo.launch 控制实体机械臂的目的。

---

## 需要修改的两个部分

首先对于直接生成的 moveit 配置文件，根源上需要更改的主要两个部分：

### 1. 接受 moveit 中的 action 指令

接受 moveit 中的 launch 文件生成的 `follow_joint_trajectory` 的 action 指令去驱动机械臂，这里注意驱动中与 moveit 中对于 `follow_joint_trajectory` 的 action 的名字一定要一致，否则会报错，这一点在之前我们在建立驱动时已经成功了，即读取 goal 信息，用来控制电机转动。

常见错误信息：
```
[ERROR] [1649324583.023988413]: Unable to identify any set of controllers that can actuate the specified joints: [ elbow_joint shoulder_lift_joint shoulder_pan_joint wrist_1_joint wrist_2_joint wrist_3_joint ]
[ERROR] [1649324583.024022449]: Known controllers and their joints:
[ERROR] [1649324583.024088233]: Apparently trajectory initialization failed
```

### 2. 读取电机状态发布到 movegroup

另一个就是读取电机的状态发布到 movegroup 中使得 moveit 机器人状态与实际机器人一致。这一点虽然我们已经在机器人驱动中把机器人状态发布出来了，但是这里还是需要修改配置文件中的 launch 文件进行修改让 moveit 知道从哪里接受实际的机器人状态，事实上（4）主要就是做的这一工作。

---

## 需要修改的文件

首先我们先理清楚需要修改的文件内容：

```
demo.launch 
  → movegroup.launch 
    → trajectory_execution.launch 
      → $(arg moveit_controller_manager)_moveit_controller_manager.launch 
        → $(arg moveit_controller_manager)_controllers.yaml
```

其中 `moveit_controller_manager` 可以等于 `fake`、`simple`、`ros_control`，这里先以 `simple` 为例实现功能，后续尝试升级为 `ros_control`。

上面是运行 `demo.launch` 需要使用的 launch 文件，当然并非这些文件都需要修改，大部分都已经被 moveit 配置助手给设计的很完善了，并不需要什么修改。

这里为了避免修改源文件影响后续的其他工作，我将这一次测试成功的几个 launch 都复制一份并增加 `_actual` 后缀。可以看到共有三个文件需要修改。

---

## 1. demo_actual.launch（修改 demo.launch）

```xml
<!-- Choose controller manager: fake, simple, or ros_control -->
<arg name="moveit_controller_manager" default="simple" />
```

这里 `moveit_controller_manager` 设定为 `simple`，然后把 `move_group.launch` 改为 `move_group_actual.launch`。

```xml
<!-- Run the main MoveIt executable without trajectory execution (we do not have controllers configured by default) -->
<include file="$(dirname)/move_group_actual.launch">
  <arg name="allow_trajectory_execution" value="true"/>
  <arg name="moveit_controller_manager" value="$(arg moveit_controller_manager)" />
  <arg name="fake_execution_type" value="$(arg fake_execution_type)"/>
  <arg name="info" value="true"/>
  <arg name="debug" value="$(arg debug)"/>
  <arg name="pipeline" value="$(arg pipeline)"/>
  <arg name="load_robot_description" value="$(arg load_robot_description)"/>
</include>
```

---

## 2. move_group_actual.launch（修改 move_group.launch）

```xml
<!-- Trajectory Execution Functionality -->
<include ns="move_group" file="$(dirname)/trajectory_execution_actual.launch.xml" if="$(arg allow_trajectory_execution)">
  <arg name="moveit_manage_controllers" value="true" />
  <arg name="moveit_controller_manager" value="$(arg moveit_controller_manager)" />
  <arg name="fake_execution_type" value="$(arg fake_execution_type)" />
</include>
```

这里其实不需要做什么改动，但是由于在后续的 `trajectory_execution.launch` 中进行了改动，因此需要把 `trajectory_execution.launch` 改为 `trajectory_execution_actual.launch`。

---

## 3. trajectory_execution_actual.launch（修改 trajectory_execution.launch）

```xml
<!-- When determining the expected duration of a trajectory, this multiplicative factor is applied to get the allowed duration of execution -->
<param name="trajectory_execution/allowed_execution_duration_scaling" value="6"/> <!-- default 1.2 -->
```

把这个参数从 `1.2` 调整为 `6`，参数是调整容错的，有时候机器人的实际响应时间并没有规划的那么快，这里调大一点增加一点容错，使得机器人的响应时间即使很慢也能慢慢执行完成。

---

## 实际运行效果

以上就完成了更改，最后展示一下实际运行状态下各个节点之间的通讯关系供参考对照。

---

## 环境信息

- **ROS 版本**: noetic
- **日期**: 2024.1.13

---

## 参考资料

- [ROS Moveit 配置全网最详细教程-CSDN 博客](https://blog.csdn.net/m0_56661101/article/details/131415296)
- [Moveit 实际的机械臂控制（4）修改机械臂配置文件实现真实控制-CSDN 博客](https://blog.csdn.net/qq_33328642/article/details/117843831)

---

---

## 原文链接

本文原载于 CSDN：[【ROS】利用 moveit 控制自制机械臂（4）——修改 moveit 配置助手生成的配置文件](https://blog.csdn.net/weixin_43326110/article/details/137371920)

*最后更新：2026 年 3 月*
