import google.generativeai as genai
import argparse
import log
import io

class GenerationConfig:
    def __init__(self) -> None:
        self.temperature = 0.9
        self.top_p = 1
        self.top_k = 1
        self.max_output_tokens = 2048

    def __str__(self) -> str:
        return str(self.__class__) + ":\n" + str(self.__dict__)


class SafetySettings:
    def __init__(self) -> None:
        self.harassment = "HARM_BLOCK_THRESHOLD_UNSPECIFIED"
        self.hate_speech = "HARM_BLOCK_THRESHOLD_UNSPECIFIED"
        self.sexually_explicit = "HARM_BLOCK_THRESHOLD_UNSPECIFIED"
        self.dangerous_content = "HARM_BLOCK_THRESHOLD_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.__class__) + ":\n" + str(self.__dict__)

class GitGeminiHub:
    def __init__(self, model_name: str = 'gemini-pro') -> None:
        self.model_name : str = model_name
        self.prompt : str = ""
        self.content : str = ""
        self.date = None
        self.model = None
        self.output : str = ""
        self.generation_config = GenerationConfig()
        self.safety_settings = SafetySettings()

    def __str__(self) -> str:
        return str(self.__class__) + ":\n" + str(self.__dict__)

    @staticmethod
    def parse_inputs():
        parser = argparse.ArgumentParser(prog='GitGeminiHub')
        parser.add_argument('model_name', default='gemini-pro', help="Specificy model name, which could be gemini-pro or gemini-pro-version")
        parser.add_argument('api_key', help="The api key of Gemini")
        parser.add_argument('prompt', help="The prompt")
        parser.add_argument('-c', '--content', default='', type=str, help="The additional content (text, file, image, and etc) for the prompt")
        parser.add_argument('-o', '--output', default='', type=str, help="The output file path for response text if set")

        parser.add_argument('-t', '--temperature', default=0.9, type=float, help="Generation congiguration - Creativity allowed in the responses.")
        parser.add_argument('-p', '--top_p', default=1, type=float, help="Generation congiguration - Probability threshold for top-p sampling.")
        parser.add_argument('-k', '--top_k', default=1, type=int, help="Generation congiguration - Number of top-scored tokens to consider during generation.")
        parser.add_argument('-m', '--max_output_tokens', default=2048, type=int, help="generation congiguration - Maximum number of tokens in response.")

        parser.add_argument('-hs', '--harassment', default="HARM_BLOCK_THRESHOLD_UNSPECIFIED", type=str, help="Satety setting - Negative or harmful comments targeting identity and/or protected attributes.")
        parser.add_argument('-ht', '--hate_speech', default="HARM_BLOCK_THRESHOLD_UNSPECIFIED", type=str, help="Satety setting - Content that is rude, disrespectful, or profane.")
        parser.add_argument('-sx', '--sexually_explicit', default="HARM_BLOCK_THRESHOLD_UNSPECIFIED", type=str, help="Satety setting - Contains references to sexual acts or other lewd content.")
        parser.add_argument('-dg', '--dangerous_content', default="HARM_BLOCK_THRESHOLD_UNSPECIFIED", type=str, help="Satety setting -	Promotes, facilitates, or encourages harmful acts.")

        # Block none	BLOCK_NONE	Always show regardless of probability of unsafe content
        # Block few	    BLOCK_ONLY_HIGH	Block when high probability of unsafe content
        # Block some	BLOCK_MEDIUM_AND_ABOVE	Block when medium or high probability of unsafe content
        # Block most	BLOCK_LOW_AND_ABOVE	Block when low, medium or high probability of unsafe content
        # HARM_BLOCK_THRESHOLD_UNSPECIFIED	Threshold is unspecified, block using default threshold

        return parser.parse_args()


    def __create_model(self, model_name: str, api_key: str, generation_config_in: GenerationConfig, safety_settings_in: SafetySettings) -> genai.GenerativeModel:

        generation_config = {
            "temperature": generation_config_in.temperature,
            "top_p": generation_config_in.top_p,
            "top_k": generation_config_in.top_k,
            "max_output_tokens": generation_config_in.max_output_tokens,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": safety_settings_in.harassment
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": safety_settings_in.hate_speech
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": safety_settings_in.sexually_explicit
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": safety_settings_in.dangerous_content
            }
        ]

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config, safety_settings=safety_settings)

        return model


    def init(self, args: argparse.Namespace):
        self.model_name = args.model_name

        self.api_key = args.api_key
        self.prompt = args.prompt
        self.content = args.content
        self.output = args.output

        self.generation_config.temperature = args.temperature
        self.generation_config.top_p = args.top_p
        self.generation_config.top_k = args.top_k
        self.generation_config.max_output_tokens = args.max_output_tokens

        # print(self.generation_config)

        self.safety_settings.harassment = args.harassment
        self.safety_settings.hate_speech = args.hate_speech
        self.safety_settings.sexually_explicit = args.sexually_explicit
        self.safety_settings.dangerous_content = args.dangerous_content

        # print(self.safety_settings)

        self.model = self.__create_model(self.model_name, self.api_key, self.generation_config, self.safety_settings)


    def __generate_to_screen(self, input: str) -> None:
        logger = log.ScreenLogger()
        if len(input) <= 0:
            ret = logger.log_error("The input should not be empty. Please input something")
            raise Exception(ret)

        response = self.model.generate_content(input)
        try:
            logger.log_msg(response.text)
        except Exception as ex:
            ret = logger.log_error(ex)
            ret += logger.log_error(response.prompt_feedback)
            raise Exception(ex)

        return response

    def __generate_to_file(self, input: str, fout: io.FileIO) -> None:
        logger = log.FileLogger(fout)
        if len(input) <= 0:
            ret = logger.log_error("The input text to GitGeminHub should not be empty. Please input something")
            raise Exception(ret)

        response = self.model.generate_content(input)
        try:
            logger.log_msg(response.text, fout)
        except Exception as ex:
            ret = logger.log_error(ex, fout)
            ret += logger.log_error(response.prompt_feedback, fout)
            raise Exception(ex)

        return response


    def generate(self, input: str, fout: io.FileIO = None) -> None:
        if not fout:
            return self.__generate_to_screen(input)
        else:
            return self.__generate_to_file(input, fout)


    def generate_raw(self, input: str, fout: io.FileIO = None) -> None:
        return self.model.generate_content(input)

if __name__ == '__main__':
    print("gemini.py")
    args = GitGeminiHub.parse_inputs()
    gm = GitGeminiHub()
    gm.init(args)
    gm.generate("Say something to me.")