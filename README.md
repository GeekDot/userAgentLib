<h2 align= center> userAgentLib 随机返回 UA 头部库 </h2>

<h5 align=right> 张懿 </h5>
<p align=right> 2019-09-11 </p>

### 一、概述

`userAgentLib` 是随机返回 `UA` 头部库，可用于爬虫的防爬策略，依赖 `os`、`json`、`random` 库，`datetimeLib` 是对 `fake_useragent` 库进行线下本地文件封装。

`fake_useragent` 这个模块的源码会引用在线资源，所以这个模块是进行几次尝试请求一个网站的 `Json` 数据，但是因为各种网络原因请求超时，所以就会报错，为了解决这个问题，`userAgentLib` 将原版 `Json` 问价下载到本地，最新版本文件为：`0.1.11`。

下面是对 `userAgentLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `userAgentLib` 的使用 `demo`

### 二、安装

`userAgentLib` 是以源码的方式呈现，使用的时候直接导入即可

	from userAgentLib import dt
    
### 三、使用

`userAgentLib` 所有的功能都是 `ua` 的属性，它的返回值都是 `string` 类型，`userAgentLib` 只包括一个功能 `get` 方法

直接使用 ua.get 就会得到一串 `UA` 头部信息的字符串

    ua.get
