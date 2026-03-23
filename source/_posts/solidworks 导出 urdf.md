---
title: SolidWorks 导出 URDF 教程
date: 2024-04-08 00:00:00
updated: 2026-03-22 00:00:00
tags: [SolidWorks, URDF, Simscape, 机器人建模]
categories: 技术分享
---

## SolidWorks 导出 URDF 教程

---

## 1. SolidWorks 中导出 URDF 文件

### 安装 SW2URDF 插件

首先需安装 SolidWorks 转 URDF 的插件（如 SW2URDF），该工具由 ROS 社区提供，支持将装配体转换为 URDF 格式。

```bash
# 插件下载地址通常为 ROS 官方或 GitHub 仓库
```

### 配置关节与连杆

在 SolidWorks 装配体中，需明确定义机器人模型的**关节类型**（旋转、平移等）和**连杆质量属性**。右键点击装配体中的运动部件，通过插件菜单分配 `<link>` 和 `<joint>` 标签，并填写惯性参数（质量、质心、转动惯量）。

### 导出 URDF

完成配置后，通过 `File > Export as URDF` 生成 URDF 文件及配套的 STL 网格文件。确保导出时坐标系与 ROS 标准（Z 轴向上）一致。

---

## 2. 导入 URDF 到 Simscape

### 使用 MATLAB 的 `smimport` 函数

在 MATLAB 命令行中运行以下代码，将 URDF 转换为 Simscape 模型：

```matlab
smimport('robot_urdf.urdf');
```

此函数会自动解析 URDF 并生成包含多体组件的 Simulink 模型。

### 调整模型参数

检查生成的 Simscape 模型：

- **单位转换**：SolidWorks 默认单位为毫米，需转换为 Simscape 的米制单位。
- **关节约束**：确认旋转/平移关节的初始位置和阻尼参数。
- **几何体路径**：若 STL 文件路径丢失，需手动关联几何文件。

---

## 3. 仿真与验证

### 添加驱动与传感器

在 Simulink 中为关节添加执行器（如扭矩输入）和传感器（如位置反馈），构建闭环控制逻辑。

### 运行仿真

使用默认求解器（如 ODE15s）进行动力学仿真，观察模型运动是否符合预期。若出现异常抖动，可调整关节刚度或惯性参数。

---

## 常见问题与优化建议

- **URDF 导出失败**：检查装配体是否完全约束，避免自由浮动的部件。
- **仿真不稳定**：尝试减小仿真步长或启用 Simscape 的 `Local Solver` 模式。
- **性能优化**：简化 STL 网格复杂度或替换为凸包几何体。

---

---

## 原文链接

本文原载于 CSDN：[SolidWorks 导出 URDF 教程](https://blog.csdn.net/weixin_43326110/article/details/137438340)

*最后更新：2026 年 3 月*
