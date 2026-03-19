# 工具使用

**版本**: v1.0.0  
**最后更新**: 2026-03-19

---

## 🛠️ 核心工具

### Hexo
- **用途**: 静态网站生成器
- **配置**: `_config.yml`
- **命令**: `hexo generate`, `hexo deploy`

### Cactus 主题
- **用途**: 网站主题
- **配置**: `source/_config.cactus.yml`
- **颜色**: white, light, classic, dark

### GitHub Pages
- **用途**: 网站托管
- **分支**: gh-pages
- **地址**: https://prologue-z.github.io

---

## 🔑 SSH Key

| Key | 用途 | 位置 |
|-----|------|------|
| hexo-deploy-new | GitHub 部署 | `~/.ssh/hexo-deploy-new` |

---

## 📝 编辑工具

- **推荐**: VS Code
- **预览**: `hexo server` (http://localhost:4000)

---

## 🚀 部署工具

```bash
# 一键部署命令
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

---

## 📊 监控工具

- **GitHub Actions**: 部署日志
- **GitHub Pages**: 访问统计

---

**关联**: `workflow.md`（工作流程）
