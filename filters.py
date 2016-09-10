import datetime

def ts2readable(ts):
    if ts:
        dt = datetime.datetime.fromtimestamp(int(ts))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return None
