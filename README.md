这是为您更新的 **README.md**。

根据您最新的 `sources.yaml` 配置，我已经更新了所有的分类（增加了 **ProxyMini**、**Social**、**Crypto全家桶** 等），并且将**所有的引用链接全部展开为完整的 URL**，方便您直接复制使用。

-----

# 🛡️ 全自动规则聚合工厂 (Auto Rules Factory)

> **仓库地址**: [https://github.com/0x1233333/my-clash-rules](https://www.google.com/search?q=https://github.com/0x1233333/my-clash-rules)
>
> **开源协议**: MIT License

### 📖 项目简介

这是一个基于 GitHub Actions 的自动化规则处理工厂。
核心目标是：**解决上游规则格式不兼容 Subconverter 的问题，同时实现多源聚合、自动去重与分类。**

脚本每天自动从各大高质量上游拉取规则，进行清洗（去除 YAML 语法）、去重、合并，并生成 **Clash** (.list) 和 **Sing-box** (.json) 双平台通用的标准规则文件。

-----

### 🌟 数据来源 (Upstream)

本项目的数据核心来源于以下优秀的开源项目，经过脚本聚合与清洗后生成：

  * **[blackmatrix7/ios\_rule\_script](https://github.com/blackmatrix7/ios_rule_script)** (主流应用、流媒体、游戏、加密货币独立规则)
  * **[ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)** (应用分流、基础规则)
  * **[Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules)** (GFWList、CN-IP、直连域名)
  * **[StricklandF/Filter](https://www.google.com/search?q=https://github.com/StricklandF/Filter)** (金融银行、券商、冷门应用)

-----

### 🔗 规则文件引用 (Clash / ACL4SSR 专用)

以下链接可直接填入 ACL4SSR 配置文件 (`.ini`) 或 OpenClash 的 Rule Provider 中。

#### 1\. 核心应用与系统

| 规则名称 | 完整链接 (Raw URL) | 说明 |
| :--- | :--- | :--- |
| **苹果服务** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Apple.list` | App Store, iCloud, Apple Music 等 |
| **微软服务** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Microsoft.list` | Windows Update, OneDrive, Office 等 |
| **谷歌服务** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Google.list` | FCM 推送, Google 通用服务 (不含 YouTube) |
| **AI 平台** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/AI.list` | OpenAI, Gemini, Claude, Copilot 等 |
| **即时通讯** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Chat.list` | Telegram, WhatsApp, Line, Discord 等 |
| **社交媒体** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Social.list` | Twitter, Facebook, Instagram, TikTok 等 |

#### 2\. 金融与资产 (重点优化)

| 规则名称 | 完整链接 (Raw URL) | 说明 |
| :--- | :--- | :--- |
| **加密货币** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Crypto.list` | 包含币安/OKX等主流交易所、TradingView、MetaMask等 |
| **国际银行** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Finance.list` | PayPal, Wise, HSBC, OCBC 等 |
| **券商股票** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Securities.list` | 富途, 老虎, 盈透, 东方财富国际等 |

#### 3\. 媒体与游戏

| 规则名称 | 完整链接 (Raw URL) | 说明 |
| :--- | :--- | :--- |
| **YouTube** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/YouTube.list` | 油管专用规则 |
| **Netflix** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Netflix.list` | 奈飞专用规则 |
| **国外媒体** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Media.list` | Disney+, HBO, Spotify, 巴哈姆特等 |
| **国内媒体** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/ChinaMedia.list` | Bilibili, 网易云音乐 (用于回国模式或直连) |
| **游戏平台** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Games.list` | Steam, Epic, PSN, Xbox, Switch |

#### 4\. 基础分类 (分级代理)

| 规则名称 | 完整链接 (Raw URL) | 说明 |
| :--- | :--- | :--- |
| **代理列表 (Full)** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Proxy.list` | **[巨无霸]** 包含 GFWList + 非 CN 域名 (4万+条)，抗污染最强 |
| **代理列表 (Lite)** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/ProxyLite.list` | **[推荐]** 仅含常见被墙域名，需配合 GEOIP 使用 |
| **代理列表 (Mini)** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/ProxyMini.list` | **[极简]** 仅含最核心代理域名 (\<100KB)，适合老旧设备 |
| **直连列表** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Direct.list` | 国内域名, 局域网, Private |
| **广告拦截** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Reject.list` | 常用广告域名屏蔽 |
| **国内 IP** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/CN-IP.list` | 纯 IP 规则 |
| **电报 IP** | `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/TelegramIP.list` | 纯 IP 规则 |

-----

### 📝 ACL4SSR 配置文件 (INI) 引用示例

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
ruleset=🌍 国外媒体,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Social.list
ruleset=🎮 游戏平台,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Games.list

; === 金融与交易 ===
ruleset=💰 加密货币,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Crypto.list
ruleset=💸 金融服务,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Finance.list
ruleset=📈 券商股票,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Securities.list

; === 基础规则 ===
ruleset=🛑 广告拦截,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Reject.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Direct.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/CN-IP.list
; [可选] 代理列表选一个即可 (Full / Lite / Mini)
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
