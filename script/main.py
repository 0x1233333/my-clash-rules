sources:
  # ============================================
  # 1. 核心大厂与系统服务 (通用 - 不分级)
  # ============================================
  - name: "Apple"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Apple.list"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/apple.txt"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/icloud.txt"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/AppStore.list"

  - name: "Microsoft"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/Microsoft.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OneDrive/OneDrive.list"

  - name: "Google"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/GoogleCN.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleFCM/GoogleFCM.list"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/google.txt"

  # ============================================
  # 2. 垂直领域 (通用 - 不分级)
  # ============================================
  - name: "AI"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/AI.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Gemini/Gemini.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Claude/Claude.list"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/OpenAI.list"

  - name: "Chat"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Telegram.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/WhatsApp/WhatsApp.list"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/Skype.list"

  - name: "Social"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Instagram/Instagram.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok.list"

  - name: "Crypto"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/0x1233333/bank-Crypto/refs/heads/main/Crypto.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Crypto/Crypto.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Binance/Binance.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OKX/OKX.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TradingView/TradingView.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/MetaMask/MetaMask.list"

  - name: "Finance"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PayPal/PayPal.list"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/Wise.list"

  - name: "Securities"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/Securities.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Futu/Futu.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TigerBrokers/TigerBrokers.list"

  - name: "Media"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyMedia.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Disney/Disney.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Spotify/Spotify.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Netflix/Netflix.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.list"

  - name: "Games"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Steam/Steam.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Epic/Epic.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nintendo/Nintendo.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Sony/Sony.list"

  # ============================================
  # 3. 基础代理分类 (分级生成)
  # ============================================

  # === ProxyFull (超大杯) ===
  # 包含 GFWList, 非CN域名, 以及各类杂项。体积巨大，抗污染最强。
  - name: "ProxyFull"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Global/Global.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Proxy/Proxy.list"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/tld-not-cn.txt"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/Grab.list"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/Uber.list"

  # === ProxyLite (中杯 - 推荐) ===
  # 包含 ACL 和 LS 的常用代理列表。平衡之选。
  - name: "ProxyLite"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyLite.list"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/proxy.txt"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/Grab.list"
      - "https://raw.githubusercontent.com/StricklandF/Filter/main/Uber.list"

  # === ProxyMini (小杯) ===
  # 仅包含核心域名。极小。必须配合 GEOIP,CN 使用。
  - name: "ProxyMini"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyLite.list"

  # ============================================
  # 4. 直连与IP分类 (分级生成)
  # ============================================

  # === DirectFull (超大杯 - 不推荐用于普通路由) ===
  # 包含所有中国域名列表。体积巨大。
  - name: "DirectFull"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/China/China.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Download/Download.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Lan/Lan.list"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/private.txt"

  # === DirectLite (中杯 - 推荐) ===
  # 仅包含局域网、下载、特定中国服务(Steam/GoogleCN)。常规国内网站走 GEOIP。
  - name: "DirectLite"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Lan/Lan.list"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/private.txt"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Download/Download.list"
      - "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/GoogleCN.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/SteamCN/SteamCN.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/MicrosoftCN.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Apple/AppleCN.list"

  # === 广告拦截 ===
  - name: "Reject"
    type: "domain-suffix"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Advertising/Advertising.list"
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Privacy/Privacy.list"
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/reject.txt"

  # === IP 规则 ===
  - name: "CN-IP"
    type: "ip-cidr"
    urls:
      - "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ChinaIPs/ChinaIPs.list"

  - name: "TelegramIP"
    type: "ip-cidr"
    urls:
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt"

  # === 应用程序 ===
  - name: "Applications"
    type: "process-name"
    urls:
      - "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/applications.txt"
