import datetime
import urllib3


# apiが止まってたとき用に一応土日判定だけする
def is_weekend():
    weekno = datetime.datetime.today().weekday()
    # 5=sat, 6=sunなので
    return weekno >= 5


check_holiday_url = "https://s-proj.com/utils/checkHoliday.php"


def is_holiday():
    http = urllib3.PoolManager()
    r = http.request('GET', check_holiday_url)
    if r.status == 200:
        api_data = r.data.decode()
        if api_data == "error":
            return is_weekend()
        return api_data == "holiday"
    else:
        return is_weekend()

