# 索引链 Index-related chains

这类链用于与索引进行交互。这些链的目的是将自己的数据（存储在索引中）与LLM结合起来。其中最好的例子是对自己的文档进行问答。

其中一个重要部分是了解如何将多个文档传递给语言模型。有几种不同的方法或链来实现这一点。

LangChain 支持其中四种常见的方法，并且我们正在积极寻求包括更多方法，如果你有任何想法，请随时联系我们！请注意，并没有一种最佳方法-选择使用哪种方法通常非常依赖上下文。按照从简单到复杂的顺序：

## Stuffing（填充）
Stuffing 是最简单的方法，您只需将所有相关数据作为上下文直接添加到提示中，然后传递给语言模型。LangChain 中的 StuffDocumentsChain 便是采用了这种方法。

** 优点： ** 只需向LLM发出一次调用。在生成文本时，LLM 可以一次性访问所有数据。

** 缺点： ** 大多数LLM具有上下文长度限制，对于大型文档（或许多文档），这种方法将不起作用，因为提示的长度将超过上下文长度。

这种方法的主要缺点是它只适用于较小的数据片段。一旦您处理许多数据片段，这种方法就不再可行。接下来的两种方法旨在帮助处理这个问题。

##  Map Reduce（映射-归约）
该方法涉及对每个数据块运行初始提示（对于摘要任务，可以是该块的摘要；对于问答任务，可以是仅基于该块的答案）。然后运行不同的提示来组合所有初始输出。LangChain中实现了这种方法，称为 MapReduceDocumentsChain。

** 优点： ** 可以扩展到比 StuffDocumentsChain 更大的文档（以及更多的文档）。对各个文档进行的LLM调用是独立的，因此可以并行化处理。

** 缺点： ** 比 StuffDocumentsChain 需要更多对 LLM 的调用。在最终的组合调用中会丢失一些信息。

## Refine（优化）
该方法涉及在第一个数据块上运行初始提示，生成一些输出。对于剩余的文档，将该输出与下一个文档一起传递给LLM，要求LLM基于新文档优化输出。

** 优点： ** 可以获取更多相关的上下文，并且可能比 MapReduceDocumentsChain 更少损失信息。

** 缺点： ** 比 StuffDocumentsChain 需要更多对LLM的调用。这些调用也不是独立的，这意味着无法像  MapReduceDocumentsChain 那样进行并行化处理。还可能对文档的顺序造成潜在的影响。


## Map-Rerank（映射-重新排序）

这种方法涉及在每个数据块上运行初始提示，该提示不仅尝试完成任务，还为其答案的确定程度给出一个分数。然后根据这个分数对响应进行排序，返回最高分的响应。

** 优点： ** 与MapReduceDocumentsChain类似的优点。与MapReduceDocumentsChain相比，需要更少的调用。

** 缺点： ** 无法在文档之间合并信息。这意味着当您期望在单个文档中有一个简单的单一答案时，这种方法最为有用。