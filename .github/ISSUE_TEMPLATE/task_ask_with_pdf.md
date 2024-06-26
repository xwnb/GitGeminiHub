---
name: Task - Ask with PDF file
about:  Create an ask request task with a PDF file
title: ''
labels: ['ask', 'pdf', 'task']
assignees: ''

---
<!-- Please just fill the below task information as follows and DO NOT remove any text of this Description template -->

### Let's read PDF file

See **Introduction** for details.

### Prompt

-------------------------------------------------------------------------------



-------------------------------------------------------------------------------

### Content

-------------------------------------------------------------------------------



-------------------------------------------------------------------------------

### Introduction

- It is an ask task which can read a pdf file as part of content, you can ask for any translation/questions/requests/help ...
- !!! This ticket only supports read pdf file page by page. It has not supported summary the whole file
- The response will be posted to the comment under this issue ticket.
- See more prompt introductions [Prompt strategies](https://ai.google.dev/docs/prompt_best_practices#experiment-with-different-parameter-values), [Multimodal prompts](https://ai.google.dev/docs/multimodal_concepts) and [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)
- ***Fill the prompt /content between the line marks "---" in each "###" sections***
- Prompt:
  - Fill the prompt between the separate lines "---" in the below **### Prompt** section
  - Examples:
    - ~~Please summary the text: ..balabala..~~ .
    - Please polish the text: ..balabala.. .
    - Please translate the text: ..balabala.. .
    - ...
- Content:
  - **Attach a file as extra content**
  - Paste, drop or click the button at the bottom of the Description to upload file or paste the available download link between the separate lines "---"
  - **File name and link should better be composed of numbers or English characters**
  - **If you want to ask with pure text, please use [Task - Ask](https://github.com/xwnb/GitGeminiHub/issues/new?assignees=&labels=ask%2Ctask&projects=&template=task_simple_ask.md&title=) and paste your text**:

<!--
### Setting

Here is the generation configuration and safety setting about Gemini, you can modify them according to your needs. [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)

-------------------------------------------------------------------------------
	{
	  "model_name": "gemini-1.5-pro-latest",
	  "generation_configuration":
	  {
	    "temperature": 0.9,
	    "top_p": 1.0,
	    "top_k": 1,
	    "max_output_tokens": 2048
	  },
	  "safety_setting":
	  {
	    "harassment": "BLOCK_MEDIUM_AND_ABOVE",
	    "hate_speech": "BLOCK_MEDIUM_AND_ABOVE",
	    "sexually_explicit": "BLOCK_MEDIUM_AND_ABOVE",
	    "dangerous_content": "BLOCK_MEDIUM_AND_ABOVE"
	  }
	}
-------------------------------------------------------------------------------
-->
