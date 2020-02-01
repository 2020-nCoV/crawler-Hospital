import sys
import requests
import json
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

rows = []
cities = []


def getHospital(url, cityData):
    cityArray = cityData.split("=")
    cityName = cityArray[0]
    cityCode = cityArray[1]
    form = {"search_key": "", "area_code": cityCode, "page_size": 300, "page": 1}
    header = {
        'Host': 'xcx.www.gov.cn',
        'accept': '*/*',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'User-Agent': '',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json;charset=utf-8',
        'Connection': 'keep-alive',
        'Referer': 'https://servicewechat.com/wxbebb3cdd9b331046/63/page-frame.html',
        'x-tif-did': 'ZKVdmWTv3L',
        'x-tif-openid': 'ojyj-45vD5swZ9AxQDcBpPqKpat4',
        'x-tif-sid': '3e4632d4856f1ec177d54062e2a939d0b2',
        'x-yss-city-code': '4400',
        'x-yss-page': 'doctor/pages/pneumonia/pneumonia'
    }
    try:
        response = requests.post(
            url,
            data=json.dumps(form),
            headers=header,
            verify=False,
            timeout=15).json()

        data = response["data"]["list"]

        for hospital in data:
            name = hospital["name"]
            level = hospital["level"]
            if level == "":
                level = "暂无描述"
            linkman = hospital["linkman"]
            if linkman == "":
                linkman = "暂无联系人"
            link_phone = hospital["link_phone"]
            if link_phone == "":
                link_phone = "暂无联系号码"
            address = hospital["address"]
            if address == "":
                address = "暂无地址"
            remark = hospital["remark"]
            if remark == "":
                remark = "暂无描述"
            rows.append((cityName, name, level, linkman, link_phone, address, remark))

    except Exception as e:
        raise e


def main():
    with open("config.ini", encoding="utf-8") as f:
        for i in f.readlines():
            cities.append(i.replace("\n", ""))

    args = sys.argv

    if len(args) != 2:
        print("请检查参数")

    else:
        type = args[1]

        if type == "fever":
            url = "https://xcx.www.gov.cn/ebus/gwymp/api/r/sars/QueryFare"
            fileName = "feverHospital.xls"

        if type == "ncov":
            url = "https://xcx.www.gov.cn/ebus/gwymp/api/r/sars/QueryJiuzhi"
            fileName = "ncovHostpital.xls"

        print("正在获取数据集")

        for data in cities:
            getHospital(url, data)

        df = pd.DataFrame(rows)
        df.columns = ['城市', '医院名称', '医院等级', '医院联系人', '医院联系电话', '医院地址', '备注']
        df.to_excel(fileName)
        print('数据集获取完成')


if __name__ == '__main__':
    main()
