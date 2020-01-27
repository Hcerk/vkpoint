vkpoint_api (v 2.0.7)
=================================================================================================================================================================================
**vkpoint** - это python модуль для работы с монетой VK Point (VK Point API Wrapper)
* [Сама библиотека](./vkpoint) (python3)
* [Примеры](./examples)

#### Установка модуля
```bash
python -m pip install vkpoint_api
```

Работа с модулем
---
#### Лёгкий старт в модуле 
```python /* или python3 */
from vkpoint import VKPoint

VKPointSession = VKPoint(user_id = 123456789, token = '_tokentokentokentokentokentoken_', hosting = 'https://site.org/')
```
* `user_id` - Ваш ID от Социальной сети Вконтакте
* `token` - Токен VKPoint (ключ получаем [здесь](https://vkpoint.vposter.ru/api/method/token))
* `hosting` - Ссылка на хостинг, где установлен скрипт


### 4-ре основных метода в VKPoint Wrapper 
#### --> MerchantSend
***Перевод VK Point с аккаунта на другой аккаунт. Учтите, перевод работает только на те аккаунты, которые есть в приложении VK Point.***
##### Python
```python /* или python3 */
VKPointSession.merchantSend(user_id = 151631142, point = 0.001)
```
* `user_id` - кому переводим
* `point` - сумма перевода (Учтите! Что если вы укажите `1` по переведётся 1. Если `0.001`, то переведётся соответственно 0.001)
#### Ответ
``` json
{
  "user_id": "151631142", 
  "amount": 0.001, 
  "user_id_to": "111111111"
}
```
* `user_id_to` - От кого был перевод
#### --> getPoint
***Вывод данных профиля***
##### Python
```python /* или python3 */
VKPointSession.getPoint(user_id = 151631142)
```
* `user_id` - Чьи данные выводим (Не указываем user_id, если нужно вывести информацию о себе)
##### Ответ
``` json
{
  "id": "", 
  "user_id": "151631142", 
  "first_name": "Илья", 
  "last_name": "Светский", 
  "photo": "https://sun9-12.userapi.com/c850724/v850724626/1dfcc8/Pxx44odNlxM.jpg?ava=1", 
  "myning": "0", 
  "user_agent": null, 
  "ban": "0", 
  "reason_ban": "", 
  "bot": "20", 
  "admin": "0", 
  "verified": "0", 
  "point": 2132191251, 
  "balance": 10, 
  "balance_set": "15", 
  "city_title": "", 
  "count_users": "73473", 
  "count_groups": "1022", 
  "click": 0.525, 
  "click_count": 1, 
  "summTimeSpeed": "1", 
  "summTimeSpeed_count": "1", 
  "summTimeZhuk": "47", 
  "summTimeZhuk_count": "15", 
  "summTimeServer": "297573", 
  "summTimeServer_count": "61", 
  "summTimeGeympad": "457", 
  "summTimeGeympad_count": "22", 
  "summTimePlata": "6772090", 
  "summTimePlata_count": "57", 
  "summTimeProces": "55457716", 
  "summTimeProces_count": "64", 
  "debug": "0", 
  "date_visit": 1575297129, 
  "online": 0
}
```
#### --> MerchantGet
***Выводит информацию о том, сколько отправлено поинтов пользователю (переводы). Этим методом можно подсчитать сколько осталось до лимита (1KК ботам)***
##### Python
```python /* или python3 */
VKPointSession.MerchantGet(user_id = 151631142)
```
* `user_id` - ID пользователя с кем проверяется остаток по выводам
##### Ответ
``` json
{
  "count_trans_day": 0
}
```
* `count_trans_day` - Количество сколько переведено

#### --> HistoryTransactions
***Вывод истории переводов пользователя***
##### Python
```python /* или python3 */
VKPointSession.HistoryTransactions(user_id = 151631142)
```
* `user_id` - ID пользователя, чью выводим историю (Оставить пустым, если если нужно вывести свою историю переводов)
##### Ответ
``` json
{
  "count_day": "24", 
  "items": [
    {
      "id": "1726502", 
      "first_name": "Alex", 
      "last_name": "Alex", 
      "photo": "https://vk.com/images/camera_200.png?ava=1", 
      "datetime": 1575301326, 
      "info": {
        "type": "translated", 
        "type_store": "", 
        "point": 4000000, 
        "user_id": "550025221", 
        "datetime": 1575301326
      }
    }
  ]
}
```
* `items` - Список 100 последних транзакций

### Как обращаться к остальным методам?
```python /* или python3 */
from vkpoint import VKPoint

VKPointSession = VKPoint(user_id = 123456789, token = '_tokentokentokentokentokentoken_')
VKPointMerchant = VKPointSession.GetApi()
```
**Приведу несколько примеров Топ пользователей, Топ вип пользователей и Топ по сообществам**

**Обращение к другим методам не требует вводить свой ID или access_token к примеру в методе --> callback.getUser**

**Подмечу, что только свой не нужно вводить**

**Если требуется, что-то сделать с другим пользователем, то его ID нужно ввести будет**
#### --> users.getTop
***Вывод общего топа пользователей***
```python /* или python3 */
VKPointMerchant.users.getTop(count = 100)
```
* `count` - Количество выводимых пользователей

#### --> users.getTopVip
***Вывод общего топа VIP пользователей***
```python /* или python3 */
VKPointMerchant.users.getTopVip(count = 100)
```
* `count` - Количество выводимых пользователей

#### --> groups.getTop
***Вывод топа сообществ***
```python /* или python3 */
VKPointMerchant.groups.getTop(count = 100)
```
* `count` - Количество выводимых сообществ

## Связь
[ВКонтакте](http://vk.com/krech_man)
