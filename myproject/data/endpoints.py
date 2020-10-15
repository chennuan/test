# -*- coding: UTF-8 -*-
# from data.settings import Host_test, Host_test1
from myproject.data.settings import Host_test, Host_test1, Host_lebov2

Login = Host_test + "bobuilder/sessions"
Apps = Host_test + "bobuilder/apps"
Toh = Host_test1 + "japi/toh"

# 乐泊V2版本接口
# 注册接口
Register = Host_lebov2 + "/wujiang/dev/api/v2/parking/account/register"
# 获取Publickey
Publickey = Host_lebov2 + "/wujiang/dev/api/v2/parking/app/v1/auth/publicKey/{openid}"
# 获取token
Token = Host_lebov2 + "/wujiang/dev/api/v2/parking/app/v1/auth/token"
# 绑定车辆
BindCar = Host_lebov2 + "/wujiang/dev/api/v2/parking/car/bindCar"
# 获取停车缴费信息
GetParkingPayBase = Host_lebov2 + "/wujiang/dev/api/v2/parking/order/getParkingPayBase/{siteId}/{carPlateColor}/{carPlateNo}/{openId}"
# 获取列表
GueryLoadingActivity = Host_lebov2 + "/wujiang/dev/api/v2/parking/advertisement/queryLoadingActivity"
# 登录接口
Login = Host_lebov2 + "/wujiang/dev/api/v2/parking/account/login/{openid}"
# 获取绑定车辆列表
GetBindCarsList = Host_lebov2 + "/wujiang/dev/api/v2/parking/car/getBindCarsList/{siteId}/{userId}"
# 获取用户下所有待付款订单
GetPendingOrdersByCarPlateNo = Host_lebov2 + "/wujiang/dev/api/v2/parking/order/getPendingOrdersByCarPlateNo"
# 获取停车场区域
GetParkingLotArea = Host_lebov2 + "/wj/dev/api/v1/console/dict/getParkingLotArea/{parkId}"
# 获取停车缴费详情
GetParkingPayDetail = Host_lebov2 + "/wujiang/dev/api/v2/parking/order/getParkingPayDetail/{siteId}/{carPlateColor}/{carPlateNo}/{openId}"
# 支付
AppPay = Host_lebov2 + "/wujiang/dev/api/v2/parking/wxpay/appPay"
# 解绑车辆
NnBindCar = Host_lebov2 + "/wujiang/dev/api/v2/parking/car/unbindCar/{userId}/{carId}/{plateNo}/{plateColor}"
