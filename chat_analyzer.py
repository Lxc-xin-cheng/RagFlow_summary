import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import os

# ==========================
# 读取配置
# ==========================

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

# ==========================
# 读取聊天记录
# ==========================

chat_file = Path("outputs/chats.json")

if not chat_file.exists():
    raise FileNotFoundError("找不到 outputs/chats.json")

with open(chat_file, "r", encoding="utf-8") as f:
    chats = json.load(f)

# ==========================
# 构造聊天文本
# ==========================

conversation_text = ""

for item in chats:
    question = item.get("question","").strip()
    answer = item.get("answer","").strip()

    if question:
        conversation_text += f"\n[用户]\n{question}\n"

    if answer:
        conversation_text += f"\n[RAGFlow]\n{answer}\n"

# ==========================
# 分析Prompt
# ==========================

prompt = f"""
你是一名资深学习分析助手。用户正在备考研究生考试，他的备考科目为408（计算机学科专业基础综合）。

下面是用户最近与RAGFlow系统的全部对话记录。请注意，你的回答不需要特别官方，且建议应该聚焦于具体知识点，而非空泛。

请从以下几个方面进行分析：

1. 用户提出的问题出现在408考纲的哪些部分
结合408官方考纲，明确当前学习对应的章节、核心考点范围
2. 用户的问题类型
区分概念背诵、性质证明、原理辨析、考点总结等提问形式，总结用户提问较多的问题类型
3. 用户408学习中遇到专业术语分析
提炼对话中的专业术语、重难点名词，应着重注意一些名词的中英文对应与解释
4. 用户存在的知识薄弱点
重点指出：知识点理解漏洞、细节盲区、易出错点、408考试高频丢分点
5. 用Markdown格式输出

聊天记录如下：

{conversation_text}
"""

# ==========================
# 调用大模型
# ==========================

print("开始分析聊天记录...")

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "system",
            "content": "你是408考研专业课分析专家"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3
)

analysis = response.choices[0].message.content

# ==========================
# 保存结果
# ==========================

output_file = Path("outputs/analysis.md")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(analysis)

print("\n分析完成！")
print(f"结果保存到: {output_file}")
