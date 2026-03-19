# 文件结构

**版本**: v1.0.0  
**最后更新**: 2026-03-19

---

## 📁 整体结构

```
~/.openclaw/workspace/projects/个人主页/
├── .ai/                        # AI 协作文档
│   ├── START.md               # 快速入口
│   ├── 00-entry/              # 入口文档
│   │   ├── overview.md        # 项目概览
│   │   └── structure.md       # 文件结构
│   ├── 01-agents/             # 智能体配置
│   │   ├── architecture.md    # 智能体架构
│   │   └── agents/            # 角色定义
│   ├── 02-collaboration/      # 协作流程
│   │   ├── workflow.md        # 工作流程
│   │   ├── tools.md           # 工具使用
│   │   └── meetings.md        # 会议记录
│   ├── 03-records/            # 记录
│   │   ├── progress.md        # 进度记录
│   │   ├── decisions.md       # 决策日志
│   │   └── discussions/       # 讨论记录
│   └── 04-git/                # Git 管理
│       ├── policy.md          # Git 策略
│       └── version.md         # 版本管理
├── _config.yml                # 站点配置
├── source/                    # 源文件
│   ├── _posts/                # 博客文章
│   ├── _config.cactus.yml     # 主题配置
│   └── ...
├── themes/cactus/             # Cactus 主题
└── public/                    # 生成的静态文件
```

---

## 📄 关键文件

| 文件 | 用途 |
|------|------|
| `_config.yml` | 站点配置（标题、作者、URL） |
| `source/_config.cactus.yml` | 主题配置（颜色、导航、社交链接） |
| `source/_posts/` | 博客文章目录 |
| `.ai/START.md` | 每次会话先读 |

---

## 🔗 关联文档

**上一级**: `overview.md`（项目概览）  
**下一级**: `workflow.md`（工作流程）
