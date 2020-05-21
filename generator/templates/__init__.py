from jinja2 import Template, Environment, PackageLoader, select_autoescape, FileSystemLoader
from utils.common import get_config
import os

env = Environment(
    loader=FileSystemLoader(get_config()['templates_path']),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True,
)
env.globals['MEDIA_PREFIX'] = '/media/'


def generate_template(template_name, html_ext=True):
    return env.get_template(f'{template_name}{".html" if html_ext else ""}')

def custom_render_template(template: Template, *args, **kwargs):
    return template.render(*args, **kwargs)

def write_rendered_template_to_file(template: Template, filename: str, file_path = '', *args, **kwargs):
    file_dir = os.path.join(get_config()['content_path'], file_path, f'{filename}.html')
    if not os.path.exists(os.path.dirname(file_dir)):
        os.makedirs(os.path.dirname(file_dir))
    with open(file_dir, mode='w') as f:
        f.write(custom_render_template(template, *args, **kwargs))