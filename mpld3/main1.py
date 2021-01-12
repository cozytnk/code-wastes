"""mpld3 with custom templates

template will be rendered as:
    template.render(figid      =json.dumps(figid),
                    d3_url     =d3_url,
                    mpld3_url  =mpld3_url,
                    figure_json=json.dumps(figure_json, cls=NumpyEncoder),
                    extra_css  =extra_css,
                    extra_js   =extra_js)
see https://mpld3.github.io/_modules/mpld3/_display.html#fig_to_html

"""


_EX1 = """
<script type="text/javascript" src="{{ d3_url }}"></script>
<script type="text/javascript" src="{{ mpld3_url }}"></script>

<div id={{ figid }}></div>
<script type="text/javascript">
  !function(mpld3){
    mpld3.draw_figure({{ figid }}, {{ figure_json }});
  }(mpld3);
</script>
"""

_EX2 = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>mpld3 test</title>
  <script type="text/javascript" src="{{ d3_url }}"></script>
  <script type="text/javascript" src="{{ mpld3_url }}"></script>
</head>

<body>
  <div id={{ figid|safe }}></div>
  <script type="text/javascript">
    !function(mpld3){
      mpld3.draw_figure({{ figid|safe }}, {{ figure_json|safe }});
    }(mpld3);
  </script>
</body>
</html>
"""

_EX3 = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>mpld3 test</title>

<body>
  <div>test</div>
  <div>{{ fig|safe }}</div>
  <!--
    render as fig = mpld3.fig_to_html(fig=plt.gcf(), template_type='simple')
    note to escape like "|safe"
      see https://stackoverflow.com/questions/50531192/uncaught-syntaxerror-unexpected-token-when-passing-list-array-to-javascript
          https://tanuhack.com/jinja2-block/
          https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/templating.html
  -->
  <p>aaa</p>
</body>
</html>
"""


def register_template(template_type, template_text, mpld3=None):
    """
    """
    if mpld3 is None:
      mpld3 = globals()['mpld3']
    if template_type in ['simple', 'notebook', 'general']:
        raise ValueError(f'template_type "{template_type}" is reserved.')

    mpld3._display.TEMPLATE_DICT[template_type] = mpld3._display.jinja2.Template(template_text)


if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import mpld3

    with open('index_ex2.html', mode='r') as f:
        template_text = f.read()
    register_template(template_type='test', template_text=template_text)
    # register_template(template_type='test', template_text=template_text, mpld3=mpld3)


    plt.plot(range(100))
    # mpld3.show(template_type='simple')
    mpld3.show(template_type='test')
