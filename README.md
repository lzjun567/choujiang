系统要求 python3.6 以上版本

### 创建虚拟环境
进入项目目录后， 执行
```
python3 -m  venv venv
```


### 激活虚拟环境

```
source  venv/bin/activate
```

### 安装依赖文件

```
pip install -r requirements.txt
```

### 启动

```
flask run
```

### 停止

ctrl+c


---------------------------


```
# 启动Gunicorn
 nohup gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app &
```

windows 安装 mysqlclient

```
pip install  mysqlclient-1.4.6-cp37-cp37m-win32.whl
```




### 测试脚本

```
pipenv run python -m unittest
```








