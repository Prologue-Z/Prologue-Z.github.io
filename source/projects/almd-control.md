---
title: 连续体机器人自适应动力学建模与控制
layout: project
comments: false
date: 2024-10-01 00:00:00
tags: [连续体机器人，动力学建模，自适应控制]
categories: 科研项目
---

> **发表论文**: *Mechanism and Machine Theory*, 2024 | JCR Q1 | IF: 4.5

---

## 📋 项目信息

| 项目 | 信息 |
|------|------|
| **项目周期** | 2022 - 2024 |
| **项目角色** | 第一作者/主要研究者 |
| **合作者** | C. Yang, Z. Song, M. A. Khanesar, D. T. Branson, J. S. Dai, R. Kang |
| **发表期刊** | Mechanism and Machine Theory |
| **论文状态** | 已发表 |

---

## 🎯 研究背景

连续体机器人在运动过程中存在大范围非线性变形和动态参数变化，传统固定参数动力学模型难以准确描述其动态特性。主要挑战包括：

1. **非线性变形**: 连续体机器人运动时产生大范围非线性变形
2. **参数时变**: 动态参数随运动状态实时变化
3. **建模困难**: 传统方法难以建立精确的动态模型

---

## 🔬 主要工作

### 1. 集总参数动力学建模

建立包含关节弹性和粘性参数的集总参数动力学模型 (Lumped-mass Dynamic Model, LMD)：

- 将连续体机器人离散化为多个质点 - 弹簧 - 阻尼系统
- 考虑关节的弹性变形和粘性阻尼效应
- 通过拉格朗日方程建立系统动力学方程

### 2. 自适应参数调整

通过数据驱动方法实现动力学参数的实时自适应调整：

- **参数估计**: 使用遗传算法 (GA) 估计不同运动状态下的最优动态参数
- **数据集构建**: 收集不同位置、速度下的最优参数数据
- **神经网络训练**: 训练多层感知机 (MLP) 建立运动状态到动态参数的映射
- **实时调整**: 实现动力学模型的实时参数自适应 (Adaptive Lumped-mass Dynamic, ALMD)

### 3. 前馈控制器设计

基于 ALMD 模型设计前馈控制器：

- 利用 ALMD 模型预测所需的关节力矩
- 结合反馈控制实现精确轨迹跟踪
- 在连续体机器人原型机上验证控制性能

---

## 📊 研究成果

### 建模精度提升

| 指标 | 固定参数 LMD | 自适应 ALMD | 提升 |
|------|-------------|-------------|------|
| **最大建模误差** | 基准 | -60.2% | 显著降低 |
| **平均建模误差** | 基准 | -45.8% | 明显降低 |

### 控制性能提升

| 指标 | 传统控制 | ALMD 前馈控制 | 提升 |
|------|---------|---------------|------|
| **最大跟踪误差** | 基准 | -67.5% | 显著降低 |
| **平均跟踪误差** | 基准 | -52.3% | 明显降低 |

### 学术产出

- **发表论文**: 1 篇 JCR Q1 期刊论文
- **期刊名称**: Mechanism and Machine Theory
- **影响因子**: 4.5
- **分区**: 中科院 1 区

---

## 📄 相关论文

**X. Zhang**, C. Yang, Z. Song, M. A. Khanesar, D. T. Branson, J. S. Dai, and R. Kang, "An adaptive lumped-mass dynamic model and its control application for continuum robots," *Mechanism and Machine Theory*, vol. 201, p. 105736, Oct. 2024.

<a href="/files/papers/Zhang 等 - 2024 - An adaptive lumped-mass dynamic model and its control application for continuum robots.pdf" target="_blank">📥 下载 PDF</a> | <a href="https://doi.org/10.1016/j.mechmachtheory.2024.105736" target="_blank">🔗 DOI</a>

---

## 📸 项目图示

*（项目图片待添加）*

---

## 🔗 相关链接

- [返回项目列表](/projects.html)
- [查看论文页面](/publications.html)

---

*最后更新：2026 年 3 月*
