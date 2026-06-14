# RagFlow_summary(基于RAGFlow聊天日志的学习行为分析系统)
以RagFlow为基础的简单知识问答的AI总结（总结最近的n条记录）
## 1. 项目简介

本项目基于开源RAG平台RAGFlow，设计并实现了一个聊天日志分析系统。

系统能够自动读取RAGFlow中的用户历史对话记录，利用大语言模型进行分析，并生成学习建议报告。

本项目主要研究：

- RAG系统部署与使用
- 聊天数据采集
- 大模型API调用

---

## 2. 系统架构

```text
RAGFlow
   │
   │ 对话记录
   ▼
MySQL数据库
   │
   ▼
chat_collector.py
   │
   ▼
chats.json
   │
   ▼
chat_analyzer.py
   │
   ▼
Qwen3.6-35B-A3B
   │
   ▼
analysis.md
```

---

## 3. 功能说明

### 3.1 chat_collector.py

功能：

- 连接RAGFlow MySQL数据库
- 读取conversation表
- 提取最近聊天记录
- 保存为JSON文件

输出：

```text
outputs/chats.json
```

---

### 3.2 chat_analyzer.py

功能：

- 读取聊天记录
- 构造Prompt
- 调用大语言模型
- 分析用户学习行为
- 输出Markdown报告

输出：

```text
outputs/analysis.md
```

分析内容包括：

- 学习领域分析
- 高频问题分析
- 兴趣关键词提取
- 知识结构画像
- 薄弱知识点分析
- 学习建议生成

---

## 4. 运行环境

### 操作系统

Ubuntu 22.04 (WSL2)

### Python版本

Python 3.10+

### 数据库

MySQL 8.0

### 大模型

Qwen/Qwen3.6-35B-A3B

---

## 5. 安装依赖

```bash
pip install -r requirements.txt
```

---

## 6. 配置环境变量

创建 `.env` 文件：

```env
API_KEY=your_api_key

BASE_URL=https://api.siliconflow.cn/v1

MODEL_NAME=Qwen/Qwen3.6-35B-A3B
```

---

## 7. 运行步骤

### Step1 采集聊天记录

```bash
python chat_collector.py
```

生成：

```text
outputs/chats.json
```

---

### Step2 分析聊天记录

```bash
python chat_analyzer.py
```

生成：

```text
outputs/analysis.md
```

---

## 8. 实验结果

系统能够自动分析用户与RAGFlow之间的对话内容，并生成学习画像。

示例结果：

- 用户主要关注数据结构与人工智能领域
- 高频问题集中于算法和RAG技术
- 推荐进一步学习Transformer与向量检索技术

---


## 10. 参考项目

- RAGFlow
- Qwen3.6-35B-A3B
- MySQL
- OpenAI Python SDK
