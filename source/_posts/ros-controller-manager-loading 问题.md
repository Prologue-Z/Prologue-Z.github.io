---
title: 【ROS】controller_manager 卡在 loading_controller 问题
date: 2024-06-11 00:00:00
updated: 2026-03-22 00:00:00
tags: [ROS, controller_manager, ros_control, 问题排查]
categories: 技术分享
---

## 项目场景

最近为自己的机械臂基于 `hardware_interface` 写了一个驱动，并希望接入 ros_control 使用 moveit 进行控制，但是在 controller_manager 加载控制器的时候停在了 `loading_controller` 上。

---

## 问题描述

在 launch 中导入 `joint_state_controller` 控制器：

```xml
<node name="rf_hybrid_arm_controller_spawner" 
      pkg="controller_manager" 
      type="spawner" 
      args="joint_state_controller rf_hybrid_arm_controller" 
      respawn="false" 
      output="screen"/>
```

在驱动中进行了一个这样的循环：

```cpp
ros::init(argc, argv, "rf_hybrid_arm_driver_node");

RFHybridArmHW RFARM;
controller_manager::ControllerManager cm(&RFARM);
ROS_INFO("Arm bring up successfully");

// 控制循环
ros::Rate loop_rate(RFARM.control_rate); // 控制频率为 50Hz
ros::Duration d(0.05);
while (ros::ok())
{
  RFARM.read();
  cm.update(ros::Time::now(), d);
  RFARM.write();
  loop_rate.sleep();
}

return 0;
```

这个基本就是参照 ros_control 的官方教程编写的。

---

## 问题分析

controller_manager 卡在 `loading_controller` 通常有以下几个原因：

1. **控制器插件未正确注册** - 检查 `pluginlib` 配置文件
2. **控制器类未正确继承** - 检查是否继承自 `controller_interface::ControllerBase`
3. **依赖未安装** - 检查 `CMakeLists.txt` 和 `package.xml`
4. **命名空间问题** - 检查 ROS 命名空间配置

---

## 解决方案

### 1. 检查 pluginlib 配置

确保在 `package.xml` 中添加了正确的依赖：

```xml
<build_depend>controller_interface</build_depend>
<exec_depend>controller_interface</exec_depend>
<build_export_depend>controller_interface</build_export_depend>
```

### 2. 检查控制器类定义

确保控制器类正确继承并实现了必要的方法：

```cpp
class MyController : public controller_interface::Controller<RFHybridArmHW>
{
public:
  virtual bool init(RFHybridArmHW *robot, ros::NodeHandle &n) override;
  virtual void starting(const ros::Time& time) override;
  virtual void update(const ros::Time& time, const ros::Duration& period) override;
  virtual void stopping(const ros::Time& time) override;
};
```

### 3. 检查 CMakeLists.txt

确保正确链接了相关库：

```cmake
find_package(controller_interface REQUIRED)
find_package(pluginlib REQUIRED)

add_library(my_controller src/my_controller.cpp)
target_link_libraries(my_controller
  ${controller_interface_LIBRARIES}
  ${pluginlib_LIBRARIES}
)
```

### 4. 检查 launch 文件

确保控制器名称和类型正确：

```xml
<node name="controller_spawner" 
      pkg="controller_manager" 
      type="spawner" 
      args="joint_state_controller my_controller" 
      respawn="false" 
      output="screen"/>
```

---

## 调试技巧

### 1. 查看详细日志
```bash
roslaunch your_package your_launch_file.launch --screen
```

### 2. 检查控制器列表
```bash
rosservice call /controller_manager/list_controllers
```

### 3. 检查插件注册
```bash
rospack plugins --attrib=plugin controller_interface
```

---

## 总结

controller_manager 卡在 `loading_controller` 通常是由于控制器插件未正确注册或控制器类定义有问题。按照上述步骤逐一排查，一般都能解决问题。

---

---

## 原文链接

本文原载于 CSDN：[【ROS】controller_manager 卡在 loading_controller](https://blog.csdn.net/weixin_43326110/article/details/139603881)

*最后更新：2026 年 3 月*
