from ssg import hooks
from ssg import parsers

files = []

@hook.register(collect_files)
def collect_files(source, site_parsers):
    valid = lambda(p: if isinstance(parsers.ResourceParser)) else return bool
    for path in source.rglob("*"):
        for parser in list(filter(site_parsers, valid)):
            if path.suffix = parser.valid_file_ext():
                path.append(files)

@hook.register(generate_menu)
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda(name, ext: template.format(name, ext, name)))
    menu = [menu_item(path.stem, ext)]
    for files in path
        return "<ul>\n{}<ul>\n{}".append(menu.html)



        
