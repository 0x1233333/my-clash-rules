关于开源协议的选择，针对你这种“工具脚本 + 数据聚合”类型的仓库，我的建议如下：

### 📜 推荐协议：MIT License

**理由：**

1.  **最通用、最宽松：** MIT 协议的核心含义是“你可以拿去随便用，只要保留我的署名即可”。这非常适合规则列表和脚本类项目。
2.  **社区习惯：** Clash/Sing-box 社区（包括 blackmatrix7 等大佬）大多使用 MIT 或 Apache 2.0，方便大家互相引用和二次开发。
3.  **避免麻烦：** 你的仓库包含代码（Python 脚本）和数据（规则）。MIT 协议简单明了，避免了 GPL 那种“传染性”带来的复杂法律边界问题。

**如何添加：**
在 GitHub 仓库页面点击 `Add file` -\> `Create new file`，文件名输入 `LICENSE`，然后点击右侧出现的 `Choose a license template` 按钮，选择 **MIT License** 提交即可。

-----

### 📝 修正后的 README.md

既然 `0x1233333` 是你自己，那就不需要把它列在“致谢上游”里了（那是你自己的资产）。我已经把这一项去掉，并更新了简介。

你可以直接复制下面的内容覆盖：

-----

# 🛡️ 全自动规则聚合工厂 (Auto Rules Factory)

> **仓库地址**: [https://github.com/0x1233333/my-clash-rules](https://www.google.com/search?q=https://github.com/0x1233333/my-clash-rules)
> **开源协议**: MIT License

### 📖 项目简介

这是一个基于 GitHub Actions 的自动化规则处理工厂。
核心目标是：**解决上游规则格式不兼容 Subconverter 的问题，同时实现多源聚合、自动去重与分类。**

脚本每天自动从各大高质量上游拉取规则，进行清洗（去除 YAML 语法）、去重、合并，并生成 **Clash** (.list) 和 **Sing-box** (.json) 双平台通用的标准规则文件。

-----

### 🌟 特别致谢与上游来源

本项目的数据核心来源于以下优秀的开源项目，经过脚本聚合与清洗后生成：

  * **[Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules)** (基础规则、GFW、直连、IP库)
  * **[ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)** (流媒体、游戏、应用分流)
  * **[StricklandF/Filter](https://www.google.com/search?q=https://github.com/StricklandF/Filter)** (金融、银行、券商、冷门应用)
  * **[blackmatrix7/ios\_rule\_script](https://github.com/blackmatrix7/ios_rule_script)** (PikPak、部分游戏规则)

-----

### 📂 目录结构

```text
.
├── rules/                  # [自动生成] 最终产出的规则文件
│   ├── clash/              # Clash 专用 (.list 格式，标准逗号分隔)
│   └── singbox/            # Sing-box 专用 (.json 格式，source rule)
├── script/                 # 核心处理脚本 (main.py)
├── sources.yaml            # [配置] 上游源与分类管理
└── .github/workflows/      # [自动化] 每天北京时间 04:00 自动更新
```

-----

### 🔗 规则引用地址 (Clash / ACL4SSR 专用)

**基础路径前缀:**
`https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/`

#### 1\. 核心应用

| 规则名称 | 文件名 | 说明 |
| :--- | :--- | :--- |
| **苹果服务** | `Apple.list` | 包含 App Store, iCloud, Apple TV 等 |
| **微软服务** | `Microsoft.list` | 包含 Windows Update, OneDrive, Office 等 |
| **谷歌服务** | `Google.list` | 包含 FCM 推送, Google 通用服务 |
| **AI 平台** | `AI.list` | 包含 OpenAI, Gemini, Claude, Copilot 等 |
| **即时通讯** | `Chat.list` | 包含 Telegram, WhatsApp, Line 等 |

#### 2\. 金融与资产

| 规则名称 | 文件名 | 说明 |
| :--- | :--- | :--- |
| **加密货币** | `Crypto.list` | 包含 Binance, OKX, Metamask, TradingView 等 |
| **国际银行** | `Finance.list` | 包含 PayPal, Wise, HSBC, OCBC 等 |
| **券商股票** | `Securities.list` | 包含 富途, 老虎, 盈透, 东方财富国际等 |

#### 3\. 媒体与游戏

| 规则名称 | 文件名 | 说明 |
| :--- | :--- | :--- |
| **YouTube** | `YouTube.list` | 油管专用 |
| **Netflix** | `Netflix.list` | 奈飞专用 |
| **国外媒体** | `Media.list` | 包含 Disney+, HBO, Spotify, 巴哈姆特等 |
| **国内媒体** | `ChinaMedia.list` | 包含 Bilibili, 网易云音乐 (用于回国模式或直连) |
| **游戏平台** | `Games.list` | 包含 Steam, Epic, PSN, Xbox, Switch |

#### 4\. 基础分类

| 规则名称 | 文件名 | 说明 |
| :--- | :--- | :--- |
| **代理列表** | `Proxy.list` | 包含 GFWList, 国外常用域名, 兜底代理 |
| **直连列表** | `Direct.list` | 包含 国内域名, 局域网, Private |
| **广告拦截** | `Reject.list` | 包含 常用广告域名屏蔽 |
| **国内 IP** | `CN-IP.list` | 纯 IP 规则 |
| **电报 IP** | `TelegramIP.list` | 纯 IP 规则 |

-----

### 📝 ACL4SSR 配置文件 (INI) 引用示例

建议在您的 `ACL4SSR_Online_My.ini` 中使用以下配置，实现全规则覆盖：

```ini
; === 应用与媒体 ===
ruleset=🍎 苹果服务,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Apple.list
ruleset=Ⓜ️ 微软服务,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Microsoft.list
ruleset=📢 谷歌FCM,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Google.list
ruleset=💬 Ai平台,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/AI.list
ruleset=📲 电报信息,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Chat.list
ruleset=📹 油管视频,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/YouTube.list
ruleset=🎥 奈飞视频,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Netflix.list
ruleset=🌍 国外媒体,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Media.list
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Games.list

; === 金融与交易 ===
ruleset=💰 加密货币,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Crypto.list
ruleset=💸 金融服务,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Finance.list
ruleset=📈 券商股票,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Securities.list

; === 基础规则 ===
ruleset=🛑 广告拦截,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Reject.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Direct.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/CN-IP.list
ruleset=🚀 节点选择,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Proxy.list
```

-----

### ⚙️ 自动化机制

  * **更新频率**: 每天北京时间凌晨 04:00 (UTC 20:00) 自动触发。
  * **处理逻辑**:
    1.  从 `sources.yaml` 读取上游链接。
    2.  下载原始内容 (支持 YAML/Text)。
    3.  提取有效载荷 (Domain/IP)。
    4.  **分类去重**：同一分类下的多个源自动合并去重。
    5.  **格式化**：转换为标准 Clash 和 Sing-box 格式。
    6.  推送到 `rules/` 目录。
