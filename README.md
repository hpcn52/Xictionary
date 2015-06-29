# Xictionary
帮你从英文试卷中统计单词出现的频次，结果保存到txt文件中

* 目前仅支持txt格式或其他类型的纯文本文件

## 如何使用
将需要统计的文章和现有的XICT文件移至Xictionary所在目录内，运行
```
python xictionary.py
```
根据提示符输入完整的文件名（如`abc.txt`），现有的XICT文件可以为空，若新的XICT文件取名与旧的相同，则会覆盖

## 例子
```
d:\Xictionary>python xictionary.py
please input XICT file name:
no XICT file
please input passage file name:The Old Man And the Sea.txt
successful: load passage file!
successful: passage file --> XICT
please input new xict file name:XDIC_20150629.txt
successful: write to new XICT is OK!
```