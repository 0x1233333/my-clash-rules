import requests
import yaml

# 定义源文件和目标文件的映射关系，以及对应的规则类型
# 格式: 'Loyalsoldier文件名': ('转换后的文件名', 'Clash规则前缀')
SOURCES = {
    'proxy.txt': ('proxy.list', 'DOMAIN-SUFFIX'),
    'direct.txt': ('direct.list', 'DOMAIN-SUFFIX'),
    'gfw.txt': ('gfw.list', 'DOMAIN-SUFFIX'),
    'apple.txt': ('apple.list', 'DOMAIN-SUFFIX'),
    'icloud.txt': ('icloud.list', 'DOMAIN-SUFFIX'),
    'google.txt': ('google.list', 'DOMAIN-SUFFIX'),
    'tld-not-cn.txt': ('tld-not-cn.list', 'DOMAIN-SUFFIX'),
    'telegramcidr.txt': ('telegram.list', 'IP-CIDR'),
    'cncidr.txt': ('cncidr.list', 'IP-CIDR'),
    'lancidr.txt': ('lancidr.list', 'IP-CIDR'),
    'applications.txt': ('applications.list', 'PROCESS-NAME')
}

BASE_URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/"

def convert():
    for src_file, (dst_file, rule_type) in SOURCES.items():
        url = BASE_URL + src_file
        print(f"正在下载: {url} ...")
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"下载失败: {src_file}")
                continue
            
            # Loyalsoldier 的文件其实是 YAML 格式，只有 payload 部分有用
            try:
                data = yaml.safe_load(response.text)
                payload = data.get('payload', [])
            except yaml.YAMLError:
                print(f"YAML 解析失败，尝试直接按行处理: {src_file}")
                # 备用方案：如果不是标准YAML，尝试按行清洗
                lines = response.text.splitlines()
                payload = []
                for line in lines:
                    line = line.strip()
                    if line.startswith("- '") and line.endswith("'"):
                        payload.append(line[3:-1])
            
            # 写入转换后的文件
            with open(dst_file, 'w', encoding='utf-8') as f:
                f.write(f"# 自动转换自 Loyalsoldier/{src_file}\n")
                f.write(f"# 格式兼容: ACL4SSR / Subconverter\n")
                
                for item in payload:
                    # 写入格式: DOMAIN-SUFFIX,google.com
                    # 如果是IP规则，且不包含/，自动补全/32 (防止报错)
                    if rule_type == 'IP-CIDR' and '/' not in item:
                         f.write(f"{rule_type},{item}/32\n")
                    else:
                         f.write(f"{rule_type},{item}\n")
            
            print(f"转换成功: {dst_file} (包含 {len(payload)} 条规则)")

        except Exception as e:
            print(f"处理出错 {src_file}: {e}")

if __name__ == "__main__":
    convert()
