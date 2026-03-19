# 🚀 个人主页项目 - 启动入口

**创建时间**: 2026-03-19  
**状态**: ✅ 基础框架已完成  
**访问地址**: https://prologue-z.github.io

---

## 📋 项目概况

### 目标
建立个人主页，展示：
- ✅ 个人信息
- ✅ 论文成果
- ✅ 技术博客
- ✅ 项目展示
- ✅ 荣誉奖项

### 技术方案
- **框架**: Hexo
- **主题**: Cactus (white - 白色主题)
- **托管**: GitHub Pages
- **仓库**: https://github.com/Prologue-Z/Prologue-Z.github.io

---

## 🎯 当前阶段

### 阶段 1: 基础框架 ✅ 已完成
- [x] Hexo 环境初始化
- [x] Cactus 主题安装
- [x] GitHub 仓库配置
- [x] 一键部署流程跑通
- [x] 白色主题配置

### 阶段 2: 内容填充 🟢 进行中
- [ ] 填充 About 页面
- [ ] 填充 Publications 页面
- [ ] 填充 Projects 页面
- [ ] 填充 Honors 页面
- [ ] 撰写技术博客

---

## 🚀 部署流程（重要！）

### 一键部署命令
```bash
cd ~/.openclaw/workspace/projects/个人主页
ssh-agent bash -c 'ssh-add ~/.ssh/hexo-deploy-new && hexo clean && hexo generate && hexo deploy'
```

### 分支说明
- **main 分支**: Hexo 源码（本地编辑）
- **gh-pages 分支**: 生成的静态文件（GitHub Pages 读取）

### GitHub Pages 设置
- **Source**: Deploy from a branch
- **Branch**: gh-pages
- **Folder**: / (root)

---

## 📁 文件结构

```
~/.openclaw/workspace/projects/个人主页/
├── .ai/                    # AI 协作文档
│   ├── 00-入口/
│   │   └── START.md       # 本文件
│   ├── 01-智能体/          # 智能体配置
│   ├── 02-流程/            # 工作流程
│   └── 03-日志/            # 讨论日志
├── _config.yml            # 站点配置
├── source/
│   ├── _posts/            # 博客文章
│   │   ├── welcome.md     # 欢迎文章
│   │   └── hello-world.md
│   ├── _config.cactus.yml # 主题配置
│   └── ...
├── themes/cactus/         # Cactus 主题
└── public/                # 生成的静态文件
```

---

## 🎨 主题配置

### 颜色方案
- **当前**: white (纯白色背景)
- **可选**: light, classic, dark

### 导航菜单
- Home
- About
- Publications
- Projects
- Honors
- Blog

### 社交链接
- GitHub: https://github.com/Prologue-Z
- Google Scholar: 配置中
- ORCID: 配置中
- Email: tju_zhangxu@tju.edu.cn

---

## 📝 下一步计划

### P0 - 高优先级
- [ ] 创建智能体团队配置
- [ ] 填充 About 页面内容
- [ ] 填充 Publications 页面

### P1 - 中优先级
- [ ] 填充 Projects 页面
- [ ] 填充 Honors 页面
- [ ] 撰写第一篇技术博客

### P2 - 低优先级
- [ ] 优化主题样式
- [ ] 添加自定义域名
- [ ] 配置 SEO 优化

---

## 💡 经验教训

### 部署注意事项
1. **SSH Key**: 使用 `~/.ssh/hexo-deploy-new`
2. **部署命令**: 必须用 `ssh-agent` 包装
3. **分支设置**: GitHub Pages 从 gh-pages 分支读取
4. **缓存时间**: GitHub Pages 刷新需要 2-5 分钟

### 主题相关
1. Cactus 主题配置在 `source/_config.cactus.yml`
2. 白色主题设置：`colorscheme: white`
3. 导航菜单在主题配置文件中设置

---

**最后更新**: 2026-03-19 23:07
