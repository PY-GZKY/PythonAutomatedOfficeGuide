## markdown转换为其他格式的文件

### markdown2html

```python
import codecs
import os

try:
    from markdown import markdown
except ModuleNotFoundError as e:
    os.system("pip install markdown")
    os.system("pip install python-markdown-math")
    os.system("pip install markdown_checklist")
    from markdown import markdown

from src.constants import *
from src.source import imgkit
from src.source import pdfkit
from src.templates.html_template import html_
from src.utils.utils import md_extensions_, md_extensions_configs_


class MARKDOWN:
    def __init__(self,
                 wkhtmltopdf_path: str = None,
                 wkhtmltoimage_path: str = None,
                 encoding: str = 'utf-8'
                 ):
        self.encoding = encoding
        self.html_ = html_
        self.wkhtmltopdf_path = default_wkhtmltopdf_path if wkhtmltopdf_path is None else wkhtmltopdf_path
        self.wkhtmltoimage_path = default_wkhtmltoimage_path if wkhtmltoimage_path is None else wkhtmltoimage_path
        self.extensions = md_extensions_()
        self.extension_configs = md_extensions_configs_()

    def markdown2html(self, input_path: str, output_path: str, is_center: bool = True, is_save: bool = True):
        """
        """
        try:
            with codecs.open(input_path, "r", encoding="utf-8") as md_:
                md_text_ = md_.read()
        except Exception as e:
            print("<Error>", e)

        title = '.'.join(os.path.basename(input_path).split('.')[:-1])
        html_text_ = markdown(md_text_,
                              output_format='html',
                              extensions=self.extensions,
                              extension_configs=self.extension_configs
                              )

        class_ = ' for="html-export"' if is_center else ""
        html_text_ = self.html_.format(title_=title, static_dir=static_dir, div_=html_text_, class_=class_)

        if is_save:
            try:
                with codecs.open(output_path, 'w', encoding=self.encoding, errors="xmlcharrefreplace") as file_html_:
                    file_html_.write(html_text_)
                return output_path
            except Exception:
                return False
        else:
            return html_text_


if __name__ == '__main__':
    M = MARKDOWN()
    M.markdown2html(input_path=f'./_.md')
```