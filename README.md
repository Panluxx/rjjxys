# rjjxys

## 项目简介

基于 Airtest + Pytest + Pywinauto 的 Windows 桌面客户端（"人教教学易"）UI 自动化测试项目。

## 目录结构

```
rjjxys/
├── Common/              # 公共模块
│   ├── basepage.py      # 基础页面操作类
│   ├── config.py        # 项目路径配置
│   └── logger.py        # 日志处理
├── Setting/             # 配置
│   └── constant.py      # 常量配置（账号、密码等）
├── TestCases/           # 测试用例
│   ├── conftest.py      # pytest fixture
│   ├── test_login/      # 登录模块测试
│   ├── test_lis_7s/     # 历史七年级上测试
│   ├── test_yingw_3s/   # 英语三年级上测试
│   └── ...
├── Picture/             # 图片资源（UI 元素识别图）
├── Report/              # 测试报告
│   ├── xml/             # Allure 原始数据
│   ├── detail_report/   # Allure 报告
│   └── screenshots/     # 失败截图
└── run.py               # 测试执行入口
```

## 环境配置

### 1. 安装依赖

```bash
pip install airtest pytest pywinauto allure-pytest pillow
```

### 2. 配置环境变量（可选）

如需覆盖默认账号密码，可设置环境变量：

```powershell
$env:RJJXYS_USERNAME = '你的账号'
$env:RJJXYS_PASSWORD = '你的密码'
```

## 运行测试

### 运行全部测试

```bash
python run.py
```

### 运行指定标记的测试

```bash
pytest -m smoke    # 冒烟测试
pytest -m login    # 登录相关测试
```

### 生成 Allure 报告

```bash
allure serve Report/xml
```

## 模块说明

| 模块 | 说明 |
|------|------|
| textbook_explain | 教材解析 |
| democlass | 教学课例 |
| digital_classroom | 数字课堂 |
| prepare_resource | 备课资源 |
| teacher_book | 电子教材 |
| design | 教学设计 |
| courseware | 教学课件 |
| example_demo | 例题演示 |
| taping | 课文录音 |
| experiment | 实验探究 |
| music | 音乐欣赏 |
| fine_arts | 美术词典 |
| extend | 拓展资源 |
| material | 素材资源 |
| snow | 冰雪运动 |
| football | 足球运动 |
| animations | 动画素材 |

## 参考资料

- [Airtest 官方文档](https://airtest.readthedocs.io/)
- [Pytest 官方文档](https://docs.pytest.org/)
