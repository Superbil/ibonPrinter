# ibonPrinter

![Python-Version](https://img.shields.io/static/v1?label=Python&message=3.x&style=flat-square&color=success&logo=python&logoColor=64BAFF)
![Require](https://img.shields.io/static/v1?label=Require&message=requests&style=flat-square&color=success)

目前僅在 Python 3.x 環境通過測試，Python 2.x 不保證運作正常
必要套件: requests

## Help

``` shell
ibonprinter -h
usage: ibonprinter [-h] [--name NAME] [--email EMAIL] file

7-11 iBon printer uploader.

positional arguments:
  file           Upload file

optional arguments:
  -h, --help     show this help message and exit
  --name NAME    User name
  --email EMAIL  User email
```

## 使用範例

### 不想收到 ibon 將取件編號及取件QRcode寄至信箱

``` shell
ibonprinter file.jpg
```

### 要收到 ibon 將取件編號及取件QRcode寄至信箱

``` shell
ibonprinter --name '陳大寶' --email 'example@example.com' file.jpg
```

### 結果

``` json
{
  "Pincode": "2901203801",
  "DeadLine": "2019/10/06 00:12:03",
  "FileQrcode": "iVBORw0KGgoAAAANSUhE........==",
  "FileDate": "2019/10/03 00:12:03",
  "ResultCode": "00",
  "Message": "成功"
}
```

### 例外錯誤:
RequestError: 對伺服器進行請求時發生錯誤

### LICENSE:
[MIT License](https://github.com/ThanatosDi/ibonPrinter/blob/master/LICENSE)

✔Commercial use
✔Modification
✔Distribution
✔Private use
