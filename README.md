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

pstree -ap|grep gunicorn


30693为主进程号，使用以下命令，重启Gunicorn
kill -HUP 30693
```

windows 安装 mysqlclient

```
pip install https://link.juejin.im/?target=https%3A%2F%2Fdownload.lfd.uci.edu%2Fpythonlibs%2Fr5uhg2lo%2Fmysqlclient-1.3.13-cp37-cp37m-win32.whl
```

安装 wxmp

```
pip install git+git://github.com/lzjun567/wxmp --upgrade

```

### 任务队列启动（非必须）

```python
>pipenv run celery beat -A weihub.tasks.tasks  -l info
>pipenv run celery -A weihub.tasks.tasks worker -l info
```
worker 在 Windows 启动时加参数 --pool=solo


### 数据库备份
```
./mysqldump -hlocalhost -uxxx -pxxxx --single-transaction  wxhub | gzip > backupfile.sql.gz
./ossutil64 cp /usr/local/mysql/bin/backupfile.sql.gz oss://ershicimi-backup
```


### [需求池](./doc/xuqiu.md)

### [待修复bug](./doc/bug.md)


### 测试脚本

```
pipenv run python -m unittest
```








