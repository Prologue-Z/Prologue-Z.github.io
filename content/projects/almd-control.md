---
title: "连续体机器人自适应动力学建模与控制"
description: "自适应集总参数动力学模型（ALMD）与基于模型的前馈控制，发表于 Mechanism and Machine Theory 2024"
date: 2024-10-01
tags: ["连续体机器人", "动力学建模", "自适应控制"]
categories: ["科研项目"]
layout: "simple"
---

## 📄 论文信息

**论文标题**: An adaptive lumped-mass dynamic model and its control application for continuum robots

**作者**: Xu Zhang, Chenghao Yang, Zhibin Song, Mojtaba A. Khanesar, David T. Branson, Jian S. Dai, Rong Kang

**发表期刊**: Mechanism and Machine Theory, Volume 201, October 2024, 105736

**摘要**: Continuum robots exhibit large-range nonlinear deformation and dynamic parameter variations during motion. Traditional dynamics models with fixed parameters struggle to accurately describe their dynamic characteristics. This paper proposes an adaptive lumped-mass dynamic (ALMD) model for continuum robots. The dynamic parameters under different robot statuses are estimated by using the genetic algorithm (GA). A dataset consisting of the robot status and the corresponding dynamic parameters is established to train a multilayer perceptron (MLP), which can predict the dynamic parameters in real time according to the robot status. Based on the ALMD model, a feedforward controller is designed to improve the trajectory tracking performance. Experimental results show that the maximum and average modeling errors are reduced by 60.2% and 45.8% respectively, and the maximum and average tracking errors are reduced by 67.5% and 52.3% respectively.

[📥 下载 PDF](/files/papers/Zhang%20%E7%AD%89%20-%202024%20-%20An%20adaptive%20lumped-mass%20dynamic%20model%20and%20its%20control%20application%20for%20continuum%20robots.pdf) | [🔗 DOI](https://doi.org/10.1016/j.mechmachtheory.2024.105736)


---


## 🎯 研究背景

连续体机器人在运动过程中存在大范围非线性变形和动态参数变化，传统固定参数动力学模型难以准确描述其动态特性。

<img class="project-figure" src="/images/projects/almd-control/01_robot_modeling.png" alt="机器人建模" loading="lazy">

*图 1：连续体机器人建模：(a) 机器人结构，(b) 运动学模型，(c) 集总参数动力学模型 (LMD)*

主要挑战包括：

1. **非线性变形**: 连续体机器人运动时产生大范围非线性变形
2. **参数时变**: 动态参数随运动状态实时变化
3. **建模困难**: 传统方法难以建立精确的动态模型


---


## 🔬 研究方法

### 1. 集总参数动力学建模

建立包含关节弹性和粘性参数的集总参数动力学模型 (Lumped-mass Dynamic Model, LMD)：

- 将连续体机器人离散化为多个质点 - 弹簧 - 阻尼系统
- 考虑关节的弹性变形和粘性阻尼效应
- 通过拉格朗日方程建立系统动力学方程

### 2. 自适应参数调整

<img class="project-figure" src="/images/projects/almd-control/02_parameter_estimation.png" alt="参数估计流程" loading="lazy">

*图 2：基于遗传算法 (GA) 的参数估计流程*

通过数据驱动方法实现动力学参数的实时自适应调整：

- **参数估计**: 使用遗传算法 (GA) 估计不同运动状态下的最优动态参数
- **数据集构建**: 收集不同位置、速度下的最优参数数据
- **神经网络训练**: 训练多层感知机 (MLP) 建立运动状态到动态参数的映射
- **实时调整**: 实现动力学模型的实时参数自适应 (Adaptive Lumped-mass Dynamic, ALMD)

### 3. 前馈控制器设计

<img class="project-figure" src="/images/projects/almd-control/11_control_scheme.png" alt="控制方案" loading="lazy">

*图 3：基于 ALMD 的前馈控制方案*

基于 ALMD 模型设计前馈控制器：

- 利用 ALMD 模型预测所需的关节力矩
- 结合反馈控制实现精确轨迹跟踪
- 在连续体机器人原型机上验证控制性能


---


## 🎥 实验演示

<video controls width="100%" style="max-width: 800px; margin: 20px auto; display: block; border-radius: 8px;">
  <source src="/videos/almd-control.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*连续体机器人自适应动力学建模与控制实验演示*


---


## 📊 研究成果

### 建模精度提升


<table>
<thead>
<tr>
<th>指标</th>
<th>固定参数 LMD</th>
<th>自适应 ALMD</th>
<th>提升</th>
</tr>
</thead>
<tbody><tr>
<td><strong>最大建模误差</strong></td>
<td>基准</td>
<td>-60.2%</td>
<td>显著降低</td>
</tr>
<tr>
<td><strong>平均建模误差</strong></td>
<td>基准</td>
<td>-45.8%</td>
<td>明显降低</td>
</tr>
</tbody></table>

### 控制性能提升


<table>
<thead>
<tr>
<th>指标</th>
<th>传统控制</th>
<th>ALMD 前馈控制</th>
<th>提升</th>
</tr>
</thead>
<tbody><tr>
<td><strong>最大跟踪误差</strong></td>
<td>基准</td>
<td>-67.5%</td>
<td>显著降低</td>
</tr>
<tr>
<td><strong>平均跟踪误差</strong></td>
<td>基准</td>
<td>-52.3%</td>
<td>明显降低</td>
</tr>
</tbody></table>

<img class="project-figure" src="/images/projects/almd-control/10_prototype.png" alt="机器人原型" loading="lazy">

*图 4：连续体机器人原型机实验平台*


---

---

## 🔗 相关链接

- [返回项目列表](/projects/)
- [查看论文页面](/publications/)

---

*最后更新：2026 年 8 月*
