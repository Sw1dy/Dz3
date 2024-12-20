import unittest
import xml.etree.ElementTree as ET
from io import StringIO
from translate import parse_xml, convert_to_config_language, remove_bom

class TestTranslate(unittest.TestCase):

    def test_remove_bom(self):
        data_with_bom = '\ufeff<?xml version="1.0"?><root></root>'
        expected_data = '<?xml version="1.0"?><root></root>'
        self.assertEqual(remove_bom(data_with_bom), expected_data)

    def test_parse_xml(self):
        xml_data = '<root><child>value</child></root>'
        root = parse_xml(xml_data)
        self.assertIsNotNone(root)
        self.assertEqual(root.tag, 'root')

    def test_parse_xml_invalid(self):
        xml_data = '<root><child>value</child>'
        with self.assertRaises(SystemExit) as cm:
            parse_xml(xml_data)
        self.assertEqual(cm.exception.code, 1)

    def test_convert_to_config_language(self):
        xml_data = '<root><child1>value1</child1><child2>value2</child2></root>'
        root = ET.fromstring(xml_data)
        expected_output = '''root:
  child1:
    значение: value1
  child2:
    значение: value2'''
        self.assertEqual(convert_to_config_language(root), expected_output)

    def test_convert_to_config_language_with_attributes(self):
        xml_data = '''<root>
                        <child1 attribute1="value1_attr1" attribute2="value1_attr2">value1</child1>
                        <child2 attribute1="value2_attr1">value2</child2>
                      </root>'''
        root = ET.fromstring(xml_data)
        expected_output = '''root:
  child1:
    attribute1: value1_attr1
    attribute2: value1_attr2
    значение: value1
  child2:
    attribute1: value2_attr1
    значение: value2'''
        self.assertEqual(convert_to_config_language(root), expected_output)

    def test_convert_to_config_language_nested(self):
        xml_data = '''<root>
                        <child1>
                          <subchild1>subvalue1</subchild1>
                          <subchild2 attribute1="subvalue2_attr1">subvalue2</subchild2>
                        </child1>
                      </root>'''
        root = ET.fromstring(xml_data)
        expected_output = '''root:
  child1:
    subchild1:
      значение: subvalue1
    subchild2:
      attribute1: subvalue2_attr1
      значение: subvalue2'''
        self.assertEqual(convert_to_config_language(root), expected_output)

    def test_main_function(self):
        # Создаем временный файл для ввода и вывода
        input_xml = '''<root>
                         <child1>value1</child1>
                         <child2>value2</child2>
                       </root>'''
        expected_output = '''root:
  child1:
    значение: value1
  child2:
    значение: value2'''

        # Перенаправляем stdin и stdout
        with open('input.xml', 'w', encoding='utf-8') as f:
            f.write(input_xml)

        with open('output.txt', 'w', encoding='utf-8') as f:
            pass

        import sys
        from translate import main

        sys.argv = ['translate.py', 'output.txt']
        with open('input.xml', 'r', encoding='utf-8') as f:
            sys.stdin = f
            main()

        with open('output.txt', 'r', encoding='utf-8') as f:
            output = f.read()

        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
