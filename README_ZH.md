# a3exception

[English](README.md) | 简体中文

`a3exception`是一个用于统一异常的包。

## 1. 简介

### errors

* 基类异常: Error
* 预设的客户端异常: ValidationError, NotFoundError ...
* 预设的服务端异常: ServerKnownError, ServerUnknownError
* 预设的通用异常: PanicError

### DynamicErrorFactory

* 根据字典动态生成异常: build_error_by_status
* 添加自定义异常: add_custom_error_cls

## 2. 使用

### 安装

```shell
pip install a3exception

```

### 样例

```python
from a3exception.dynamic_error_factory import DynamicErrorFactory
from a3exception.errors import Error


class MyError(Error):
    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)

        
if __name__ == "__main__":
    DynamicErrorFactory.add_custom_error_cls(MyError)
    
    error_message = "custom error"
    error = DynamicErrorFactory.build_error_by_status(status=MyError.__name__, message=error_message)
    assert isinstance(error, MyError)
    assert error.message == error_message

```
