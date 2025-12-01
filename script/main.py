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
    """解析内容，提取纯净的规则实体"""
    lines = content.splitlines()
    payload = set()

    for line in lines:
        line = line.strip()
        # [基础过滤]
        if not line or line.startswith('#') or line.startswith('//'):
            continue
        
        # [核心修复] 全局查杀 payload 关键字
        # 无论是什么文件，只要包含 payload: 或者等于 payload，直接跳过
        if 'payload' in line.lower():
            continue

        # 暴力过滤 YAML 键值
        if ':' in line and not line.startswith('http'):
            continue

        # 处理 YAML 列表格式 (- 'value')
        if line.startswith("- '") and line.endswith("'"):
            item = line[3:-1]
            payload.add(item)
            continue
        if line.startswith('- "') and line.endswith('"'):
            item = line[3:-1]
            payload.add(item)
            continue
        if line.startswith("- "):
            item = line[2:].strip()
            payload.add(item)
            continue
        
        # 处理 Clash 格式 (TYPE,value,...)
        if ',' in line:
            parts = line.split(',')
            if len(parts) >= 2:
                payload.add(parts[1].strip())
            continue
            
        # 处理纯文本格式
        payload.add(line)
        
    return payload

def generate_clash(name, rule_type, dataset):
    """生成 Clash 格式文件 (.list)"""
    # 映射 Clash 类型
    clash_type = "DOMAIN-SUFFIX"
    if rule_type == "domain-keyword": clash_type = "DOMAIN-KEYWORD"
    if rule_type == "domain": clash_type = "DOMAIN"
    if rule_type == "ip-cidr": clash_type = "IP-CIDR"
    if rule_type == "process-name": clash_type = "PROCESS-NAME"

    filename = os.path.join(OUTPUT_CLASH, f"{name}.list")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# NAME: {name}\n")
        f.write(f"# TYPE: {clash_type}\n")
        f.write(f"# COUNT: {len(dataset)}\n")
        f.write("\n")
        for item in sorted(dataset):
            # [IP清洗] 确保 IP 规则里没有怪东西
            if rule_type == 'ip-cidr':
                if re.search(r'[a-zA-Z]', item): # 如果包含字母，跳过
                    continue
                if '/' not in item:
                    f.write(f"{clash_type},{item}/32,no-resolve\n")
                else:
                    f.write(f"{clash_type},{item},no-resolve\n")
            else:
                f.write(f"{clash_type},{item}\n")
    print(f"Clash 规则已生成: {filename}")

def generate_singbox(name, rule_type, dataset):
    """生成 Sing-box 格式文件 (.json)"""
    srs_data = {
        "version": 1,
        "rules": []
    }
    
    clean_dataset = []
    if rule_type == "ip_cidr" or rule_type == "ip-cidr":
        for item in dataset:
            if re.search(r'[a-zA-Z]', item):
                continue
            clean_dataset.append(item)
    else:
        clean_dataset = list(dataset)

    if not clean_dataset:
        return

    rule_obj = {}
    dataset_list = sorted(clean_dataset)

    # 映射 Sing-box 类型
    if rule_type == "domain-suffix":
        rule_obj["domain_suffix"] = dataset_list
    elif rule_type == "domain-keyword":
        rule_obj["domain_keyword"] = dataset_list
    elif rule_type == "domain":
        rule_obj["domain"] = dataset_list
    elif rule_type == "ip-cidr":
        rule_obj["ip_cidr"] = dataset_list
    elif rule_type == "process-name":
        rule_obj["process_name"] = dataset_list
        
    srs_data["rules"].append(rule_obj)

    filename = os.path.join(OUTPUT_SINGBOX, f"{name}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(srs_data, f, indent=2, ensure_ascii=False)
    print(f"Sing-box 规则已生成: {filename}")

def main():
    os.makedirs(OUTPUT_CLASH, exist_ok=True)
    os.makedirs(OUTPUT_SINGBOX, exist_ok=True)

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    for category in config['sources']:
        name = category['name']
        rule_type = category['type']
        urls = category['urls']
        
        print(f"\n正在处理分类: {name} ({rule_type}) ...")
        
        merged_data = set()
        for url in urls:
            content = download_content(url)
            parsed = parse_content(content)
            merged_data.update(parsed)
        
        print(f"去重后数据量: {len(merged_data)}")
        
        if merged_data:
            generate_clash(name, rule_type, merged_data)
            generate_singbox(name, rule_type, merged_data)

if __name__ == "__main__":
    main()
