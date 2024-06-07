---
name: Task - Ask with images
about: Create an ask images request task
title: ''
labels: ['ask', 'image', 'task']
assignees: ''

---
<!-- Please just fill the below task information as follows and DO NOT remove any text of this Description template -->

### Let's read images

See **Introduction** for details.

### Prompt

-------------------------------------------------------------------------------



-------------------------------------------------------------------------------

### Content

-------------------------------------------------------------------------------



-------------------------------------------------------------------------------

### Introduction

- It is a read images task which can read images and response according to the prompt and images ...
- The response will be posted to the comment under this issue ticket.
- See more prompt introductions [Prompt strategies](https://ai.google.dev/docs/prompt_best_practices#experiment-with-different-parameter-values), [Multimodal prompts](https://ai.google.dev/docs/multimodal_concepts) and [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)
- ***Fill the prompt /content between the line marks "---" in each "###" sections***
- Prompt:
  - Examples:
    - What's in the picture?
    - Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.
    - ...
- Content:
  - Attach an image or multiples images list
  - Paste, drop or click to add images between line marks "---"

<!--
### Setting

Here is the generation configuration and safety setting about Gemini, you can modify them according to your needs. [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)

-------------------------------------------------------------------------------
	{
	  "model_name": "gemini-pro-vision",
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