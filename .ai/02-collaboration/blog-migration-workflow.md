# 博客搬运工作流

> 从 CSDN/其他平台迁移博客文章到个人主页的标准流程

---

## 📋 工作流程

### 1. 获取文章内容
- 使用 `web_fetch` 工具获取 CSDN 文章内容和代码
- 保存文章元信息（发布日期、标签、分类等）

### 2. 创建博客文件
```bash
cd /home/admin/.openclaw/workspace/projects/个人主页
hexo new post "文章标题"
```

### 3. 编辑 Front-matter
```markdown
---
title: 文章标题
date: YYYY-MM-DD HH:MM:SS  # 原文发布日期
updated: YYYY-MM-DD HH:MM:SS  # 迁移日期
tags: [标签 1, 标签 2]
categories: 分类名称
---
```

### 4. ⚠️ 重要注意事项

#### ❌ 不要添加文章标题
**错误做法**：
```markdown
---
title: 文章标题
---

# 文章标题  <!-- 不要这样写！ -->

正文内容...
```

**正确做法**：
```markdown
---
title: 文章标题
---

正文内容...  <!-- 直接开始正文 -->
```

> **原因**：Hexo 主题会自动在页面顶部显示文章标题（包含在 post.ejs 的 title partial 中），如果在正文中再写一遍标题，会导致页面显示两个相同的标题。

#### ✅ 正确的文章结构
```markdown
---
title: 文章标题
date: 2026-03-20 10:00:00
tags: [标签]
categories: 分类
---

> 可选的引言或摘要

## 第一个章节

正文内容...

## 第二个章节

更多内容...
```

### 5. 处理图片

#### CSDN 图片防盗链
CSDN 的图片有防盗链保护，不能直接引用。有两种方案：

**方案 A：手动下载图片**
1. 下载原文中的图片
2. 放到 `source/images/posts/` 目录
3. 在文章中使用：`![图片说明](/images/posts/文件名.jpg)`

**方案 B：使用浏览器截图**
1. 用 browser 工具打开 CSDN 文章
2. 截图保存
3. 放到 `source/images/posts/` 目录

### 6. 更新博客列表
编辑 `source/blog.md`，在"最新文章"部分添加：
```markdown
- <a href="/YYYY/MM/DD/文章 URL/">文章标题</a> - YYYY 年 M 月 D 日
```

> **注意**：使用 HTML `<a>` 标签而不是 Markdown `[]()` 语法，避免中文字符和特殊字符的解析问题。

### 7. 生成并部署
```bash
hexo clean && hexo generate && hexo deploy
```

### 8. 验证
- 访问博客文章页面
- 检查是否只有一个标题
- 检查图片是否正常显示
- 检查链接是否可以点击

---

## 📝 检查清单

- [ ] Front-matter 填写完整（title, date, tags, categories）
- [ ] **正文开头没有重复的标题**
- [ ] 图片已本地化（不引用外部链接）
- [ ] 代码块格式正确
- [ ] 博客列表已更新
- [ ] 已清理缓存并重新生成
- [ ] 已部署到 GitHub Pages
- [ ] 已验证页面显示正常

---

## 🔧 常用命令

```bash
# 创建新文章
hexo new post "文章标题"

# 清理并重新生成
hexo clean && hexo generate

# 部署
hexo deploy

# 一键完成
hexo clean && hexo generate && hexo deploy
```

---

## 📚 参考文件

- 博客文章目录：`source/_posts/`
- 图片目录：`source/images/posts/`
- 博客列表：`source/blog.md`
- 导航菜单配置：`themes/cactus/layout/_partial/nav-menu.ejs`

---

*最后更新：2026-03-21*
