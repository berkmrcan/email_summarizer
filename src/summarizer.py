from openai import OpenAI
import re 

def summarize(contents):
    client = OpenAI()
    contents = contents[:3] # debuggin purposes
    string = [f"Content {i+1}: {content}" for i, content in enumerate(contents)]
    string = "\n".join(string)
    string = "I want you to summarize the following paper contents. Keep the summaries super short, precise and straight-forward. You should return the summaries in this format: Summary 1: summary_of_content_1 $$ Summary 2: ... etc. Make sure the dollar signs are there im between. Here are the contents:" + "\n" + string
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": string}
    ]
    )
    return process_summaries(completion.choices[0].message.content)
    
def process_summaries(summaries):
    summaries = summaries.split("$$")
    summaries = [sum.rstrip() for sum in summaries]
    summaries = [sum.lstrip() for sum in summaries]
    summaries = [re.sub(r'^Summary \d+:?', '', summary).strip() for summary in summaries]
    return summaries