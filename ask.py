import sys
import gemini
import log
import util
import PIL.Image
import requests
import io
import os
import wget


class Asker:

  def __init__(self) -> None:
    self.hub = gemini.GitGeminiHub()


  def ask(self):
    self.hub = gemini.GitGeminiHub()
    args = self.hub.parse_inputs()
    # print(args)
    self.hub.init(args)

    fout_path = util.response_path
    if (self.hub.output):
      fout_path = self.hub.output

    with open(fout_path, 'w+', encoding='utf-8') as fout:
      logger = log.Logger(fout)

      if len(self.hub.prompt) <= 0:
        ret = logger.log_error("Prompt is empty, please fill the prompt.")
        raise Exception(ret)

      if self.hub.task == 'text':
        input = self.hub.prompt
        urls = util.extract_urls(self.hub.content)
        if len(urls) > 0:

          base_name = os.path.basename(urls[0])
          input_file_path = os.path.join("cabin/", base_name)
          wget.download(urls[0], input_file_path)

          max_lines_count = 20
          with open(input_file_path, 'r+', encoding='utf-8') as fin:
            lines = fin.readlines()
            if len(lines) > max_lines_count:
              ret = logger.log_warning("Please limit the text file less than 20 lines.")
              # raise Exception(ret)

            line_count = 0
            input += "\n"
            for line in lines:
              if (len(line.strip()) <= 0):
                continue

              if line_count > max_lines_count:
                ret = logger.log_warning("Please limit the text file less than 20 lines.")
                break

              input += line
              line_count += 1

        self.hub.generate(input, fout)

      elif self.hub.task == 'image':
        input = [self.hub.prompt]
        img_urls = util.extract_urls(self.hub.content)
        for url in img_urls:
          img_response = requests.get(url)
          img_content = io.BytesIO(img_response.content)
          img_data = PIL.Image.open(img_content)
          input.append(img_data)

        self.hub.generate(input, fout)
      else:
        self.hub.generate(self.hub.prompt, fout)


if __name__ == '__main__':
    # print(sys.argv)
    asker = Asker()
    asker.ask()