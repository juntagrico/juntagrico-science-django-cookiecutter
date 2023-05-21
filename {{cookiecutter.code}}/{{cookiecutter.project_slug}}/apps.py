from django.apps import AppConfig

class {{cookiecutter.project_slug|capitalize}}Config(AppConfig):
    name = '{{cookiecutter.project_slug}}'
    verbose_name = "{{cookiecutter.organisation_name}}"

    def ready(self):
        pass
