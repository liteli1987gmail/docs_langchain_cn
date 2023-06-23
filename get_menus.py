import os

import re

def extract_file_paths(data):
    pattern = r'"@site/([^"]+)"'  # 匹配以"@site/"开头的文件路径
    matches = re.findall(pattern, data)  # 提取匹配的文件路径
    return matches

def write_to_txt(file_paths, output_file):
    with open(output_file, 'w') as file:
        for path in file_paths:
            file.write(path + '\n')

# 输入清单数据
data = '''
": [()=>n.e(3632).then(n.bind(n, 5287)), "@site/docs/components/models/chat-model.md", 5287],
            "0288536f": [()=>n.e(5033).then(n.bind(n, 3256)), "@site/docs/use-cases/personal-assistants.md", 3256],
            "04a51e6f": [()=>n.e(5442).then(n.bind(n, 5052)), "@site/docs/components/agents/agent-executor.md", 5052],
            "0f003c2b": [()=>n.e(1637).then(n.bind(n, 7980)), "@site/docs/components/chains/index_related_chains.md", 7980],
            "13044bf5": [()=>n.e(3246).then(n.bind(n, 1480)), "@site/docs/components/schema/text.md", 1480],
            "14eb3368": [()=>Promise.all([n.e(532), n.e(9817)]).then(n.bind(n, 5541)), "@theme/DocCategoryGeneratedIndexPage", 5541],
            17896441: [()=>Promise.all([n.e(532), n.e(7918)]).then(n.bind(n, 7617)), "@theme/DocItem", 7617],
            "1b58c3bb": [()=>Promise.all([n.e(532), n.e(6225)]).then(n.bind(n, 949)), "@site/docs/components/prompts/index.mdx", 949],
            "1bc774d2": [()=>n.e(4262).then(n.bind(n, 716)), "@site/docs/components/schema/examples.md", 716],
            "1be78505": [()=>Promise.all([n.e(532), n.e(9514)]).then(n.bind(n, 9963)), "@theme/DocPage", 9963],
            "1d4805c8": [()=>n.e(3681).then(n.bind(n, 8691)), "@site/docs/components/prompts/prompt-template.md", 8691],
            "20e0e154": [()=>Promise.all([n.e(532), n.e(9685)]).then(n.bind(n, 2797)), "@site/docs/components/chains/index.mdx", 2797],
            "243ab9da": [()=>n.e(1664).then(n.bind(n, 9922)), "@site/docs/components/prompts/output-parser.md", 9922],
            "243b4bc3": [()=>n.e(8112).then(n.bind(n, 4817)), "@site/docs/components/memory/chat_message_history.md", 4817],
            "24dcb8a0": [()=>n.e(5684).then(n.bind(n, 4285)), "@site/docs/use-cases/chatbots.md", 4285],
            37117196: [()=>n.e(8660).then(n.bind(n, 6068)), "@site/docs/components/agents/agent.md", 6068],
            "3b13a1f9": [()=>n.e(5778).then(n.bind(n, 1989)), "@site/docs/components/models/language-model.md", 1989],
            "3cded096": [()=>n.e(5623).then(n.bind(n, 5396)), "@site/docs/components/indexing/vectorstore.md", 5396],
            "4f0cfe70": [()=>n.e(8245).then(n.bind(n, 5965)), "@site/docs/components/indexing/text-splitters.md", 5965],
            "5357a4f1": [()=>n.e(2809).then(n.bind(n, 2900)), "@site/docs/use-cases/evaluation.md", 2900],
            "5843fc46": [()=>n.e(6405).then(n.bind(n, 6113)), "@site/docs/components/chains/chain.md", 6113],
            "5e9f5e1a": [()=>Promise.resolve().then(n.bind(n, 6809)), "@generated/docusaurus.config", 6809],
            "633b6434": [()=>Promise.all([n.e(532), n.e(202)]).then(n.bind(n, 5972)), "@site/docs/components/agents/index.mdx", 5972],
            "6357dfff": [()=>n.e(9362).then(n.bind(n, 4343)), "@site/docs/components/models/text-embedding-model.md", 4343],
            "6d5c8854": [()=>Promise.all([n.e(532), n.e(8739)]).then(n.bind(n, 6433)), "@site/docs/components/memory/index.mdx", 6433],
            "73983ada": [()=>n.e(9960).then(n.bind(n, 1029)), "@site/docs/components/prompts/prompt-value.md", 1029],
            "831eabda": [()=>Promise.all([n.e(532), n.e(2829)]).then(n.bind(n, 9615)), "@site/docs/components/models/index.mdx", 9615],
            "869217d6": [()=>Promise.all([n.e(532), n.e(5988)]).then(n.bind(n, 4321)), "@site/docs/components/schema/index.mdx", 4321],
            "86d80368": [()=>n.e(5545).then(n.bind(n, 9260)), "@site/docs/components/indexing/document-loaders.md", 9260],
            "87a42372": [()=>n.e(8221).then(n.bind(n, 8515)), "@site/docs/components/schema/chat-messages.md", 8515],
            "8bb0b68c": [()=>n.e(8499).then(n.bind(n, 7e3)), "@site/docs/components/chains/prompt-selector.md", 7e3],
            "935f2afb": [()=>n.e(53).then(n.t.bind(n, 1109, 19)), "~docs/default/version-current-metadata-prop-751.json", 1109],
            "9629a648": [()=>n.e(2830).then(n.t.bind(n, 3769, 19)), "/vercel/path0/src/.docusaurus/docusaurus-plugin-content-docs/default/plugin-route-context-module-100.json", 3769],
            "97919cd9": [()=>n.e(544).then(n.bind(n, 6193)), "@site/docs/components/prompts/example-selectors.md", 6193],
            "993feaa2": [()=>n.e(8633).then(n.bind(n, 1350)), "@site/docs/use-cases/qa-docs.md", 1350],
            a976dd89: [()=>n.e(9695).then(n.bind(n, 6647)), "@site/docs/components/agents/tool.md", 6647],
            acabc2a3: [()=>n.e(3367).then(n.bind(n, 2805)), "@site/docs/components/schema/document.md", 2805],
            b22fe832: [()=>n.e(9125).then(n.bind(n, 7426)), "@site/docs/use-cases/summarization.md", 7426],
            c377a04b: [()=>n.e(6971).then(n.bind(n, 1269)), "@site/docs/index.md", 1269],
            c4f5d8e4: [()=>n.e(4195).then(n.bind(n, 2841)), "@site/src/pages/index.js", 2841],
            ca9e2a97: [()=>n.e(1834).then(n.bind(n, 8738)), "@site/docs/use-cases/extraction.md", 8738],
            cd1627fb: [()=>n.e(1829).then(n.t.bind(n, 5745, 19)), "/vercel/path0/src/.docusaurus/docusaurus-plugin-content-pages/default/plugin-route-context-module-100.json", 5745],
            cea17e9b: [()=>Promise.all([n.e(532), n.e(3570)]).then(n.bind(n, 416)), "@site/docs/components/indexing/index.mdx", 416],
            ec183bea: [()=>n.e(1235).then(n.t.bind(n, 4570, 19)), "~docs/default/category-docs-sidebar-category-components-c01.json", 4570],
            ed526170: [()=>n.e(5607).then(n.bind(n, 2095)), "@site/docs/use-cases/qa-tabular.md", 2095],
            ed830b67: [()=>n.e(5961).then(n.bind(n, 5816)), "@site/docs/components/indexing/retriever.md", 5816],
            eecccaa4: [()=>n.e(8090).then(n.bind(n, 5046)), "@site/docs/components/chains/llm-chain.md", 5046],
            f79a773f: [()=>n.e(107).then(n.t.bind(n, 7642, 19)), "~docs/default/category-docs-sidebar-category-use-cases-689.json", 7642],
            f7e92e65: [()=>n.e(6800).then(n.bind(n, 1130)), "@site/docs/use-cases/apis.md", 1130],
            f8d2d437: [()=>n.e(9902).then(n.bind(n, 97)), "@site/docs/components/agents/toolkit.md", 97]
            '''

# 提取文件路径
file_paths = extract_file_paths(data)

# 写入txt文件
output_file = 'file_paths.txt'
write_to_txt(file_paths, output_file)


def create_files_from_txt(txt_file):
    with open(txt_file, 'r') as file:
        for line in file:
            file_path = line.strip()
            directory = os.path.dirname(file_path)
            os.makedirs(directory, exist_ok=True)  # 创建文件夹，如果文件夹已存在则忽略
            open(file_path, 'w').close()  # 创建文件

# 调用函数
txt_file_path = 'file_paths.txt'  # 替换为你的txt文件路径
create_files_from_txt(txt_file_path)
