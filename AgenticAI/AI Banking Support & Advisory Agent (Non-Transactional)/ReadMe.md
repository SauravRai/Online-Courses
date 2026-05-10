In this Industry Capstone, you will work as an AI Engineer or Applied AI Consultant inside a company. The organization wants to deploy an AI agent that can assist users in real workflows — handling ambiguity, reasoning across steps, using tools, learning from feedback, and operating safely in production.
Your responsibility is to design, build, test, iterate, and justify an AI agent in an industry setting, not as a one-off prototype.

Problem Statement
You must design an AI agent to support a realistic business workflow in a chosen industry scenario. The agent should demonstrate reliability, explainability, safety-first behaviour, and practical usefulness for real users, with evidence through artefacts and test logs.

Your final submission should make it clear:

who the user is and what workflow the agent supports,
what success looks like (criteria + metrics),
what failures you anticipated and how you handled them,
and why your architecture/design decisions are justified.

Framework Requirement:
Framework-Based: LangChain OR CrewAI OR Flowise.


Scenario: Banking — AI Banking Support & Advisory Agent (Non-Transactional)
Safety Requirements:

Must refuse money movement, approvals, or legal advice.
Must not hallucinate customer data.
Must escalate ambiguous or high-risk cases.
Must not store PII in logs.

Task to be performed
You will build the agent following an industry workflow across the phases below. Your submission must include clear evidence (screenshots/logs/tables/artefacts) for the key capabilities.

Phase 1: Understand the Problem & Define Success
Coding: Not Required (optional)

Tools/Skills: Problem framing, user persona definition, workflow mapping, requirements writing, success criteria, edge-case thinking, evaluation planning

- Identify the primary user persona and daily workflow
- Document the exact problem to be solved
- Define inputs, outputs, constraints, and assumptions
- Write 3–5 example user questions
- Define success criteria
- List known failure cases and edge scenarios


Phase 2: Build a Basic Working Agent
Coding: Required

Tools/Skills: Python, CLI or notebook workflow, input/output handling, basic rules/templates, logging sample runs

- Create a Python-based agent
- Handle user input and generate responses
- Demonstrate baseline limitations

Tasks:
- Create a Python-based agent that accepts user input
- Implement basic response generation (rules or templates)
- Demonstrate at least 2 limitations of the baseline agent
- Log sample interactions and responses
- Explain why this version is insufficient for real users



Phase 3: Make the Agent Smarter
Coding: Required

Tools/Skills: LLM integration (provider API), prompt engineering, prompt versioning, structured comparison of outputs, error/failure analysis

- Integrate an LLM
- Experiment with prompt strategies
- Show how behaviour changes with better prompts
- 
Tasks:
- Integrate an LLM into the agent workflow
- Design and test multiple prompt strategies
- Compare outputs across prompt variants
- Document improvements and new failure modes
- Select a default prompt strategy with justification


Phase 4: Add Knowledge & Retrieval
Coding: Required

Tools/Skills: Embeddings, semantic search, RAG concepts, text chunking, vector stores (e.g., Chroma/FAISS), retrieval-quality testing

-  Implement embeddings and retrieval
-  Enable document or data reference
-  Show improvement over baseline
Tasks:

-  Prepare documents or datasets for embedding
-  Implement semantic search using embeddings
-  Connect retrieval results to agent responses
-  Compare responses with and without retrieval
-  Handle cases where relevant information is missing


Phase 5: Enable Tool Usage
Coding: Required

Tools/Skills: Tool/function calling, tool schemas, routing/selection logic, guardrails, error handling, loop prevention

Allow the agent to choose and use tools
Demonstrate correct vs incorrect tool usage
Add safeguards

Tasks
Define at least two tools the agent can use
Implement tool calling logic
Demonstrate correct tool selection
Show at least one failed or incorrect tool call
Add safeguards against misuse or loops


Phase 6: Planning, Memory & Context
Coding: Required

Tools/Skills: Planning/task decomposition, conversation state, short-term/long-term memory, memory reset/retention rules, multi-turn testing

Introduce multi-step reasoning
Add memory handling
Improve multi-turn conversations

Tasks
Implement multi-step reasoning or planning logic
Add short-term or long-term memory
Define memory retention and reset behaviour
Demonstrate improved conversation quality
 

Phase 7: Adaptive Behaviour
Coding: Required

Tools/Skills: Feedback collection, storing feedback, behaviour adjustment logic, before/after comparisons, change explanation

Introduce feedback signals
Show behavioural change
Explain the adaptation logic

Tasks
Store feedback for future interactions
Modify behaviour based on feedback
Demonstrate before vs after behaviour
Explain what changed and why
 

Phase 8: Deployment Readiness
Coding: Required

Tools/Skills: Packaging and reproducibility, environment management, basic deployment (local/cloud), logging/tracing, latency/error capture, graceful failure handling

Package for deployment
Add logging and tracing
Handle runtime failures

Tasks
Deploy locally or on the cloud
Capture latency and error logs
Demonstrate graceful failure handling
Document deployment assumptions and limitations
 

Phase 9: Evaluation & Engineering Review
Coding: Required

Tools/Skills: Test harness design, evaluation prompts, quality/consistency metrics, failure analysis (root cause), safety/ethics review, improvement roadmap

Measure response quality
Analyze failures
Review safety and ethiccs

Tasks
Create evaluation prompts and test scenarios
Measure quality and consistency metrics
Perform root cause analysis
Propose next-step improvements


Deliverables
Your final submission package must include:

Working AI Agent
Problem Framing Document (1–2 pages)
Demo Script (3–5 forced interactions)
Evaluation Report
Engineering & Product Justification


Minimum Bar (Required Evidence):
Problem framing document
Forced demo script
Retrieval, tool usage, memory, and adaptation proof
Evaluation report with root cause and fix
Safety enforcement demonstration
Framework usage or justified framework-free design

Required Method (Prompt Comparison Rule): You must demonstrate prompt evaluation using the same test set, 2–3 prompt variants, and a comparison table (Prompt → Output → What Improved/Worsened).


How to Approach the Project
Build your capstone like an industry project: define success, ship a baseline, iterate with evidence, and document tradeoffs. Your artifacts should make your decisions easy to evaluate.

Start with a clear persona + workflow and define success criteria early.
Show the evolution: baseline → LLM → retrieval → tools → memory/planning → adaptation.
Use logs/screenshots/tables as evidence — not just narrative claims.
Demonstrate at least one failure case with root cause and a fix (before/after proof).
Treat safety as a feature: refusals, uncertainty, escalation, and PII-safe logging.








