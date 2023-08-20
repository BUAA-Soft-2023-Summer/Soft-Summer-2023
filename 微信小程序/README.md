# 微信小程序指引

## 教程

- 官方文档：[小程序框架 / 介绍 (qq.com)](https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/#小程序简介)
  - 主要参考API和组件等内容，特别注意有些方法在更新后已不再使用，慎重复制粘贴网上代码。
- 入口：[公众号 (qq.com)](https://mp.weixin.qq.com/cgi-bin/wx)
  - 完成注册以及之后可能的审核工作，不要忽视这部分工作。
- 论坛：[首页 | 微信开放社区 (qq.com)](https://developers.weixin.qq.com/community/homepage)
  - 查看自己遇到的问题有没有（最新的）官方回答，也可以联系客服解决（指非开发技术性问题）。
- 利用现有组件库、chatGPT、bilibili等你能想到的方法进行学习。

## 优势

- 集成的开发平台，即开即用，不需复杂的环境配置：
  - 等大家以后配置各种环境就知道了
- 实时预览，方便设计：
  - 虽然 vue 等网页开发框架也可以做到，但是手机屏幕无疑更加小巧，方便ui设计
- 锻炼经验：
  - 可以发布自己的小程序，为以后的软件工程开发积累经验

## 工具

### 稳定版 [Stable Build](https://developers.weixin.qq.com/miniprogram/dev/devtools/stable.html) (1.06.2307260)

> 测试版缺陷收敛后转为稳定版。Stable版本从 1.06 开始不支持Windows7，建议开发者升级Windows版本。

[Windows 64](https://servicewechat.com/wxa-dev-logic/download_redirect?type=win32_x64&from=mpwiki&download_version=1062307260&version_type=1) 、 [Windows 32](https://servicewechat.com/wxa-dev-logic/download_redirect?type=win32_ia32&from=mpwiki&download_version=1062307260&version_type=1) 、 [macOS x64](https://servicewechat.com/wxa-dev-logic/download_redirect?type=darwin_x64&from=mpwiki&download_version=1062307260&version_type=1) 、 [macOS ARM64](https://servicewechat.com/wxa-dev-logic/download_redirect?type=darwin_arm64&from=mpwiki&download_version=1062307260&version_type=1)

### 预发布版 [RC Build](https://developers.weixin.qq.com/miniprogram/dev/devtools/rc.html) (1.06.2306281)

> 预发布版，包含大的特性；通过内部测试，稳定性尚可。RC版本从 1.06 开始不支持Windows7，建议开发者升级Windows版本。

[Windows 64](https://servicewechat.com/wxa-dev-logic/download_redirect?type=win32_x64&from=mpwiki&download_version=1062306281&version_type=1) 、 [Windows 32](https://servicewechat.com/wxa-dev-logic/download_redirect?type=win32_ia32&from=mpwiki&download_version=1062306281&version_type=1) 、 [macOS x64](https://servicewechat.com/wxa-dev-logic/download_redirect?type=darwin_x64&from=mpwiki&download_version=1062306281&version_type=1) 、 [macOS ARM64](https://servicewechat.com/wxa-dev-logic/download_redirect?type=darwin_arm64&from=mpwiki&download_version=1062306281&version_type=1)

### 开发版 [Nightly Build](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) (1.06.2308142)

> 日常构建版本(基于 NW.js 0.54.1) ，用于尽快修复缺陷和敏捷上线小的特性；开发自测验证，稳定性欠佳。Nightly版本从 1.06 开始不支持Windows7，建议开发者升级Windows版本。

[Windows 64](https://dldir1.qq.com/WechatWebDev/nightly/p-3bd19c2db3a642a0b39af853efaf67f8/0.54.1/wechat_devtools_1.06.2308142_win32_x64.exe)、[Windows 32](https://dldir1.qq.com/WechatWebDev/nightly/p-3bd19c2db3a642a0b39af853efaf67f8/0.54.1/wechat_devtools_1.06.2308142_win32_ia32.exe)、[macOS x64](https://dldir1.qq.com/WechatWebDev/nightly/p-3bd19c2db3a642a0b39af853efaf67f8/0.54.1/wechat_devtools_1.06.2308142_darwin_x64.dmg)、[macOS ARM64](https://dldir1.qq.com/WechatWebDev/nightly/p-3bd19c2db3a642a0b39af853efaf67f8/0.54.1/wechat_devtools_1.06.2308142_darwin_arm64.dmg)

### 小游戏版 [Minigame Build](https://developers.weixin.qq.com/minigame/dev/devtools/download.html)

> 适用于最新的小游戏开发者工具，其他版工具依然只能体验到旧版本小游戏开发模式。

[点击下载小游戏版开发者工具](https://developers.weixin.qq.com/minigame/dev/devtools/download.html)