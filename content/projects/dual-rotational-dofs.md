---
title: "集成双旋转自由度的连续体机器人设计与控制"
description: "集成双旋转自由度的连续体机器人机构设计与运动控制，发表于 IEEE IROS 2025"
date: 2025-10-01
tags: ["连续体机器人", "双旋转自由度", "运动控制"]
categories: ["科研项目"]
layout: "simple"
---

## 📄 论文信息

**论文标题**: Enhancing Continuum Robot Mobility: Design and Control with Integrated Dual Rotational DOFs

**作者**: Peng Yuan, Chen Sun, Xinyu Chang, Xu Zhang, Rong Kang

**发表会议**: IEEE&#x2F;RSJ International Conference on Intelligent Robots and Systems (IROS), Hangzhou, China, October 2025

**摘要**: Continuum robots, known for their compliance in unstructured environments, face limitations due to the lack of rotational degrees of freedom (DOFs) about the backbone. This prevents them from compensating undesired torsional deformation and performing 6-DOF control of the end-effector, thereby restricting their mobility. This paper presents a continuum robot with integrated dual rotational DOFs. One is integrated at the arm base to compensate for torsional deformation caused by external loads, while the other one, located at the end-effector, enables dexterous manipulation. The design, kinematic modeling, and control of the proposed robot are presented. Experimental results demonstrate the enhanced mobility and dexterity of the robot in complex manipulation tasks.

[📥 下载 PDF](/files/papers/Yuan%20%E7%AD%89%20-%20Enhancing%20Continuum%20Robot%20Mobility%20Design%20and%20Control%20with%20Integrated%20Dual%20Rotational%20DOFs.pdf) | [🔗 DOI](https://doi.org/10.1109/IROS60139.2025.11247688)


---


## 🎯 研究背景

传统连续体机器人在非结构化环境中表现出色，但由于缺乏绕骨干轴的旋转自由度，存在以下局限性：

1. **自由度有限**: 无法补偿扭转变形
2. **运动受限**: 难以执行 6 自由度末端控制
3. **灵活性不足**: 需要增强运动能力


---


## 🔬 研究方法

### 1. 机构创新设计

<img class="project-figure" src="/images/projects/dual-rotational-dofs/01_robot_design.png" alt="双旋转自由度机器人" loading="lazy">

*图 1：集成双旋转自由度的连续体机器人设计*

设计集成双旋转自由度的连续体机器人：

- **双旋转自由度**: 在连续体结构基础上集成两个旋转自由度
- **结构优化**: 优化机械结构以实现更大的工作空间
- **驱动设计**: 设计相应的驱动系统

### 2. 控制系统开发

<img class="project-figure" src="/images/projects/dual-rotational-dofs/02_mechanism.png" alt="机构原理" loading="lazy">

*图 2：双旋转自由度机构原理*

开发双旋转自由度的运动学模型和控制策略：

- **运动学建模**: 建立包含双旋转自由度的运动学模型
- **控制策略**: 设计相应的运动控制算法
- **协调控制**: 实现连续体变形与旋转运动的协调控制


---


## 🎥 实验演示

<video controls width="100%" style="max-width: 800px; margin: 20px auto; display: block; border-radius: 8px;">
  <source src="/videos/dual-rotational-dofs.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*集成双旋转自由度的连续体机器人运动演示*


---


## 📊 研究成果

### 性能提升


<table>
<thead>
<tr>
<th>指标</th>
<th>传统设计</th>
<th>双旋转自由度设计</th>
<th>提升</th>
</tr>
</thead>
<tbody><tr>
<td><strong>工作空间</strong></td>
<td>基准</td>
<td>显著扩大</td>
<td>灵活性提升</td>
</tr>
<tr>
<td><strong>运动能力</strong></td>
<td>基准</td>
<td>明显增强</td>
<td>适应复杂场景</td>
</tr>
</tbody></table>

<img class="project-figure" src="/images/projects/dual-rotational-dofs/03_experiments.png" alt="运动灵活性测试" loading="lazy">

*图 3：运动灵活性测试实验*


---

---

## 🔗 相关链接

- [返回项目列表](/projects/)
- [查看论文页面](/publications/)

---

*最后更新：2026 年 8 月*
