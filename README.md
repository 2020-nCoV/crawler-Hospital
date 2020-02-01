# crawler-Hospital

## 总述

本程序用于爬取**新型冠状病毒肺炎**疫情期间全国的发热门诊和定点治疗医院，并通过 xls 文件持久化到本地。



## 工作方法

通过抓包工具 Fiddler 分析“国务院微信小程序”所指向的 API 地址，向特定地址发送所需查询地区的行政区域代码即可返回 JSON 格式的医院数据，数据处理完成后使用 Pandas 生成 xls 文件。



## 使用方法

若需获取发烧门诊信息，请使用以下命令
``` 
python main.py fever
```

若需获取 nCoV 定点医院信息，请使用以下命令
``` 
python main.py ncov
```

若您电脑上未安装 Python 环境，可直接下载本仓库中的数据文件



## 注意

经试验，每次请求时携带的认证信息仅有 1 天左右的有效期，若请求失败，请在微信中打开“国务院”小程序，自行抓包替换下方 header 中的相关字段。

```json
{'x-tif-did': 'ZKVdmWTv3L',
'x-tif-openid': 'ojyj-45vD5swZ9AxQDcBpPqKpat4',
'x-tif-sid': '3e4632d4856f1ec177d54062e2a939d0b2',
'x-yss-city-code': '4400'}
```



## 作者相关

如有问题请发送邮件至 ultraxia@foxmail.com 联系作者。



## 武汉加油！