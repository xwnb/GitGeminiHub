import sys
import gemini
import log
import util
class Asker:

  def __init__(self) -> None:
    self.hub = gemini.GitGeminiHub()

  def __ask_to_file(self):

    fout_path = util.response_path
    if (self.hub.output):
       fout_path = self.hub.output

    with open(fout_path, 'w+', encoding='utf-8') as fout:
      logger = log.FileLogger(fout)

      if len(self.hub.prompt) <= 0:
        ret = logger.log_error("Prompt is empty, please fill the prompt.")
        raise Exception(ret)

      # if len(self.hub.content) <= 0:
      #   ret = logger.log_error("Content is empty, please fill the Content.")
      #   raise Exception(ret)
      input = self.hub.prompt
      if self.hub.content:
        input += ": " + self.hub.content

      self.hub.generate(input, fout)

  def __ask_to_screen(self):
    logger = log.ScreenLogger()

    if len(self.hub.prompt) <= 0:
      ret = logger.log_error("Prompt is empty, please fill the prompt.")
      raise Exception(ret)

    # if len(self.hub.content) <= 0:
    #   ret = logger.log_error("Content is empty, please fill the Content.")
    #   raise Exception(ret)


    input = self.hub.prompt
    if self.hub.content:
      input += ": " + self.hub.content

    self.hub.generate(input)

  def ask(self):
    self.hub = gemini.GitGeminiHub()
    args = self.hub.parse_inputs()
    # print(args)
    self.hub.init(args)

    if not self.hub.output:
      self.__ask_to_screen()
    else:
      self.__ask_to_file()

if __name__ == '__main__':
    # print(sys.argv)
    asker = Asker()
    asker.ask()