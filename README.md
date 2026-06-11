作品集（静态站点）

说明
- 这是为武汉大学在读学生准备的一个静态作品集模板，重点展示产品与数据分析类项目。

文件
- index.html — 入口页面（已包含交互与图表）
- styles.css — 原有样式（保留）
- portfolio.css — 新增覆盖样式（视觉增强）
- script.js — 页面交互与数据渲染（加载 projects.json）
- projects.json — 示例项目数据（可替换为真实数据）
- assets/ — 建议放置简历 `resume.pdf` 与项目截图

本地预览
1. 直接在浏览器中打开 `index.html`（推荐使用 VS Code Live Server 或本地静态服务器以避免跨域问题）。

示例命令（如果安装了 Node.js）：

```bash
# 安装一个快速静态服务器
npm install -g http-server
# 在项目根目录运行
http-server -c-1
# 打开浏览器访问 http://localhost:8080
```

部署建议
- 将该文件夹推送到 GitHub 仓库并启用 GitHub Pages（branch: main 或 gh-pages）。
- 推荐压缩图片为 WebP，预加载关键字体，启用 Lighthouse 性能优化。

如何修改内容
- 编辑 `projects.json` 添加/更新项目条目
- 修改 `portfolio.css` 调整配色与间距
- 在 `index.html` 中替换个人照片与邮件链接

后续可选工作
- 将详细项目页面改为单独路由或使用静态站点生成器（Gatsby/Vite/Next）
- 使用 Figma 重做高保真设计并导出资源
