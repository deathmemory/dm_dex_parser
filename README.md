# dm_dex_parser
解析 dex 文件，python 安装包的封装

本项目是 [dex_parser](https://github.com/ondreji/dex_parser) 的引用，主要是加了层封装，可以作为第三方库导入 python 环境。

# install

`python setup.py install`

# import 

`import dex_parser` or `from dex_parser import dex`

# usage

```python
def main():
    if sys.argv < 2:
        print ("Usages: %s dex_file" % sys.argv[0])
        quit()

    filename = sys.argv[1]
    # filename = "D:\\classes.dex"
    dex = dex_parser(filename)
    for key in dex.m_class_name_id:
        if ('MobileAgent' in key):
            clsid = dex.m_class_name_id[key]
            print(dex.getclassmethod_count(clsid))
            method_id, code_off = dex.getclassmethod(clsid, 0)
            print(hex(code_off))
            methodcode = method_code(dex, code_off)
            methodcode.printf(dex)
            method_id, code_off = dex.getclassmethod(clsid, virtrualmethod_idx= 0)
            print(hex(code_off))
            methodcode = method_code(dex, code_off)
            methodcode.printf(dex)
            print(dex.getmethodname(method_id))
            print(dex.getmethodfullname(method_id))
            print(dex.getmethodfullname1(method_id))
```
