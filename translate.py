import sys
import argparse
import xml.etree.ElementTree as ET


def remove_bom(data):
    # Удаляем BOM, если он присутствует
    if data.startswith('\ufeff'):
        return data[1:]
    return data


def parse_xml(xml_data):
    try:
        # Парсим XML-данные
        root = ET.fromstring(xml_data)
        return root
    except ET.ParseError as e:
        print(f"Ошибка парсинга XML: {e}")
        sys.exit(1)


def convert_to_config_language(root):
    # Преобразуем XML-данные в учебный конфигурационный язык
    config_lines = []

    def process_element(element, indent=0):
        line = ' ' * indent + f'{element.tag}:'
        config_lines.append(line)
        for attr, value in element.attrib.items():
            config_lines.append(' ' * (indent + 2) + f'{attr}: {value}')
        for child in element:
            process_element(child, indent + 2)
        if element.text and element.text.strip():
            config_lines.append(' ' * (indent + 2) + f'значение: {element.text.strip()}')

    process_element(root)
    return '\n'.join(config_lines)


def main():
    parser = argparse.ArgumentParser(description='Convert XML to config language.')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    args = parser.parse_args()

    # Читаем XML-данные из стандартного ввода
    xml_data = sys.stdin.read()
    xml_data = remove_bom(xml_data)

    # Парсим XML-данные
    root = parse_xml(xml_data)

    # Преобразуем XML-данные в учебный конфигурационный язык
    config_language_text = convert_to_config_language(root)

    # Записываем результат в файл
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(config_language_text)


if __name__ == '__main__':
    main()
