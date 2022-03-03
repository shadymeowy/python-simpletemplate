from simple_template import template

# Examples from bottlepy documentation
# https://bottlepy.org/docs/dev/stpl.html

print(template('Hello {{name}}!', name='World'))

my_dict={'number': '123', 'street': 'Fake St.', 'city': 'Fakeville'}
print(template('I live at {{number}} {{street}}, {{city}}', **my_dict))

print(template(
r"""<ul>
% for item in map(str,range(10)):
    <li>{{item}}</li>
% end
</ul>"""))
