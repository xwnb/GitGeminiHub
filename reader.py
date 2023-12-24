import gemini
import log
import recorder
import io
import PIL.Image
import requests
import util

class Reader:

  def __init__(self) -> None:
    self.hub = gemini.GitGeminiHub("gemini-pro-vision")

  def __make_input(self, fout: io.FileIO = None):
    logger = log.FileLogger(fout)

    if len(self.hub.prompt) <= 0:
      ret = logger.log_error("Prompt is empty, please fill the prompt.")
      raise Exception(ret)

    if len(self.hub.content) <= 0:
      ret = logger.log_error("Please provide available image file(s) or url(s).")
      raise Exception(ret)

    input = [self.hub.prompt]
    img_urls = util.extract_urls(self.hub.content)
    for url in img_urls:
      img_response = requests.get(url)
      img_content = io.BytesIO(img_response.content)
      img_data = PIL.Image.open(img_content)
      input.append(img_data)

    return input


  def __generate_to_file(self):

    fout_path = recorder.path
    if (self.hub.output):
       fout_path = self.hub.output

    with open(fout_path, 'w+', encoding='utf-8') as fout:
      input = self.__make_input(fout)
      self.hub.generate(input, fout)

  def __generate_to_screen(self):
    input = self.__make_input()
    self.hub.generate(input)


  def read(self):
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
    reader.read()