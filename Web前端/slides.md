---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
css: unocss
title: 小学期WEB开发
---
# 什么是前端
---
layout: image-right
image: https://source.unsplash.com/collection/94734596/1920x1080
---

# 什么是前端

前端的基本概念

- 在传统的Web开发中，前后端的分离以浏览器为界限

  - 将客户端展示给用户的部分称为前端

  - 而将运行在服务器端负责业务逻辑和数据准备的开发称为后端

<style>
  ul {
    margin-top:1rem;
  }
  h1 {
    background-color: #2B90B6;
    background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
    background-size: 100%;
    -webkit-background-clip: text;
    -moz-background-clip: text;
    -webkit-text-fill-color: transparent;
    -moz-text-fill-color: transparent;
  }
</style>
---
layout: section
---

# 前端基本工具
工欲善其事，必先利其器
---
layout : two-cols
---
# VS Code
- VSCode（基于JS语言的Electron框架编写）是前端的**主力开发工具**，拥有数以万计的插件，生态极为活跃和丰富。![img](https://camo.githubusercontent.com/59fcf8fd89e84aaafba090e1341f139d0667e9d99935d6b572cc19521249e872/687474703a2f2f696d672e736d79687661652e636f6d2f32303139303331335f313735305f332e706e67)
  - VS Code 官网：[https://code.visualstudio.com](https://code.visualstudio.com/)
::right::
# Chrome浏览器
- Chrome浏览器是前端的主流浏览器，由Google进行开发，控制台功能强大，对程序员十分友好。![Chrome | Google Blog](data:image/png;base64,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)

  - Chrome浏览器下载地址：https://www.google.com/intl/zh-CN/chrome/


---
layout: section
---
# 前端入门
HTML CSS JavaScript
---
layout: two-cols
---
# HTML
- HTML：（超文本标记语言——HyperText Markup Language）是构成 Web 世界的一砖一瓦。它定义了网页内容的含义和结构。
::right::
# CSS
- CSS：（层叠样式表——Cascading Style Sheets）是一种 [样式表](https://developer.mozilla.org/zh-CN/docs/Web/API/StyleSheet) 语言，用来描述 [HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML) 等文档的呈现形式。

---
layout: two-cols
---
# 示例


<div style="border:3px solid yellow;margin-top:100px;">
<h1 style="color:blue;text-align:center;">
This is a Heading.
</h1>
<p style="text-decoration:line-through;">
This is a paragraph.
</p>
</div>


::right::

# 示例代码
<v-clicks>
```html {18|19|5-13|17|all}
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
	<style>
        h1{
          color:blue;
          text-align:center;
        }
        p{
          text-decoration:line-through;
        }
    </style>
</head>
<body>

<div style="border:1px solid yellow;">
<h1>This is a Heading.</h1>
<p>This is a paragraph.</p>
</div>

</body>
</html>
```
</v-clicks>

---
layout:default
---

# JavaScript
 - [JavaScript](https://developer.mozilla.org/zh-CN/docs/Glossary/JavaScript) 是一种[即时编译型](https://zh.wikipedia.org/wiki/即時編譯)的编程语言，允许你在 Web 页面上实现复杂的功能。如果你看到一个网页不仅仅显示静态的信息，而是显示依时间更新的内容，或者交互式地图，或者 2D/3D 动画图像，或者滚动的视频播放器，等等——你基本可以确定，这需要 JavaScript 的参与。
[![vJJJxS.png](https://s1.ax1x.com/2022/08/12/vJJJxS.png)](https://imgtu.com/i/vJJJxS)
---
layout: default
---
# 学习资源
- MDN：创立于2005年，记录了包括 CSS、HTML 和 JavaScript的丰富Web技术，前端开发必备。
  - 链接地址：https://developer.mozilla.org/en-US/
- W3Schools：世界上最大的Web开发人员网站。
  - 链接地址：https://www.w3schools.com/
- 现代 JavaScript 教程：通过简单但足够详细的内容，为你讲解从基础到高阶的 JavaScript 相关知识。
  - 链接地址：[现代 JavaScript 教程](https://zh.javascript.info/)
- Programming with Mosh：YouTube知名博主，上传大量教学速成视频。
  - 链接地址：https://www.youtube.com/c/programmingwithmosh

---
layout: section
---
# 前端框架
提高开发效率
---
layout: default
---
# Vue.js

什么是Vue.js

- Vue.js是一款用于构建用户界面的 JavaScript 框架。它基于标准 HTML、CSS 和 JavaScript 构建，并提供了一套声明式的、组件化的编程模型，帮助你高效地开发用户界面。无论是简单还是复杂的界面，Vue.js 都可以胜任。
  - 官方教程：[Vue.js - 渐进式JavaScript框架](https://cn.vuejs.org/)
- Node.js是一个基于 Chrome V8 引擎的 JavaScript 运行时，使用Vue前我们需要先拥有Node环境。
  - 下载地址：[Node.js中文网](http://nodejs.cn/download/)

---
layout: two-cols
---
# 计数器
<div style="margin-top:40%;margin-left:30%;">
<Counter :count="10" m="t-4" />
</div>


::right::

# 示例代码
<v-clocks>
```vue{1-7|8-19|all}
<script setup>
import { ref, watch } from 'vue'
const counter = ref(10)
watch(counter,(val)=>{
  if(val==15) alert("小学期快乐！")
})
</script>
<template>
  <div>
    <button @click="counter -= 1">
      -
    </button>
    <span>{{ counter }}</span>
    <button @click="counter += 1">
      +
    </button>
  </div>
</template>
```
</v-clocks>
---
layout: section
---
# 常用包
---
layout: two-cols
---

# Vue Router
[用Vue.js构建单页应用](https://router.vuejs.org/zh/introduction.html)
- 将构建的组件映射到路由上进行渲染
- 可以拦截任何导航并精确控制结果
::right::
# Pinia
[Vue.js的状态存储库](https://pinia.web3doc.top/)
- 允许跨页面跨组件存储状态
- 与Vue devtools挂钩，提升开发体验
---
layout: two-cols
---

# Axios
[一个基于Promise的网络请求库](https://www.axios-http.cn/docs/intro)
- 从浏览器创建 [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
- 拦截请求和响应
- 转换请求和响应数据
- 取消请求
- 自动转换JSON数据

::right::
# VueUse
[一个Vue组合式函数集合](https://vueuse.org/)，其源码是很好的学习资料
- <Mouse/>
- ```js
  const { x, y, sourceType} = useMouse();
  ```
- <Interval/>
- ```js
  const counter = useInterval(2000);
  ```
- <Now/>
- ```js
  const now = useDateFormat(useNow(), 'YYYY-MM-DD HH:mm:ss');
  ```


---
layout: iframe-right
url: https://element-plus.org/zh-CN/component/button.html
---

# Element-plus
[基于 Vue 3，面向设计师和开发者的组件库](https://element-plus.org/zh-CN/)
- 组件资源丰富
- 设计逻辑清晰
- 样式简洁通用
- 按钮、布局、表单、菜单…
---
layout: image-right
---
# ECharts
[一个基于 JavaScript 的开源可视化图表库](https://echarts.apache.org/zh/)
- 上手简单，样式美观
- 折线图、柱状图、饼图、散点图…

---
layout: section
---

# 一个简单案例
抛砖引玉

---
layout: end
---

感谢
