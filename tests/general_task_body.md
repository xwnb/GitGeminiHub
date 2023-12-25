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

### Ask anything you want

- It is a general ask task request, you can ask for any questions/requests/help ...
- The response will be posted to the comment under this issue ticket.
- See more about [Prompt strategies](https://ai.google.dev/docs/prompt_best_practices#experiment-with-different-parameter-values) and [Safety settings](https://ai.google.dev/docs/safety_setting_gemini)

### Prompt

	- Fill the prompt between the separate lines "---" in the below **### Prompt** section
	- More: [Introduction to prompt design](https://ai.google.dev/docs/prompt_intro)

    Examples:
    - Please summary the text: ..balabala.. .
    - Please polish the text: ..balabala.. .
    - Please translate the text: ..balabala.. .
    - Tell a story about ...balabala... to me.
    - ...
-------------------------------------------------------------------------------

Please translate the text to Chinese

-------------------------------------------------------------------------------

### Content

    - Attach a file as extra context
    - Paste, drop or click the button at the bottom of the Description to add file, or paste the download link of the file between the separate lines "---"
    - **File name and link should better be composed of numbers or English characters**
    - Support text formats: *.txt, *.md (more formats support are working in progress)

-------------------------------------------------------------------------------

[hello_world.txt](https://raw.githubusercontent.com/xwnb/GitGeminiHub/main/samples/hello_world.txt)

-------------------------------------------------------------------------------