# Prompt模板 Prompt Templates

“ PromptValue ”是最终传递给模型的内容。大多数情况下，该值不是硬编码的，而是根据用户输入、其他非静态信息（通常来自多个源）和固定的模板字符串动态创建的。

我们将负责创建“ PromptValue ”的对象称为 PromptTemplate。该对象公开了一种将输入变量作为输入并返回“ PromptValue ”的方法。