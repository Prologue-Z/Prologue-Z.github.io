# 工作流程

**版本**: v1.0.0  
**最后更新**: 2026-03-19

---

## 📋 标准流程

### 1. 内容创建流程

```
用户提供素材
    ↓
内容专家撰写
    ↓
Reviewer 审查
    ↓
Leader 确认
    ↓
部署上线
```

### 2. 主题优化流程

```
用户反馈
    ↓
前端专家调整
    ↓
Reviewer 测试
    ↓
Leader 确认
    ↓
部署上线
```

### 3. 日常更新流程

```
Leader 检查进度
    ↓
分配任务给专家
    ↓
专家完成任务
    ↓
Reviewer 审查
    ↓
Leader 部署
```

---

## 🔄 常用 Workflow

### WF-001: 添加新页面

```bash
# 1. Leader 创建任务
# 2. 内容专家撰写内容
# 3. 前端专家配置导航
# 4. Reviewer 审查
# 5. Leader 部署

# 创建新页面
hexo new page "page-name"

# 编辑内容
vim source/page-name/index.md

# 配置导航
vim source/_config.cactus.yml

# 部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

### WF-002: 发布新博客

```bash
# 1. 内容专家撰写
# 2. Reviewer 审查
# 3. Leader 部署

# 创建新文章
hexo new post "文章标题"

# 编辑文章
vim source/_posts/文章标题.md

# 本地预览
hexo server

# 部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

### WF-003: 主题配置变更

```bash
# 1. 前端专家提出方案
# 2. Leader 确认
# 3. 前端专家实施
# 4. Reviewer 测试
# 5. Leader 部署

# 编辑主题配置
vim source/_config.cactus.yml

# 本地预览
hexo server

# 部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

### WF-004: 内容更新

```bash
# 1. 内容专家更新
# 2. Reviewer 审查
# 3. Leader 部署

# 编辑页面
vim source/about.md

# 本地预览
hexo server

# 部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

### WF-005: 紧急修复

```bash
# 1. Leader 确认问题
# 2. 专家修复
# 3. Leader 直接部署

# 快速修复
vim source/xxx.md

# 立即部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

---

## 📊 阶段确认

每个阶段结束必须找用户确认：

| 阶段 | 确认内容 | 状态 |
|------|----------|------|
| 阶段 1: 基础框架 | 部署流程、主题配置 | ✅ 已完成 |
| 阶段 2: 内容填充 | About / Publications / Projects / Honors | 🟡 进行中 |
| 阶段 3: 主题优化 | 样式、响应式 | ⚪ 待确认 |
| 阶段 4: 最终审查 | 全面检查 | ⚪ 待确认 |

---

## 🛠️ 快速命令

```bash
# 新建文章
hexo new post "标题"

# 本地预览
hexo server

# 一键部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

---

**关联**: `tools.md`（工具详情）、`START.md`（快速入口）
