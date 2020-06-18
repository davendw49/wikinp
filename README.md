# WIKI for Nobel Prize and Pulitzer Prize 搜索引擎
----
> scrapy+elasticsearch+flask+vue

just for fun,for learn.

### how to run？
```
# 安装中文分词插件ik
# https://github.com/medcl/elasticsearch-analysis-ik
> elasticsearch-plugin install <>
# 启动elasticsearch
> bin/elasticsearch

# 设置虚拟环境
> python -m venv env
> source env/bin/activate
> pip install -r requirements.txt

# 启动爬虫
# 数据自动送入elasticsearch
scrapy crawl douban

# server
> python app.py

# client
> npm install
> npm run serve

# 访问: localhost:8080
```