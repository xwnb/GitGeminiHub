import google.generativeai as genai
from pathlib import Path
import gemini
import log
import recorder
import io
import wget
import util
import os
# import nltk



class Reader:

  def __init__(self) -> None:
    self.hub = gemini.GitGeminiHub("gemini-pro")

  def __translate(self, fout: io.FileIO = None):
    logger = log.FileLogger(fout)

    if len(self.hub.prompt) <= 0:
      ret = logger.log_error("Prompt is empty, please fill the prompt.")
      raise Exception(ret)

    if len(self.hub.content) <= 0:
      ret = logger.log_error("Please provide available text file(s) or url(s).")
      raise Exception(ret)
      # return self.hub.generate(self.hub.prompt, fout)

    else:
      # input = [self.hub.prompt]
      urls = util.extract_urls(self.hub.content)
      if len(urls) < 0:
        ret = logger.log_warning("Please provide available text file(s) or url(s).")

      base_name = os.path.basename(urls[0])
      input_file_path = os.path.join("cabin/", base_name)
      wget.download(urls[0], input_file_path)

      output_file_path = "cabin/Translated - " + base_name

      with open(input_file_path, 'r+', encoding='utf-8') as fin_original:
        with open(output_file_path, 'w+', encoding='utf-8') as fout_translated:
          translated_logger = log.FileLogger(fout_translated)
          has_error = False
          lines = fin_original.readlines()
          for line in lines:
              if (len(line.strip()) <= 0):
                continue

              try:
                input = self.hub.prompt + "\n" + line
                response = self.hub.generate_raw(input, fout)
                response_text = response.text + "\n"
                translated_logger.log_raw(response_text)
              except Exception as ex:
                has_error = True
                error_count = error_count + 1
                msg = logger.log_error(ex)
                translated_logger.log_raw(msg)

          complete_info = "Translate task completed!\n"
          if has_error:
            complete_info += "Number of translation sections failures: " + str(error_count)
          else:
            complete_info += "Successfully! The translated file is: " + os.path.basename(output_file_path)

          msg = logger.log_info(complete_info)
          fout_translated.write(msg)

    return None


  def __generate_to_file(self):

    fout_path = recorder.path
    if (self.hub.output):
       fout_path = self.hub.output

    with open(fout_path, 'w+', encoding='utf-8') as fout:
      self.__translate(fout)


  def __generate_to_screen(self):
    self.__translate()


  def execute(self):
    self.hub = gemini.GitGeminiHub()
    args = self.hub.parse_inputs()
    # print(args)
    self.hub.init(args)

    if not self.hub.output:
      self.__generate_to_screen()
    else:
      self.__generate_to_file()

if __name__ == '__main__':
    # print(sys.argv)
    reader = Reader()
    reader.execute()