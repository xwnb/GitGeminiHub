import re

response_path: str = "cabin/response.txt"

def extract_urls(text):
    result = []
    url_regex = r"(https?|http|ftp|file):\/\/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"
    matches = re.finditer(url_regex, text, re.MULTILINE)
    for match in matches:
        result.append(match.group())

    return result


if __name__ == '__main__':
    pass
