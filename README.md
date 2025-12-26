# AI Agents Journey

Learning how to build AI agents from scratch.
Week 0: project setup, Python environment, Git initializ

### Week 1 — Day 1 Notes

**Why system message is important**
System message defines global rules for the model: its role, constraints, output format, and priorities.  
It acts as a behavioral contract that controls how the model should respond to all subsequent inputs.

**Why tokens matter for architecture**
Tokens matter because they limit the amount of context the model can process, which affects how data must be structured, summarized, or stored across requests.

**Example where LLM can fail**
LLMs can fail in tasks that require strict symbolic or step-by-step logic.  
For example, when asked to reverse the letters in the word "lollipop", the model may give an incorrect answer because it predicts tokens probabilistically rather than manipulating characters explicitly.