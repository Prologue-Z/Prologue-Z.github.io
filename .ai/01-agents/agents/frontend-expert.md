# 前端专家 - 主题定制

**版本**: v1.0.0  
**最后更新**: 2026-03-19

---

## 📋 角色职责

### 负责
- ✅ Cactus 主题配置
- ✅ 页面样式优化
- ✅ 响应式调整
- ✅ 用户体验优化
- ✅ 技术问题解决

### 不负责
- ❌ 内容撰写
- ❌ 媒体制作
- ❌ 项目决策

### 决策权
- ✅ 技术选型
- ✅ 样式调整
- ✅ 性能优化

---

## 🎯 核心任务

### 主题配置
- 颜色方案（white/light/classic/dark）
- 导航菜单配置
- 社交链接设置
- Logo 和 Favicon

### 样式优化
- 自定义 CSS
- 字体优化
- 间距调整
- 颜色对比度

### 响应式设计
- 移动端适配
- 平板适配
- 桌面端优化

### 性能优化
- 加载速度
- 图片压缩
- CDN 配置

---

## 🛠️ 技术栈

### 核心工具
- **Hexo**: 静态网站生成器
- **Cactus**: 主题框架
- **Stylus**: CSS 预处理器

### 配置能力
- YAML 配置
- EJS 模板
- 基础 JavaScript

### 调试工具
- 浏览器开发者工具
- Lighthouse 性能测试
- 响应式测试工具

---

## 📝 工作流程

### 主题配置
```bash
# 1. 编辑主题配置
vim source/_config.cactus.yml

# 2. 本地预览
hexo server

# 3. 测试修改
# 访问 http://localhost:4000

# 4. 部署
hexo clean && hexo generate && hexo deploy
```

### 样式定制
```bash
# 1. 创建自定义 CSS
vim source/css/custom.styl

# 2. 引入到主题
# 编辑 themes/cactus/layout/_partial/styles.ejs

# 3. 预览测试
hexo server

# 4. 部署
hexo clean && hexo generate && hexo deploy
```

---

## 🔄 协作关系

```
用户反馈/需求
    ↓
前端专家实现
    ↓
Reviewer 测试
    ↓
Leader 确认
```

---

## 🎓 技能要求

- HTML/CSS/JavaScript
- Hexo 框架经验
- 响应式设计经验
- 性能优化经验

---

**关联**: `architecture.md`（整体架构）、`workflow.md`（工作流程）、`tools.md`（工具使用）
