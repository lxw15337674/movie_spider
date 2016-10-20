import HTMLParser
html_cont = " asdfg>123<"
html_parser = HTMLParser.HTMLParser()
new_cont = html_parser.unescape(html_cont)
print(new_cont)