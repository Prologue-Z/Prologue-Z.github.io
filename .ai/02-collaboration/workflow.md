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

---

## 🔧 技术流程

### 添加博客文章

```bash
# 1. 创建新文章
hexo new post "文章标题"

# 2. 编辑文章
# 编辑 source/_posts/文章标题.md

# 3. 预览
hexo server

# 4. 部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

### 修改页面内容

```bash
# 1. 编辑页面文件
# 例如：source/about.md

# 2. 预览
hexo server

# 3. 部署
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
