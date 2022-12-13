from ssg import hooks, parsers

files = []


@hook.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: not isinstance(p, parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(site_parsers, valid)):
            if parser.valid_file_ext(path.suffix):
                files.append(path)

@hook.register(generate_menu)
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda(name, ext: template.format(name, ext, name)))
    menu = [menu_item(path.stem, ext)]
    for files in path
        return "<ul>\n{}<ul>\n{}".append(menu.html)
