/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @format
 */

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

 module.exports = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  sidebar: [
    "index",
    {
      type: "category",
      label: "介绍 （ Introduction ）",
      collapsed: false,
      collapsible: false,
      items: [{ type: "autogenerated", dirName: "introduction" }],
    },
    {
      type: "category",
      label: "模块（ Components ）",
      collapsed: false,
      collapsible: false,
      description: "在本节中，我们首先介绍一些底层模式抽象，然后再深入探讨 LangChain 的六个主要组件。",
      items: [{ type: "autogenerated", dirName: "components" }],
      link: {
        type: 'generated-index',
	      slug: "components",
      },
    },
    {
      type: "category",
      label: "用例（ Use Cases  ）",
      collapsed: false,
      collapsible: false,
      items: [{ type: "autogenerated", dirName: "use-cases" }],
    },
    {
      type: "html",
      value: '<img src="https://www.aiqbh.com/qun.png" alt="扫我，入群" width="280" height="330"/>'
    }
  ],
};
