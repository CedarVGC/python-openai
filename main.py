import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="UUk6VHJekGGJyCbShtdOVIP0aW8HGBZ9SBikPGny1fkXmAW7q3Fk9SYpya-bUjPxyV6AMgbyT3BlbkFJic4FlJCugG5Ys569ObR0v9rOF6Rf3U5hohMMI6BAI8b5eRDgoQluvMAA557K6Seva5LzCVl_oA",
    base_url="https://www.bigdaole.top:8000/v1"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

response_content = chat_completion.choices[0].message.content
# 打印生成的回复
print("ChatGPT回复：", response_content)
