from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

OPEN_API_KEY=os.getenv('API_KEY')
client=OpenAI(
    api_key=OPEN_API_KEY
)


def findSimilarity(job_description,resume):
    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"system","content":"You are a hiring manager looking at a job description and resume. Your job is to determine how good the candidate would be for the position and assign a percentage to it. In addition to that, you will give important key words for the job description. Give this percentage and key words in a comma separated array."
            },
            {"role":"user","content":f"Job description:{job_description} and Resume: {resume} "}
        ]
    )
    result=response.choices[0].message.content
    print(result)
    return result.split(', ')

