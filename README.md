my-clash-rules/
├── .github/
│   └── workflows/
│       └── update.yml      # 自动运行的 Action
├── rules/                  # [自动生成] 存放最终结果
│   ├── clash/              # Clash 格式 (.list)
│   └── singbox/            # Sing-box 格式 (.json)
├── script/                 # 存放 Python 脚本
│   └── main.py
├── sources.yaml            # [核心] 在这里添加/管理你的上游
├── requirements.txt        # Python 依赖
└── README.md
