---
name: Task - Ask
about: Create an simple ask request task
title: ''
labels: ['ask', 'task']
assignees: ''

---
<!-- Please just fill the below task information as follows and DO NOT remove any text of this Description template -->
### Ask anything you want

See **Introduction** for details.

### Prompt

-------------------------------------------------------------------------------



-------------------------------------------------------------------------------

### Introduction

- It is a general ask task request, you can ask for any questions/requests/help ...
- The response will be posted to the comment under this issue ticket.
- See more prompt introductions [Prompt strategies](https://ai.google.dev/docs/prompt_best_practices#experiment-with-different-parameter-values), [Multimodal prompts](https://ai.google.dev/docs/multimodal_concepts) and [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)
- ***Fill the prompt /content between the line marks "---" in each "###" sections***
- Prompt:
  - Examples:
    - Please summary the text: ..balabala.. .
    - Please polish the text: ..balabala.. .
    - Please translate the text: ..balabala.. .
    - Tell a story about ...balabala... to me.
    - ...

<!--
### Setting

Here is the generation configuration and safety setting about Gemini, you can modify them according to your needs.
- [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)

-------------------------------------------------------------------------------
	{
	  "model_name": "gemini-pro",
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