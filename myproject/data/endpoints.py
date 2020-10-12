#-*- coding: UTF-8 -*-
# from data.settings import Host_test, Host_test1
from myproject.data.settings import Host_test, Host_test1, Host_lebov2

Login = Host_test+"bobuilder/sessions"
Apps = Host_test+"bobuilder/apps"
Toh = Host_test1 + "japi/toh"

# 乐泊V2版本接口
Register = Host_lebov2 + "/wujiang/dev/api/v2/parking/account/register"
Publickey = Host_lebov2 + "/wujiang/dev/api/v2/parking/app/v1/auth/publicKey/{openid}"
Token = Host_lebov2 + "/wujiang/dev/api/v2/parking/app/v1/auth/token"
BindCar = Host_lebov2 + "/wujiang/dev/api/v2/parking/car/bindCar"
GetParkingPayBase = Host_lebov2 + "/wujiang/dev/api/v2/parking/order/getParkingPayBase/{siteId}/{carPlateColor}/{carPlateNo}/{openId}"

