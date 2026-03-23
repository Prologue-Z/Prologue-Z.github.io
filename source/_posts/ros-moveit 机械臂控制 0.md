---
title: 【ROS】利用 moveit 控制自制机械臂（0）—— 前言
date: 2024-01-10 00:00:00
updated: 2026-03-22 00:00:00
tags: [ROS, MoveIt, 机械臂控制，运动规划]
categories: 技术分享
---

## 前言

本系列教程将介绍如何使用 ROS MoveIt 控制自制的机械臂。这是一个完整的系列，从基础配置到实际控制，循序渐进地讲解整个流程。

---

## 系列文章目录

- **（0）前言** - 本系列教程概述（本文）
- **（1）利用 moveit 控制自制机械臂（1）** - URDF 文件编写
- **（2）利用 moveit 控制自制机械臂（2）** - MoveIt Setup Assistant 配置文件生成
- **（3）利用 moveit 控制自制机械臂（3）** - 机器人驱动编写
- **（4）利用 moveit 控制自制机械臂（4）** - 修改 moveit 配置文件
- **（5）利用 moveit 控制自制机械臂（5）** - 实际控制测试

---

## 基本思路

ROS MoveIt 是一个强大的运动规划框架，要使用其控制机械臂，一般步骤为：

1. **配置机械臂的 URDF 模型**
2. **设置运动规划场景**
3. **编写控制代码实现运动规划与执行**

---

## 具体方法和教程

### 1. 创建工作空间与功能包

```bash
mkdir -p delta_arm_ws/src
cd delta_arm_ws/src
ros2 pkg create --build-type ament_cmake delta_arm_control \
  --dependencies rclcpp control_msgs geometry_msgs moveit_servo moveit_core moveit_msgs planning_scene_monitor tf2_ros
```

参考创建 Panda 机械臂控制功能包的方法，这里创建了用于 Delta 机械臂控制的功能包。

### 2. 配置机械臂 URDF 模型

创建 Delta 机械臂的 URDF（Unified Robot Description Format）文件，描述机械臂的连杆、关节等信息。将该文件放置在功能包的 `urdf` 目录下。

### 3. 设置运动规划场景

使用 MoveIt Setup Assistant 工具为机械臂生成配置文件。运行以下命令启动该工具：

```bash
ros2 run moveit_setup_assistant moveit_setup_assistant
```

在工具中导入 URDF 文件，配置关节、规划组、末端执行器等信息，最后生成配置包。

### 4. 编写控制代码

在 `delta_arm_control` 功能包的 `src` 目录下创建控制代码文件。以下是一个简单示例：

```cpp
#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("delta_arm_control_node");

  moveit::planning_interface::MoveGroupInterface move_group(node, "delta_arm_group");

  // 设置目标位姿
  geometry_msgs::msg::Pose target_pose;
  target_pose.position.x = 0.5;
  target_pose.position.y = 0.0;
  target_pose.position.z = 0.2;
  move_group.setPoseTarget(target_pose);

  // 进行运动规划
  moveit::planning_interface::MoveGroupInterface::Plan my_plan;
  bool success = (move_group.plan(my_plan) == moveit::core::MoveItErrorCode::SUCCESS);

  // 执行运动
  if (success) {
    move_group.execute(my_plan);
  }

  rclcpp::shutdown();
  return 0;
}
```

在 `CMakeLists.txt` 中添加编译规则：

```cmake
add_executable(delta_arm_control src/delta_arm_control.cpp)
ament_target_dependencies(delta_arm_control rclcpp moveit_ros_planning_interface)
install(TARGETS
  delta_arm_control
  DESTINATION lib/${PROJECT_NAME}
)
```

编译并运行代码：

```bash
cd delta_arm_ws
colcon build
source install/setup.bash
ros2 run delta_arm_control delta_arm_control
```

---

## 实时速度控制

若要实现实时速度控制，可参考通过 ROS2 topic 手动发布速度指令的方法。例如在笛卡尔空间中移动末端执行器：

```bash
ros2 topic pub /servo_server/delta_twist_cmds geometry_msgs/msg/TwistStamped \
  '{header: {frame_id: "base_link"}, twist: {linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}}'
```

这样可使机械臂末端执行器在笛卡尔空间按指定速度移动。

---

## 后续文章

本系列的后续文章将详细介绍每一步的具体操作和注意事项，敬请期待！

---

---

## 原文链接

本文原载于 CSDN：[【ROS】利用 moveit 控制自制机械臂（0）](https://blog.csdn.net/weixin_43326110/article/details/135127988)

*最后更新：2026 年 3 月*
