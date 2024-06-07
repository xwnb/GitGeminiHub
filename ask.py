import sys
import gemini
import log
import util
import PIL.Image
import requests
import io
import os
import wget
import fitz
import time


class Asker:

  def __init__(self) -> None:
    self.hub = gemini.GitGeminiHub()


  def ask(self):
    # self.hub = gemini.GitGeminiHub()
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
      elif self.hub.task == 'pdf':
        input = self.hub.prompt
        urls = util.extract_urls(self.hub.content)

        if len(urls) > 0:
          base_name = os.path.basename(urls[0])
          input_file_path = os.path.join("cabin/", base_name)
          wget.download(urls[0], input_file_path)

          max_pages = 5
          max_batch_pages = 1
          with fitz.open(input_file_path) as fin:
            if len(fin) > max_pages:
              ret = logger.log_warning(f"Please limit pdf pages within {max_pages}.\n\n")
              # raise Exception(ret)

            # total_tokens_count = 0
            page_count = 0
            for page_num in range(len(fin)):
              if page_count == 0:
                input = [self.hub.prompt]

              page = fin.load_page(page_num)
              pix = page.get_pixmap()
              image_data = pix.tobytes()
              image = PIL.Image.open(io.BytesIO(image_data))
              input.append(image)
              page_count += 1

              if page_count < max_batch_pages:
                  continue
              elif page_num > max_pages:
                  break

              page_count = 0
              logger.log_msg(f"\n\n#Page: {page_num}\n\n")

              self.hub.generate(input, fout)
              time.sleep(1)
      else:
        self.hub.generate(self.hub.prompt, fout)


if __name__ == '__main__':
    # print(sys.argv)
    asker = Asker()
    asker.ask()