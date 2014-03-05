import os

import yaml


def load_modules(data):
    result = yaml.load(data)
    if result:
        apache = result.get('apache', {})
        if apache:
            return apache.get('modules', [])
    return []


def install_modules(modules):
    installed = 0
    for module in modules:
        print '\e[1G\e[K'+"      Installing Apache module %s" % module
        os.system("a2enmod "+module+" >/dev/null 2>&1")
        installed = installed + 1

    if installed > 0: 
       os.system('/etc/init.d/apache2 restart >/dev/null 2>&1')
       print '\e[1G\e[K'+"      Done installing Apache modules."
    else:
       print '\e[1G\e[K'+"      No Apache modules installed."


def load_file(working_dir="/home/application/current"):
    files_name = ["app.yaml", "app.yml"]
    for file_name in files_name:
        try:
            with open(os.path.join(working_dir, file_name)) as f:
                return f.read()
        except IOError:
            pass
    return ""


def main():
    print '\e[1G\e[K'+"----> Parsing required Apache modules"
    data = load_file()
    modules = load_modules(data)
    install_modules(modules)

main()
