import requests
import json

from time import sleep

class VKPoint:
    def __init__(self, user_id, token):
        self.link = 'https://vkpoint.vposter.ru/api/method/'
        self.user_id = user_id
        self.token = token
        self.user_agent = {
            "Accept-language": "en",
            "Cookie": "foo=bar",
            "User-Agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:10"}

    def _send_api_request(self, method, params = None, headers = None):
        linker = self.link + method
        response = requests.get(linker, params = params, headers = headers).json()
        if 'error' in response:
            return Exception(response)
        return response['response']

    def setCallback(self, url): 
        data = {'user_id': self.user_id, 'callback_url': url, 'access_token': self.token}
        return self._send_api_request(method = 'account.MerchantSend?', params = data)

    def getUrl(self, point = None, fixed = False):
        url = f"https://vk.com/app6748650#u={self.user_id}"
        if point:
            url += f"&point={point}"
        if fixed:
            url += "&fixed"
        return url

    def send_payment(self, to_id, amount):
        data = {'user_id_to': self.user_id, 'user_id': to_id, 'point': amount, 'access_token': self.token}
        return self._send_api_request(method = 'account.MerchantSend?', params = data)

    def get_history(self, user_id):
        data = {'user_id': user_id}
        return self._send_api_request(method = 'users.HistoryTransactions?', params = data, headers = self.user_agent)

    def get_point(self, user_id = None):
        user_id = user_id or self.user_id
        data = {'user_id': user_id}
        return self._send_api_request(method = 'account.getPoint?', params = data, headers = self.user_agent)

    def get_top(self, count):
        data = {'count': count}
        return self._send_api_request(method = 'users.getTop?', params = data, headers = self.user_agent)

    def get_top_vip(self, count):
        data = {'count': count}
        return self._send_api_request(method = 'users.getTopVip?', params = data, headers = self.user_agent)

    def get_top_groups(self, count):
        data = {'count': count}
        return self._send_api_request(method = 'groups.getTop?', params = data, headers = self.user_agent)

    def get_info_groups(self, group_id):
        data = {'group_id': group_id}
        return self._send_api_request(method = 'groups.Info?', params = data, headers = self.user_agent)

    def get_point_ids(self, user_ids):
        data = {'user_ids': user_ids}
        return self._send_api_request(method = 'users.getTopIds?', params = data, headers = self.user_agent)

    def get_games_get_byid(self):
        return self._send_api_request(method = 'games.getByld', headers = self.user_agent)

    def get_search(self, search, count):
        data = {'search': search, 'count': count}
        return self._send_api_request(method = 'users.search?', params = data, headers = self.user_agent)

    def get_app_notif(self,count):
        data = {'count': count}
        return self._send_api_request(method = 'app.notif?', params = data, headers = self.user_agent)

    def get_stock(self, count):
        data = {'count': count}
        return self._send_api_request(method = 'get.Stock?', params = data, headers = self.user_agent)

    def get_ex_top(self, count):
        data = {'count': count}
        return self._send_api_request(method = 'ex.getTop?', params = data, headers = self.user_agent)

    def get_ex_search(self, search, count):
        data = {'search': search, 'count': count}
        return self._send_api_request(method = 'ex.search?', params = data, headers = self.user_agent)

    def merchant_get(self, user_id):
        data = {'user_id': user_id, 'user_id_to': self.user_id}
        request_data = self._send_api_request(method = 'account.MerchantGet?', params = data, headers = self.user_agent)
        return request_data['count_trans_day']

    def longpoll(self, timeout = 1):
        last_transfer = self.get_history(self.user_id)['items'][0]['id']
        while True:
            history = self.get_history(self.user_id)['items']

            for payment in history:
                if payment['id'] > last_transfer:
                    yield payment
                else: break
                last_transfer = history[0]['id']
            sleep(timeout)