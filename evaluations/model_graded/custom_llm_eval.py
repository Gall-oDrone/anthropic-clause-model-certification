import anthropic
import os
import json

def llm_eval(summary, article):
    """
    Evaluate summary using an LLM (Claude).

    Args:
    summary (str): The summary to evaluate.
    article (str): The original text that was summarized.

    Returns:
    bool: True if the average score is above the threshold, False otherwise.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""Evaluate the following summary based on these criteria:
    1. Conciseness (1-5) - is the summary as concise as possible?
        - Conciseness of 1: The summary is unnecessarily long, including excessive details, repetitions, or irr
        - Conciseness of 3: The summary captures most key points but could be more focused. It may include some
        - Conciseness of 5: The summary effectively condenses the main ideas into a brief, focused text. It
    2. Accuracy (1-5) - is the summary completely accurate based on the initial article?
        - Accuracy of 1:
        - Accuracy of 3:
        - Accuracy of 5:
    4. Tone (1-5) - is the summary appropriate for a grade school student with no technical training?
        - Tone of 1:
        - Tone of 3:
        - Tone of 5:
    5. Explanation - a general description of the way the summary is evaluated
    """