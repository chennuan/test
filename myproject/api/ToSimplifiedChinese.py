import requests


class ToSimplifiedChinese():


    def api_get_toSimplifiedChinese(self, url, params, headers):

        return requests.get(url, params=params, headers=headers)


