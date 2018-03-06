# dm_dex_parser
解析 dex 文件，python 安装包的封装

本项目是 [dex_parser](https://github.com/ondreji/dex_parser) 的引用，主要是加了层封装，可以作为第三方库导入 python 环境。

# install

`python setup dm_dex_parser.zip`

# import 

`import dex_parser` or `from dex_parser import dex`

# usage

```python
from dex_parser import dex
import pprint

dex_obj = dex.dex_parser("F:\code_workplace\ida_script\classes.dex")
class_data = dex_obj.get_class_data()
pprint.pprint(class_data)
```
