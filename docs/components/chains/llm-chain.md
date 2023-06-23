
# LLM链 LLMChain 

LLMChain（LLM链）是最常见的链类型。

它由 PromptTemplate（提示模板）、模型（可以是 LLM 或 ChatModel ）和可选的输出解析器组成。该链接受多个输入变量，使用 PromptTemplate 将它们格式化为提示。然后将提示传递给模型。最后，它使用 OutputParser（如果提供）将LLM的输出解析为最终格式。