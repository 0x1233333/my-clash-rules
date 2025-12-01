import requests
import yaml
import json
import os
import re

# 配置文件路径
CONFIG_FILE = 'sources.yaml'
# 输出目录
OUTPUT_CLASH = 'rules/clash'
OUTPUT_SINGBOX = 'rules/singbox'

def download_content(url):
    """下载规则内容"""
    try:
        print(f"正在下载: {url}")
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        print(f"下载失败 {url}: {e}")
    return ""

def parse_content(content):
    """解析内容，提取纯净的域名或IP"""
    lines = content.splitlines()
    payload = set() # 使用集合自动去重

    for line in lines:
        line = line.strip()
        # 跳过空行和注释
        if not line or line.startswith('#'):
            continue
        
        # 处理 YAML 格式 (- 'domain')
        if line.startswith("- '") and line.endswith("'"):
            item = line[3:-1]
            payload.add(item)
            continue
        
        # 处理 Clash 格式 (DOMAIN-SUFFIX,google.com,Proxy)
        if ',' in line:
            parts = line.split(',')
            if len(parts) >= 2:
                # 取第二个元素作为值 (domain 或 ip)
                payload.add(parts[1].strip())
            continue
            
        # 处理纯文本格式
        payload.add(line)
        
    return payload

def generate_clash(name, rule_type, dataset):
    """生成 Clash 格式文件"""
    # 映射类型名称
    clash_type = "DOMAIN-SUFFIX"
    if rule_type == "domain-keyword": clash_type = "DOMAIN-KEYWORD"
    if rule_type == "domain": clash_type = "DOMAIN"
    if rule_type == "ip-cidr": clash_type = "IP-CIDR"

    filename = os.path.join(OUTPUT_CLASH, f"{name}.list")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# NAME: {name}\n")
        f.write(f"# TYPE: {clash_type}\n")
        f.write(f"# COUNT: {len(dataset)}\n")
        f.write("\n")
        for item in sorted(dataset):
            # IP-CIDR 需要特殊处理 /32
            if rule_type == 'ip-cidr' and '/' not in item:
                f.write(f"{clash_type},{item}/32,no-resolve\n")
            elif rule_type == 'ip-cidr':
                f.write(f"{clash_type},{item},no-resolve\n")
            else:
                f.write(f"{clash_type},{item}\n")
    print(f"Clash 规则已生成: {filename}")

def generate_singbox(name, rule_type, dataset):
    """生成 Sing-box (JSON Source) 格式文件"""
    srs_data = {
        "version": 1,
        "rules": []
    }
    
    rule_obj = {}
    
    # 映射 Sing-box 类型
    if rule_type == "domain-suffix":
        rule_obj["domain_suffix"] = sorted(list(dataset))
    elif rule_type == "domain-keyword":
        rule_obj["domain_keyword"] = sorted(list(dataset))
    elif rule_type == "domain":
        rule_obj["domain"] = sorted(list(dataset))
    elif rule_type == "ip-cidr":
        rule_obj["ip_cidr"] = sorted(list(dataset))
        
    srs_data["rules"].append(rule_obj)

    filename = os.path.join(OUTPUT_SINGBOX, f"{name}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(srs_data, f, indent=2, ensure_ascii=False)
    print(f"Sing-box 规则已生成: {filename}")

def main():
    # 创建输出目录
    os.makedirs(OUTPUT_CLASH, exist_ok=True)
    os.makedirs(OUTPUT_SINGBOX, exist_ok=True)

    # 读取配置
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # 遍历每个分类
    for category in config['sources']:
        name = category['name']
        rule_type = category['type']
        urls = category['urls']
        
        print(f"\n正在处理分类: {name} ...")
        
        # 聚合该分类下的所有数据
        merged_data = set()
        for url in urls:
            content = download_content(url)
            parsed = parse_content(content)
            merged_data.update(parsed)
        
        print(f"去重后数据量: {len(merged_data)}")
        
        # 生成文件
        if merged_data:
            generate_clash(name, rule_type, merged_data)
            generate_singbox(name, rule_type, merged_data)

if __name__ == "__main__":
    main()
