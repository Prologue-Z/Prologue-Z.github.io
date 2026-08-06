---
title: "基于速度敏感性的连续体机器人变增益控制"
description: "速度敏感性分析与变增益控制策略，发表于 Mechanism and Machine Theory 2022"
date: 2022-02-01
tags: ["连续体机器人", "变增益控制", "速度敏感性"]
categories: ["科研项目"]
layout: "simple"
---

## 📄 论文信息

**论文标题**: Variable-gain control for continuum robots based on velocity sensitivity

**作者**: Xu Zhang, Yue Liu, David T. Branson, Chenghao Yang, Jian S. Dai, Rong Kang

**发表期刊**: Mechanism and Machine Theory, Volume 168, February 2022, 104618

**摘要**: The kinematic characteristics of continuum robots vary with configuration, resulting in significant tracking error fluctuations when following a given path. This paper proposes a velocity sensitivity analysis method to evaluate the kinematic characteristics of continuum robots. The velocity sensitivity represents the contribution of individual actuators to the instantaneous motion of the end-effector. Based on the velocity sensitivity analysis, a variable-gain control strategy is proposed to adjust the controller gains in real time according to the configuration changes. Experimental results show that the proposed method can effectively smooth the tracking error and achieve smooth motion within the workspace.

[📥 下载 PDF](/files/papers/Zhang%20%E7%AD%89%20-%202022%20-%20Variable-gain%20control%20for%20continuum%20robots%20based%20o.pdf) | [🔗 DOI](https://doi.org/10.1016/j.mechmachtheory.2021.104618)


---


## 🎯 研究背景

连续体机器人的运动学特性随构型变化而变化，在跟踪给定路径时存在以下挑战：

<img class="project-figure" src="/images/projects/variable-gain/01_robot_design.png" alt="机器人设计" loading="lazy">

*图 1：连续体机器人结构设计*

1. **构型依赖性**: 运动学特性在不同构型下差异显著
2. **致动器耦合**: 不同致动器对末端运动的贡献随构型变化
3. **误差波动**: 传统固定增益控制导致跟踪误差波动大


---


## 🔬 研究方法

### 1. 速度敏感性分析

提出速度敏感性参数，评估连续体机器人的运动学特性：

- **定义**: 速度敏感性表示个体致动器对末端瞬时运动的贡献
- **计算**: 基于雅可比矩阵分析各致动器的速度贡献
- **应用**: 用于评估机器人在不同构型下的运动学特性

### 2. 变增益控制策略

<img class="project-figure" src="/images/projects/variable-gain/02_control_scheme.png" alt="变增益控制方案" loading="lazy">

*图 2：基于速度敏感性的变增益控制策略*

根据路径上变化的速度敏感性实时调节伺服控制器增益：

- **增益调度**: 根据速度敏感性实时调整控制器增益
- **误差平滑**: 减少跟踪误差的实时波动
- **自适应调节**: 实现控制器参数随构型自适应变化


---


## 🎥 实验演示

<video controls width="100%" style="max-width: 800px; margin: 20px auto; display: block; border-radius: 8px;">
  <source src="/videos/variable-gain.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*基于速度敏感性的连续体机器人变增益控制实验演示*


---


## 📊 研究成果

### 控制性能对比


<table>
<thead>
<tr>
<th>指标</th>
<th>固定增益控制</th>
<th>变增益控制</th>
<th>提升</th>
</tr>
</thead>
<tbody><tr>
<td><strong>误差波动</strong></td>
<td>基准</td>
<td>显著降低</td>
<td>有效平滑</td>
</tr>
<tr>
<td><strong>运动平滑性</strong></td>
<td>基准</td>
<td>明显改善</td>
<td>工作空间内平滑运动</td>
</tr>
</tbody></table>

<img class="project-figure" src="/images/projects/variable-gain/03_experiment_setup.png" alt="实验结果对比" loading="lazy">

*图 3：固定增益与变增益控制的跟踪误差对比*


---

---

## 🔗 相关链接

- [返回项目列表](/projects/)
- [查看论文页面](/publications/)

---

*最后更新：2026 年 8 月*
