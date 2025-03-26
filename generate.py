from jinja2 import Environment, FileSystemLoader


def generate_html_report(results, output_file="report.html"):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    rendered_html = template.render(results=results)

    with open(output_file, 'w') as f:
        f.write(rendered_html)
    print(f"Report generated: {output_file}")
