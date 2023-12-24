---
name: 0 Read Images task
about: Create a read images request to start a task
title: ''
labels: ['read', 'image', 'task']
assignees: ''

---
<!-- Please fill the below task information as follows -->
<!-- Do not remove any text of this Description template, just fill items -->

<!--
### Setting

Here is the generation configuration and safety setting about Gemini, you can modify them according to your needs.
- [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)

---
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
---
-->

### Let's read images

- It is a read images task which can read images and response according to the prompt and images ...
- The response will be posted to the comment under this issue ticket.
- See more about [Prompt strategies](https://ai.google.dev/docs/prompt_best_practices#experiment-with-different-parameter-values) and [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)
- ***Fill the prompt /content between the line marks "---" below each "###” sections***

### Prompt

	- More: [Introduction to prompt design](https://ai.google.dev/docs/prompt_intro)

    Examples:
    - What's in the picture?
    - Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.
    - ...
---

What's in the picture?

---

### Content

    - Attach an image or multiples images list
    - Paste, drop or click to add images between line marks "---"

---

[scones.jpg](https://storage.googleapis.com/generativeai-downloads/images/scones.jpg)

---