# Git 策略

**版本**: v1.0.0  
**最后更新**: 2026-03-19

---

## 📋 分支策略

| 分支 | 用途 | 说明 |
|------|------|------|
| main | Hexo 源码 | 本地编辑，推送到 GitHub |
| gh-pages | 静态文件 | hexo deploy 自动生成 |

---

## 🚀 部署流程

```bash
# 一键部署
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

---

## 🔑 SSH Key

**位置**: `~/.ssh/hexo-deploy-new`  
**公钥**: `~/.ssh/hexo-deploy-new.pub`  
**用途**: GitHub deploy key

---

## 📝 Commit 规范

采用 Conventional Commits:

```
feat: 新功能
fix: 修复
docs: 文档
style: 格式
refactor: 重构
chore: 杂项
```

**示例**:
```bash
git commit -m "feat: add About page"
git commit -m "fix: navigation menu"
git commit -m "docs: update README"
```

---

## 📊 版本管理

采用语义化版本号：`MAJOR.MINOR.PATCH`

- **MAJOR**: 网站重构
- **MINOR**: 新页面/功能
- **PATCH**: 内容更新/Bug 修复

**当前版本**: v1.0.0

---

**关联**: `version.md`（版本详情）
