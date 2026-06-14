from openai import OpenAI

client = OpenAI(
    api_key="sk-ttysbyysaxtkdyxdpiiutghnxuowvowekxzrsdocskzfqzvc",
    base_url="https://api.siliconflow.cn/v1"
)

models = client.models.list()

for m in models.data:
    print(m.id)
