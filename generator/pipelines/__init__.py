from utils.common import get_config
from templates import generate_template, write_rendered_template_to_file

def global_pipeline():
    projects_pipeline()
    static_pipeline()
    home_pipeline()

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