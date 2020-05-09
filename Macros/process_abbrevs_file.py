import xml.etree.ElementTree as ET

xml_tree = ET.parse('Abbreviations.kmmacros')

exceptions = {'=lorem': '200 words of [Lorem ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum)',
              '=uktel': 'my UK phone number',
              '=shrugs': '`¯\_(ツ)_/¯`'}

expect_group = ''

for child in xml_tree.getroot().iter():
    if child.tag == 'key' and child.text == 'Text':
        expect_group = 'printed_text'
        continue
    elif child.tag == 'key' and child.text == 'TypedString':
        expect_group = 'typed_string'
        continue
    elif expect_group == 'printed_text':
        assert child.tag == 'string'
        printed_text = child.text
        expect_group = ''
    elif expect_group == 'typed_string':
        assert child.tag == 'string'
        typed_string = child.text
        expect_group = ''
        if typed_string in exceptions:
            quoted_printed_text = exceptions[typed_string]
        else:
            quoted_printed_text = f'“{printed_text}”'
        print(f' - `{typed_string}` produces {quoted_printed_text}')
    else:
        expect_group = ''
