import json
import pymysql

#读取RAGFlow最新一条完整会话，拆分成问答对，截取最后10组并导出

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="infini_rag_flow",
    database="rag_flow",
    charset="utf8mb4"
)

cursor = conn.cursor()

cursor.execute("""
SELECT message
FROM conversation
ORDER BY create_date DESC
LIMIT 1
""")

messages = json.loads(cursor.fetchone()[0])

qa_pairs = []

current_question = None

for msg in messages:

    role = msg.get("role")

    if role == "user":

        current_question = msg.get("content")

    elif role == "assistant" and current_question:

        qa_pairs.append({
            "question": current_question,
            "answer": msg.get("content")
        })

        current_question = None

qa_pairs = qa_pairs[-10:]

with open(
    "outputs/chats.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        qa_pairs,
        f,
        ensure_ascii=False,
        indent=4
    )

print(f"保存 {len(qa_pairs)} 条问答")
