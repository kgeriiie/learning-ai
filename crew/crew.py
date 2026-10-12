from crewai import Agent, Task, Crew

pm_agent = Agent(
    role="Product Manager",
    goal="Write a clear, concise feature specification",
    backstory="You are an experienced product manager who writes precise specs for developers.",
    llm="ollama/qwen2.5:14b"
)

pm_task = Task(
    description="Write a short feature spec for: {feature}",
    agent=pm_agent,
    expected_output="A concise feature specification with requirements and edge cases."
)

developer_agent = Agent(
    role="Software Engineer",
    goal="Implement clean, working Python code based on a specification",
    backstory="You are a pragmatic senior developer who writes simple, correct code.",
    llm="ollama/qwen2.5:14b"
)

dev_task = Task(
    description="Based on the specification, implement the core scheduling logic in Python (not the full app, just the key function(s)).",
    agent=developer_agent,
    context=[pm_task],
    expected_output="A Python code snippet implementing the core medication reminder scheduling logic."
)

reviewer_agent = Agent(
    role="Software Engineer",
    goal="Review Python code against specifications to ensure high quality, performance, maintainability, and security by identifying bugs, edge cases, and best practice violations while providing actionable improvements with clear reasoning.",
    backstory="You are a pragmatic senior developer who reviews code.",
    llm="ollama/qwen2.5:14b"
)

review_task = Task(
    description="Review the key Python function(s) for the core scheduling logic based on the specification.",
    agent=reviewer_agent,
    context=[dev_task],
    expected_output="Review the core medication reminder scheduling logic implementation in Python, assessing quality, potential bugs, maintainability, performance, and security, with clear rationale for each suggestion."
)

crew = Crew(agents=[pm_agent, developer_agent, reviewer_agent], tasks=[pm_task, dev_task, review_task])
result = crew.kickoff(inputs={"feature": "a medication reminder feature for a healthcare app"})
print(result)