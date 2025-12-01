

# 🛡️ 全自动规则聚合 (Auto Rules Factory)

> **仓库地址**: [https://github.com/0x1233333/my-clash-rules](https://www.google.com/search?q=https://github.com/0x1233333/my-clash-rules)

### 📖 项目简介

这是一个基于 GitHub Actions 的自动化规则处理仓库。
核心目标是：**解决 Loyalsoldier 等上游规则格式不兼容 Subconverter 的问题，同时实现多源聚合与自动更新。**

脚本会自动从 `sources.yaml` 配置的上游拉取规则，进行清洗（去除 YAML 语法）、去重、分类，并生成 **Clash** 和 **Sing-box** 双平台通用的规则文件。

-----

### 📂 目录结构

```text
.
├── rules/                  # [自动生成] 最终产出的规则文件
│   ├── clash/              # Clash 专用 (.list 格式，标准逗号分隔)
│   └── singbox/            # Sing-box 专用 (.json 格式，source rule)
├── script/                 # 核心处理脚本 (main.py)
├── sources.yaml            # [配置文件] 管理上游链接和分类
└── .github/workflows/      # 自动化配置 (每天 04:00 运行)
```

-----

### 🔗 规则引用地址 (Clash / ACL4SSR 专用)

**基础前缀:** `https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/`

#### 1\. 苹果服务 (Apple + iCloud)

```text
https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Apple.list
```

#### 2\. 谷歌服务 (Google)

```text
https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Google.list
```

#### 3\. 代理列表 (Proxy + GFW + Non-CN)

```text
https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Proxy.list
```

#### 4\. 直连列表 (Direct + Local + Private)

```text
https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Direct.list
```

#### 5\. 电报 IP (TelegramIP)

```text
https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/TelegramIP.list
```

#### 6\. 国内 IP (CN-IP)

```text
https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/CN-IP.list
```

#### 7\. 广告拦截 (Reject)

```text
https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Reject.list
```

-----

### 📝 ACL4SSR 配置文件修改示例

如果你想在转换中使用这些规则，请在 INI 配置中这样写：

```ini
; [苹果服务] 使用自建仓库源
ruleset=🍎 苹果服务,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Apple.list

; [谷歌服务] 使用自建仓库源
ruleset=📢 谷歌FCM,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Google.list

; [电报信息] 使用自建仓库源
ruleset=📲 电报信息,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/TelegramIP.list

; [代理兜底] 使用自建仓库源
ruleset=🚀 节点选择,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Proxy.list

; [直连规则] 使用自建仓库源
ruleset=🎯 全球直连,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/Direct.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/LAN-IP.list
ruleset=🎯 全球直连,https://raw.githubusercontent.com/0x1233333/my-clash-rules/main/rules/clash/CN-IP.list
```

-----

### ⚙️ 如何管理规则 (sources.yaml)

所有上游规则都在根目录的 `sources.yaml` 中配置。

**配置示例：**

```yaml
sources:
  - name: "Apple"             # 生成的文件名 (Apple.list)
    type: "domain-suffix"     # 类型: domain-suffix / ip-cidr / process-name
    urls:
      - "https://raw.github.../apple.txt"
```

### 🕒 运行机制

  * **自动运行**：每天北京时间凌晨 04:00。
  * **手动运行**：仓库 `Actions` -\> `Update Rules Factory` -\> `Run workflow`。
