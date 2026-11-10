from llm_utils import call_llm
from resume_parser import resume_schema

SYSTEM_PROMPT = f"""
ROLE: You are an AI-powered Resume Assistant designed to help HR professionals and recruiters interact conversationally with a candidate's resume.

TASK: Your primary responsibility is to answer questions about the candidate accurately, professionally, and exclusively based on the information contained in the provided resume. The structured input (resume) format: {resume_schema}

"""


def ask_candidate(question, resume):

    query_prompt = f"""
    Candidate Resume:
    {resume}

    HR/RECRUITER QUESTION:
    {question}
    """

    answer = call_llm(SYSTEM_PROMPT, query_prompt)
    return answer
