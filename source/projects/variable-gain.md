---
title: 基于速度敏感性的连续体机器人变增益控制
layout: project
comments: false
date: 2022-02-01 00:00:00
tags: [连续体机器人，变增益控制，速度敏感性，Mechanism and Machine Theory]
categories: 科研项目
---

> **发表论文**: *Mechanism and Machine Theory*, 2022 | JCR Q1 | IF: 4.5

---

## 📋 项目信息

| 项目 | 信息 |
|------|------|
| **项目周期** | 2020 - 2022 |
| **项目角色** | 第一作者/主要研究者 |
| **合作者** | Y. Liu, D. T. Branson, C. Yang, J. S. Dai, R. Kang |
| **发表期刊** | Mechanism and Machine Theory |
| **论文状态** | 已发表 |

---

## 🎯 研究背景

连续体机器人的运动学特性随构型变化而变化，在跟踪给定路径时存在以下挑战：

1. **构型依赖性**: 运动学特性在不同构型下差异显著
2. **致动器耦合**: 不同致动器对末端运动的贡献随构型变化
3. **误差波动**: 传统固定增益控制导致跟踪误差波动大

---

## 🔬 主要工作

### 1. 速度敏感性分析

提出速度敏感性参数，评估连续体机器人的运动学特性：

- **定义**: 速度敏感性表示个体致动器对末端瞬时运动的贡献
- **计算**: 基于雅可比矩阵分析各致动器的速度贡献
- **应用**: 用于评估机器人在不同构型下的运动学特性

### 2. 变增益控制策略

根据路径上变化的速度敏感性实时调节伺服控制器增益：

- **增益调度**: 根据速度敏感性实时调整控制器增益
- **误差平滑**: 减少跟踪误差的实时波动
- **自适应调节**: 实现控制器参数随构型自适应变化

### 3. 实验验证

在杆驱动连续体机器人平台上验证所提方法：

- **实验平台**: 搭建杆驱动连续体机器人实验系统
- **路径跟踪**: 设计典型跟踪路径进行实验验证
- **性能评估**: 对比固定增益和变增益控制的性能

---

## 📊 研究成果

### 控制性能

| 指标 | 固定增益控制 | 变增益控制 | 提升 |
|------|-------------|-----------|------|
| **误差波动** | 基准 | 显著降低 | 有效平滑 |
| **运动平滑性** | 基准 | 明显改善 | 工作空间内平滑运动 |

### 学术产出

- **发表论文**: 1 篇 JCR Q1 期刊论文
- **期刊名称**: Mechanism and Machine Theory
- **影响因子**: 4.5
- **分区**: 中科院 1 区

---

## 📄 相关论文

**X. Zhang**, Y. Liu, D. T. Branson, C. Yang, J. S. Dai, and R. Kang, "Variable-gain control for continuum robots based on velocity sensitivity," *Mechanism and Machine Theory*, vol. 168, p. 104618, Feb. 2022.

<a href="/files/papers/Zhang 等 - 2022 - Variable-gain control for continuum robots based o.pdf" target="_blank">📥 下载 PDF</a> | <a href="https://doi.org/10.1016/j.mechmachtheory.2021.104618" target="_blank">🔗 DOI</a>

---

## 📸 项目图示

*（项目图片待添加）*

---

## 🔗 相关链接

- [返回项目列表](/projects.html)
- [查看论文页面](/publications.html)

---

*最后更新：2026 年 3 月*
