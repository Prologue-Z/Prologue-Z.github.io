---
title: "连续体机器人环链式运动学模型及在刚柔混合臂中的应用"
description: "环链式运动学模型与刚柔混合臂系统应用，发表于 IEEE ROBIO 2025"
date: 2025-12-01
tags: ["连续体机器人", "环链式运动学", "刚柔混合臂"]
categories: ["科研项目"]
layout: "simple"
---

## 📄 论文信息

**论文标题**: A Cyclotomic-Linked Kinematic Model for Continuum Robots and Its Application in Rigid-Flexible Hybrid Arms

**作者**: Xu Zhang, Sheng Yang, Peng Yuan, Zhibin Song, Tao Sun, David T. Branson, Rong Kang

**发表会议**: IEEE International Conference on Robotics and Biomimetics (ROBIO), Chengdu, China, December 2025

**摘要**: The control of continuum robots is generally based on a kinematic model consisting of the actuation-configuration-task spaces. The nonlinear relationship between the actuation and configuration space makes it challenging to build control systems for continuum robots. This paper introduces the cyclotomic-linked kinematic model (CLKM), a pragmatic modeling approach designed to bridge this integration gap by replacing the configuration space with an intuitive joint space. The cornerstone of CLKM is the establishment of a linear relationship between actuation and joint spaces, which simplifies the control system design. The proposed model is applied to a rigid-flexible hybrid arm system, demonstrating its effectiveness in motion planning and precise control.

[📥 下载 PDF](/files/papers/Zhang%20%E7%AD%89%20-%20A%20Cyclotomic-Linked%20Kinematic%20Model%20for%20Continuum%20Robots%20and%20Its%20Application%20in%20Rigid-Flexible%20Hybri.pdf) | [🔗 DOI](https://doi.org/10.1109/ROBIO66223.2025.11378300)


---


## 🎯 研究背景

连续体机器人的运动学建模需要兼顾精度和计算效率，特别是在刚柔混合臂系统中：

1. **建模精度**: 需要准确描述连续体变形
2. **计算效率**: 实时控制需要高效计算
3. **刚柔耦合**: 刚柔混合臂系统建模复杂


---


## 🔬 研究方法

### 1. 环链式运动学建模

<img class="project-figure" src="/images/projects/cyclotomic-model/01_kinematic_model.png" alt="环链式运动学模型" loading="lazy">

*图 1：环链式运动学模型原理*

提出环链式运动学模型 (Cyclotomic-linked Kinematic Model, CLKM)：

- **模型结构**: 采用环链式结构描述连续体变形
- **精度平衡**: 平衡建模精度和计算复杂度
- **参数辨识**: 通过实验数据辨识模型参数

### 2. 刚柔混合臂应用

<img class="project-figure" src="/images/projects/cyclotomic-model/02_robot_design.png" alt="刚柔混合臂设计" loading="lazy">

*图 2：刚柔混合臂系统设计*

将模型应用于刚柔混合臂系统：

- **系统集成**: 将连续体模块与刚性机械臂集成
- **运动规划**: 实现刚柔混合臂的运动规划
- **精确控制**: 实现系统的精确运动控制


---


## 🎥 实验演示

<video controls width="100%" style="max-width: 800px; margin: 20px auto; display: block; border-radius: 8px;">
  <source src="/videos/cyclotomic-model.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*连续体机器人环链式运动学模型及刚柔混合臂实验演示*


---


## 📊 研究成果

### 模型性能对比


<table>
<thead>
<tr>
<th>指标</th>
<th>传统模型</th>
<th>环链式模型</th>
<th>提升</th>
</tr>
</thead>
<tbody><tr>
<td><strong>建模精度</strong></td>
<td>基准</td>
<td>提高</td>
<td>更准确描述变形</td>
</tr>
<tr>
<td><strong>计算效率</strong></td>
<td>基准</td>
<td>提升</td>
<td>适合实时控制</td>
</tr>
</tbody></table>

<img class="project-figure" src="/images/projects/cyclotomic-model/03_experiments.png" alt="实验测试" loading="lazy">

*图 3：刚柔混合臂运动性能测试*


---

---

## 🔗 相关链接

- [返回项目列表](/projects/)
- [查看论文页面](/publications/)

---

*最后更新：2026 年 8 月*
