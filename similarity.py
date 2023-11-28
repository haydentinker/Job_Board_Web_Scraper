from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

OPEN_API_KEY=os.getenv('API_KEY')
client=OpenAI(
    api_key=OPEN_API_KEY
)


job_description = """
Key Responsibilities
Collaborate with the development team to conceptualize innovative software solutions.
Design and implement the front-end of applications, ensuring visually appealing and intuitive interfaces.
Develop, manage, and optimize well-functioning databases and applications.
Create and maintain effective APIs.
Conduct software testing for responsiveness and efficiency, ensuring high-quality outputs.
Troubleshoot, debug, and upgrade software to enhance performance.
Produce comprehensive technical documentation.
Work closely with data scientists and analysts to refine and advance software capabilities.
Implement and maintain testing automation to ensure software reliability.
Qualifications
Bachelor’s degree in Computer Science or related field, or equivalent professional certifications.
At least 2 years of full-time, relevant experience in software development.
Proficiency in cloud computing and experience with cloud resource management (GCP experience is advantageous).
Experience in working with APIs.
Strong knowledge and experience in Full Stack development, including:
TypeScript
React / Redux
Python
SQL
HTML/CSS
Additional proficiency in TailwindCSS is preferred.
"""

# Example resume
resume = """
Hayden Tinker
Software Engineer | BS in Computer Science and Business
Administration
Santa Cruz, California, United States
Summary
I'm Hayden Tinker, a dedicated Software Developer based in
Santa Cruz, CA, specializing in Python, SQL, Dart, JavaScript,
HTML, CSS, and web application development. With a Bachelor's
degree in Computer Science and Business Administration from
Walla Walla University, I've designed and built backend systems,
implemented automated testing, and thrived in collaborative
coding environments. My passion for Test-Driven Development,
proficiency in Git, Docker, Jest, Pytest, and VS Code, and a strong
GitHub presence underscore my commitment to delivering highquality software solutions. I'm eager to connect and collaborate on
innovative projects in the ever-evolving tech landscape.
Experience
Walla Walla University
Software Developer
September 2022 - June 2023 (10 months)
Walla Walla, Washington, United States
- Designed and developed the backend of a web-based application using Dart
Shelf for Walla Walla University School of Nursing.
- Streamlined development with implementation of automated testing suite.
- Collaborated with peers and technical mentors in weekly code reviews.
- Organized and overhauled documentation.
Sherwin-Williams
Sales and Management Intern
June 2022 - September 2022 (4 months)
Walla Walla, Washington, United States
- Gained hands-on experience in management, sales, and store operations,
focusing on providing exceptional customer experiences
- Completed marketing project that addressed critical business issues
alongside peers
Page 1 of 2
Monterey Bay Academy
2 years 11 months
Academic Resident Assistant
August 2018 - June 2019 (11 months)
Aptos, California, United States
- Demonstrated leadership by mentoring multiple residents to ensure a safe,
enjoyable, and meaningful living experience.
- Successfully coached students on effective scheduling, study habits, and
academic boundaries to support their academic success.
English I-IV Grader
August 2016 - June 2019 (2 years 11 months)
Aptos, California, United States
- Facilitated an efficient and well-organized process for grading student
assignments, while also providing support to the teacher to create a productive
and effective learning environment.
- Demonstrated a meticulous attention to detail by thoroughly grading essays
and other assignments to maintain high academic standards and ensure
student success.
Education
Walla Walla University
Bachelor of Science - BS, Business Administration and Management,
General · (September 2019 - June 2023)
Walla Walla University
Bachelor of Science - BS, Computer Science · (September 2019 - June 2023)

"""

response=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"system","content":"You are a hiring manager looking at a job description and resume. Your job is to determine how good the candidate would be for the position and assign a percentage to it. In addition to that, you will give important key words for the job description."
        },
        {"role":"user","content":f"Job description:{job_description} and Resume: {resume} "}
    ]
)
print(response)
