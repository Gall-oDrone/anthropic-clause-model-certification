def basic_prompt(complaint):
    return f"""
    Classify the following customer complaint into one or more of these categories:
    Software Bug, Hardware Malfunction, User Error, Feature Request, or Service Outage.
    Only respond with the classification.

    Complain: {complaint}

    Classification:
    """

def improved_prompt(complaint):
    return f"""
    You are an AI assistant specializing in customer support issue classification. Your task is to analyze customer

    1.  Software Bug: Issues related to software not functioning as intended.
    2. Hardware Malfunction: Problem with physical devices or components.
    3. User Error: Difficulties arising form user misunderstanding or miuse.
    4. Feature Request: Suggestions for new funcitonalities or improvements.
    5. Service Outage: System-wide issues affecting service availability.

    Important Guidelines:
    - A complaint may fall into multiple categories. If so, list all that apply but try to prioritize picking a

    Examples:
    1. Complaint: "The app crashes when I try to save my progress."
    Classification: Software Bug

    2. Complaint: "My keyboard isn't working after I spilled coffee on it."
    Classification: Hardware Malfunction
    
    3. Complaint: "My keyboard isn't working after I spilled coffee on it."
    Classification: Hardware Malfunction
    
    4. Complaint: "It would be great if your app had a dark mode."
    Classification: Feature Request
    
    5. Complaint: "None of your services are loading for me or my colleagues."
    Classification: Service Outage
    
    6. Complaint: "My keyboard isn't working after I spilled coffee on it."
    Classification: Hardware Malfunction
    """

def basic_summarize(article):
    return f"Summarize this article {article}"

def better_summarize(article):
    return f"""
    Summarize this article for a grade-school audience: {article}
    """

def best_summarize(article):
    return f"""
    You are tasked with summarizing long wikipedia articles for a grade-school audience.
    Write a short summary, keeping itt as concise as posssible.
    The summary is intended for a non-technocal, grade-school audience.
    This is the article: {article}
    """