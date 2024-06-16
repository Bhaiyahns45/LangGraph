![image](https://github.com/Bhaiyahns45/LangGraph/assets/72096831/b1700092-6c32-4474-a8f3-28aebd746698)


LangGraph is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Compared to other LLM frameworks, it offers these core benefits: cycles, controllability, and persistence. LangGraph allows you to define flows that involve cycles, essential for most agentic architectures, differentiating it from DAG-based solutions. As a very low-level framework, it provides fine-grained control over both the flow and state of your application, crucial for creating reliable agents. Additionally, LangGraph includes built-in persistence, enabling advanced human-in-the-loop and memory features.

LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

### Key Features

Cycles and Branching: Implement loops and conditionals in your apps.

Persistence: Automatically save state after each step in the graph. Pause and resume the graph execution at any point to support error recovery, human-in-the-loop workflows, time travel and more.

Human-in-the-Loop: Interrupt graph execution to approve or edit next action planned by the agent.

Streaming Support: Stream outputs as they are produced by each node (including token streaming).

Integration with LangChain: LangGraph integrates seamlessly with LangChain and LangSmith (but does not require them).

