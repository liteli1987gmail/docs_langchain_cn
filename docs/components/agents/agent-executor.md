# 代理执行器 Agent Executor

代理执行器（ Agent Executor ）是一个代理（ Agent ）和一组工具（ Tools ）。

代理执行器负责调用代理，获取动作和动作输入，根据动作引用的工具以及相应的输入调用工具，获取工具的输出，然后将所有这些信息传递回代理，以获取它应该采取的下一个动作。

代理执行器充当了协调和管理代理与工具之间交互的角色。


它通过调用代理获取动作和动作输入，然后根据动作引用的工具调用相应的工具进行处理。最后，将工具的输出和其他相关信息传递回代理，以便代理决定下一步应该采取的动作。代理执行器将代理与工具的使用组织起来，以实现更复杂的任务或问题的解决。