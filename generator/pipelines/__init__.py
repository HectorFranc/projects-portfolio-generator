from utils.common import get_config
from templates import generate_template, write_rendered_template_to_file
import shutil
import os

def global_pipeline():
    projects_pipeline()
    static_pipeline()
    home_pipeline()
    media_pipeline()

def projects_pipeline():
    project_template = generate_template('project')
    for project in get_config()['projects']:
        write_rendered_template_to_file(
            template=project_template,
            filename=project['slug'],
            file_path='proyecto',
            **project
        )

def home_pipeline():
    home_template = generate_template('home')
    write_rendered_template_to_file(
        home_template, 
        filename='index',
        projects_list=get_config()['projects'],
        **get_config()['home']
    )

def static_pipeline():
    for static_site in get_config()['static_sites']:
        static_file_dir = f'static/{static_site["filename_with_ext"]}'
        static_template = generate_template(static_file_dir, html_ext=False)
        write_rendered_template_to_file(
            template=static_template,
            filename=static_site['slug'],
            **static_site
        )


def media_pipeline():
    dst_path = os.path.join(get_config()['content_path'], 'media')
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)

    shutil.copytree(
        src=get_config()['media_path'], 
        dst=dst_path
    )