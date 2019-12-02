from vkpoint_api import VKPoint, VKPointPool

VKPointSession = VKPoint(user_id = 123456789, token = '_tokentokentokentokentokentoken_')

for payment in VKPointPool(VKPointSession).listen(sleep = 5):

    user_id = payment['info']['user_id']
    amount = payment['info']['point']

    print('Получен платёж на сумму {amount} от {user_id}'.format(amount = amount, user_id = user_id))