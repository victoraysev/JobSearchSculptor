import re
from openai import OpenAI

def run(prompt, tokens, api_key):

    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return chat_completion.choices[0].message.content


def generate_cover_letter(title, company, description, resume, api_key, tokens):
    if not api_key:
        return "No API key provided"
    with open('./genai/promt.txt', 'r') as file:
        promt = file.read().replace('[title]', title).replace('[company]', company).replace('[description]', description).replace('[resume]', resume)
        return run(promt, tokens, api_key)


if __name__ == '__main__':
    with open('example/title.txt', 'r') as file:
        title = file.read()
    with open('example/company.txt', 'r') as file:
        company = file.read()
    with open('example/description.txt', 'r') as file:
        description = file.read()
    with open('example/resume.txt', 'r') as file:
        resume = file.read()
    generate_cover_letter(title, company, description, resume, 100, '')