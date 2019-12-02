import requests, six, time

class VKPoint(object):

    __slots__ = ('__user_id', '__token', '__ApiUrl', '__AppUrl', '__UserAgent')

    def __init__(self, user_id, token):
        self.__user_id = user_id
        self.__token = token
        self.__ApiUrl = 'https://vkpoint.vposter.ru/api/method/'
        self.__AppUrl = 'https://vk.com/app6748650'
        self.__UserAgent = {
            "Accept-language": "en",
            "Cookie": "foo=bar",
            "User-Agent": "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:10"
            }

    def _SendRequestss(self, method, params = None):
        response = requests.get(self.__ApiUrl + method, params = params, headers = self.__UserAgent).json()
        if 'error' in response:
            return Exception(response)
        return response['response']

    def MerchantGet(self, user_id):
        params = {
            'user_id_to': self.__user_id,
            'user_id': user_id
        }
        return self._SendRequestss('account.MerchantGet', params = params)

    def getPoint(self, user_id = None):
        user_id = user_id or self.__user_id
        params = {
            'user_id': user_id,
            'access_token': self.__token
        }
        return self._SendRequestss('account.getPoint', params = params)

    def merchantSend(self, user_id, point): 
        params = {
            'user_id_to': self.__user_id,
            'user_id': user_id,
            'point': point,
            'access_token': self.__token
        }
        return self._SendRequestss('account.MerchantSend', params = params)

    def HistoryTransactions(self, user_id = None):
        params = {
            'user_id': user_id or self.__user_id
        }
        return self._SendRequestss('users.HistoryTransactions', params = params)

    def GetApi(self):
        return VKPointApiMethod(self, self.__token, self.__user_id)

class VKPointApiMethod(object):

    __slots__ = ('_api', '_method', '__token', '__user_id')

    def __init__(self, vkPointObj, token, user_id, method = None):
        self._api = vkPointObj
        self._method = method
        self.__token = token
        self.__user_id = user_id

    def __getattr__(self, method):
        if '_' in method:
            m = method.split('_')
            method = m[0] + ''.join(i.title() for i in m[1:])

        return VKPointApiMethod(
            self._api,
            self.__token,
            self.__user_id,
            (self._method + '.' if self._method else '') + method
        )

    def __call__(self, **kwargs):
        for k, v in six.iteritems(kwargs):
            if isinstance(v, (list, tuple)):
                kwargs[k] = ','.join(str(x) for x in v)

        kwargs.update({
            'user_id_to': self.__user_id,
            'user_id': kwargs['user_id'] if 'user_id' in kwargs else self.__user_id,
            'access_token': self.__token
        })

        return self._api._SendRequestss(method = self._method, params = kwargs)

class VKPointPool(object):

    __slots__ = ('__api', '__LastTransactions')

    def __init__(self, ApiObject):
        self.__api = ApiObject
        self.__LastTransactions = self.__api.HistoryTransactions()['items'][0]['id']

    def listen(self, sleep = 5):
        while True:
            history = self.__api.HistoryTransactions()['items']
            if history[0] != self.__LastTransactions:
                for payment in history:
                    if payment['id'] > self.__LastTransactions:
                        yield payment
                else:
                    self.__LastTransactions = self.__api.HistoryTransactions()['items'][0]['id']

            time.sleep(sleep)