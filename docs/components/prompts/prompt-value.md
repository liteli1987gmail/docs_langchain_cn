# 提示内容 PromptValue

“提示 Prompt”指的是传递给底层模型的内容。LangChain 提供了几种针对提示的抽象，以处理文本数据。对于其他数据类型（例如图像、音频），我们正在努力添加抽象，但还没有完成。

不同的模型可能期望不同的数据格式。在可能的情况下，我们希望允许在不同的模型类型中使用相同的提示。因此，我们有“ PromptValue ”的概念。这是一个类，公开了用于转换为每种模型类型所期望的确切输入类型（目前为文本或 ChatMessages ）的方法。 