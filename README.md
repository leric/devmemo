# DevMemo

[![PyPI - Version](https://img.shields.io/pypi/v/devmemo.svg)](https://pypi.org/project/devmemo)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/devmemo.svg)](https://pypi.org/project/devmemo)

-----

## Overview

AI programming has two approaches:

1. Writing a script to solve a problem, such as a script to write a snake, analyze an Excel file.
2. Software engineering tasks in large projects, such as fixing bugs in a project that has been developed for 3 years.

The complexity of the latter is order of magnitude larger than the former. In software projects, the complexity is a variable that increases with time. Every technical decision made, every change in requirements, every piece of data in the database, contributes to the complexity of a new development task. Many projects like Devin, Aider, SWE-Agent tries to solve this problem, but the performance is still far from useful.

Driven by Scaling Law, LLMs are becoming more and more smart, but LLMs are fundamentally stateless, so providing complete and clear context information to LLMs would be the key to make AI programmer doing good work.

From the perspective of information, software projects have a large portion of information that is not in the source code repository, not in the documentation and issue tracker, even forgotten by the people who wrote the code. But when the code is written, all the relevant context information is loaded into the developer's brain, if you want to record down this code's relevant information, this is the best time.

All the information about a software project could be described in 3 forms:

- Implementation: Implementation details, or just the code itself.
- Responsibility: High level, layered seperation of concerns of the system, form a tree of responsibilities.
- Intent: Intent of code changes, describe the history of how the code base evolves.

The source code repository is mainly about the implementation, if the code run, its self-proven. But the other two part of information is not so well maintained. A good project should have responsibilities described in documents and comments, and the intent is tracked in the vcs comments, but the quality of these record is rarely good enough. We are too lazy to write these things down, but now we have AI.

## Proposed Solution

This project is a tool to help programmers to record important information about a software project, for further reference by AI, or by human.

AI agents are used to summarize code changes before committing: summarize commit comment, add missing comments(describing responsibility of class and function), update outdated comments, summarize the intent of code changes(for every changed function).

A data retrieval api can be used to retrieve the information of history code changes, for AI programmer to better understand the code base.


## How to use

```console
pip install devmemo
```



## License

`devmemo` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
