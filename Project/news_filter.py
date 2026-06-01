from llm import llm_plain


def is_relevant(article, topic):

    title = article.get("title", "")
    description = article.get("description", "")

    prompt = f"""
You are a news relevance classifier.

Topic: {topic}

Article Title:
{title}

Article Description:
{description}

Rules:
- Return YES if article genuinely belongs to the topic.
- Return NO if article is only loosely related.
- Ignore keyword matches.
- Use semantic understanding.

Return ONLY:
YES
or
NO
"""

    response = llm_plain.invoke(prompt)

    return response.content.strip().upper() == "YES"