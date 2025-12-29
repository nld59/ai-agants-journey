# AI Agents Journey

Learning how to build AI agents from scratch.
Week 0: project setup, Python environment, Git initializ

### Week 1 — Day 1 Notes

**Why system message is important:**
System message defines global rules for the model: its role, constraints, output format, and priorities.  
It acts as a behavioral contract that controls how the model should respond to all subsequent inputs.

**Why tokens matter for architecture:**
Tokens matter because they limit the amount of context the model can process, which affects how data must be structured, summarized, or stored across requests.

**Example where LLM can fail:**
LLMs can fail in tasks that require strict symbolic or step-by-step logic.  
For example, when asked to reverse the letters in the word "lollipop", the model may give an incorrect answer because it predicts tokens probabilistically rather than manipulating characters explicitly.

### Week 1 — Day 2 Notes

**Why classification is a system-level task:**
Classification is a system-level task because it is used to route user requests within the application.  
By identifying the type of request first, the system can apply specialized instructions or logic, making the overall behavior more stable, controllable, and scalable.

**Why moderation should happen before generation:**
Moderation should be applied before generating a response to prevent the system from processing or producing unsafe or disallowed content.  
This reduces safety, legal, and reputational risks, not just computational cost.

**Example of missing moderation risk:**
Without moderation, a system may respond to inappropriate requests, such as when a child asks about adult content.  
In such cases, the LLM could generate responses that violate safety policies or regulations.

## Week 1 Day 3
- First Python LLM integration
- Input moderation before processing
- System-level classification with strict JSON output

## Week 1 Day 4
- Validating LLM outputs
- Safe JSON parsing
- Handling unreliable model responses

## Week 1 Day 5
- Added retry strategy for classification
- Added fallback when model output is invalid
- System stays stable under API/format failures

## Week 1 Summary
- System-level prompt design
- Classification and moderation pipelines
- LLM output validation
- Retry and fallback strategies for reliability