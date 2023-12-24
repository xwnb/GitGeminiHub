---
name: Task - Translate file
about: Create a translate request task
title: ''
labels: ['translate', 'task']
assignees: ''

---
<!-- Please fill the below task information as follows -->
<!-- Do not remove any text of this Description template, just fill items -->

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

### Let's translate files

- It is a translate file task which can translate the text or files to another language you'd like ...
- If you want to translate pure text, you can use the ask task simply
- The translated files will be posted to the comment under this issue ticket.
- See more about [Prompt strategies](https://ai.google.dev/docs/prompt_best_practices#experiment-with-different-parameter-values) and [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)
- ***Fill the prompt /content between the line marks "---" below each "###” sections***

### Prompt

- Fill a translation prompt you like.
- Example:

> - Please help translate the text to English/(Simplified Chinese/Traditional Chinese/Japanese/中文/英文/繁體中文/日文, and etc.)
**(If you want to translate pure, please use ask request for easy use.)**:
> - Please translate the text to Chinese/English more elegent/beautiful/authentic, and etc,.
-------------------------------------------------------------------------------



-------------------------------------------------------------------------------

### Content

- Upload one file to translate.
- Paste, drop or click the button at the bottom of the Description to add file or paste the available download link between the separate lines "---"
- **File name and link should better be composed of numbers or English characters**
- Support text formats: *.txt, *.md （more formats support are working in progress）
- Example:

> - [the_moon_and_sixpence_chapter_1.txt](https://raw.githubusercontent.com/xwnb/GitAutoTranslator/main/samples/the_moon_and_sixpence_chapter_1.txt)
> - https://raw.githubusercontent.com/xwnb/GitAutoTranslator/main/samples/hello_world.txt

-------------------------------------------------------------------------------



-------------------------------------------------------------------------------