# Задание 3
# Учебный конфигурационный язык
Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.

Входной текст на языке xml принимается из стандартного ввода. Выходной
текст на учебном конфигурационном языке попадает в файл, путь к которому
задан ключом командной строки.

## Пример работы

### Входной файл
```txt
<?xml version="1.0"?>
<Tests xmlns="http://www.adatum.com">
  <Test TestId="0001" TestType="CMD">
    <Name>Convert number to string</Name>
    <CommandLine>Examp1.EXE</CommandLine>
    <Input>1</Input>
    <Output>One</Output>
  </Test>
  <Test TestId="0002" TestType="CMD">
    <Name>Find succeeding characters</Name>
    <CommandLine>Examp2.EXE</CommandLine>
    <Input>abc</Input>
    <Output>def</Output>
  </Test>
  <Test TestId="0003" TestType="GUI">
    <Name>Convert multiple numbers to strings</Name>
    <CommandLine>Examp2.EXE /Verbose</CommandLine>
    <Input>123</Input>
    <Output>One Two Three</Output>
  </Test>
  <Test TestId="0004" TestType="GUI">
    <Name>Find correlated key</Name>
    <CommandLine>Examp3.EXE</CommandLine>
    <Input>a1</Input>
    <Output>b1</Output>
  </Test>
  <Test TestId="0005" TestType="GUI">
    <Name>Count characters</Name>
    <CommandLine>FinalExamp.EXE</CommandLine>
    <Input>This is a test</Input>
    <Output>14</Output>
  </Test>
  <Test TestId="0006" TestType="GUI">
    <Name>Another Test</Name>
    <CommandLine>Examp2.EXE</CommandLine>
    <Input>Test Input</Input>
    <Output>10</Output>
  </Test>
</Tests>
```
### Перевод 
```python
{http://www.adatum.com}Tests:
  {http://www.adatum.com}Test:
    TestId: 0001
    TestType: CMD
    {http://www.adatum.com}Name:
      значение: Convert number to string
    {http://www.adatum.com}CommandLine:
      значение: Examp1.EXE
    {http://www.adatum.com}Input:
      значение: 1
    {http://www.adatum.com}Output:
      значение: One
  {http://www.adatum.com}Test:
    TestId: 0002
    TestType: CMD
    {http://www.adatum.com}Name:
      значение: Find succeeding characters
    {http://www.adatum.com}CommandLine:
      значение: Examp2.EXE
    {http://www.adatum.com}Input:
      значение: abc
    {http://www.adatum.com}Output:
      значение: def
  {http://www.adatum.com}Test:
    TestId: 0003
    TestType: GUI
    {http://www.adatum.com}Name:
      значение: Convert multiple numbers to strings
    {http://www.adatum.com}CommandLine:
      значение: Examp2.EXE /Verbose
    {http://www.adatum.com}Input:
      значение: 123
    {http://www.adatum.com}Output:
      значение: One Two Three
  {http://www.adatum.com}Test:
    TestId: 0004
    TestType: GUI
    {http://www.adatum.com}Name:
      значение: Find correlated key
    {http://www.adatum.com}CommandLine:
      значение: Examp3.EXE
    {http://www.adatum.com}Input:
      значение: a1
    {http://www.adatum.com}Output:
      значение: b1
  {http://www.adatum.com}Test:
    TestId: 0005
    TestType: GUI
    {http://www.adatum.com}Name:
      значение: Count characters
    {http://www.adatum.com}CommandLine:
      значение: FinalExamp.EXE
    {http://www.adatum.com}Input:
      значение: This is a test
    {http://www.adatum.com}Output:
      значение: 14
  {http://www.adatum.com}Test:
    TestId: 0006
    TestType: GUI
    {http://www.adatum.com}Name:
      значение: Another Test
    {http://www.adatum.com}CommandLine:
      значение: Examp2.EXE
    {http://www.adatum.com}Input:
      значение: Test Input
    {http://www.adatum.com}Output:
      значение: 10
```
## Использование
```python
python translate.py output.txt < input.xml
```

## Запуск тестов
```python
python -m unittest translateTest.py
```
