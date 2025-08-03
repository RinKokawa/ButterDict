# 🧈 ButterDict - 黄油字典

**ButterDict** 由于本人收集了不少小黄油，为了避免有一天会解压不了项目，所以写了这个脚本，用于提取 `ButterDict.csv` 中的密码字段，生成纯密码字典文件 `ButterDict.txt`。

---

## 📂 项目结构

```

ButterDict/  
├── ButterDict.csv # 密码字典文件（含备注）  
├── ButterDict.txt # 提取后生成的纯密码字典（每行一个）  
├── ButterDictExtract.py # 提取脚本  
└── README.md # 项目说明

```
---

## 📝 文件格式说明

### ButterDict.csv

```csv
password,remark
example123,example.com 注册默认
event2024,活动通用密码
123456,常见弱口令
...
```

-   **password**：实际用于爆破的密码
    
-   **remark**：备注信息，可用于记录来源、用途等说明
    

### ButterDict.txt（由脚本生成）

```txt
example123
event2024
123456
...
```

仅保留纯密码行，适用于大多数压缩包爆破工具。

---

## 🚀 使用方法

确保你已安装 Python 3，然后在终端或 PowerShell 中运行以下命令：

```bash
python ButterDictExtract.py
```

执行后，将读取 `ButterDict.csv` 中所有 `password` 字段，生成 `ButterDict.txt` 文件。

---

## 🧰 示例用途

-   压缩包恢复工具，如：`fcrackzip`、`John the Ripper`、`rarcrack`
    
-   自定义弱口令字典生成
    
-   安全教育与合法授权下的渗透测试字典构建
    

⚠ 本工具仅用于合法用途，如忘记密码的文件恢复、渗透测试授权目标等，**禁止用于非法用途**。