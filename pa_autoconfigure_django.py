from docopt import docopt

from pythonanywhere.django_project import DjangoProject
from pythonanywhere.snakesay import snakesay
from pythonanywhere.utils import ensure_domain


def main(repo_url, branch, domain, python_version, nuke):
    domain = ensure_domain(domain)
    project = DjangoProject(domain, python_version)
    project.sanity_checks(nuke=nuke)
    project.download_repo(repo_url, nuke=nuke),
    project.ensure_branch(branch),
    project.create_virtualenv(nuke=nuke)
    project.create_webapp(nuke=nuke)
    project.add_static_file_mappings()
    project.find_django_files()
    project.update_wsgi_file()
    project.update_settings_file()
    project.run_collectstatic()
    project.run_migrate()
    project.webapp.reload()
    print(snakesay(f'All done!  Your site is now live at https://{domain}'))
    print()
    project.start_bash()


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(
        arguments['<git-repo-url>'],
        arguments['--branch'],
        arguments['--domain'],
        arguments['--python'],
        nuke=arguments.get('--nuke')
    )
