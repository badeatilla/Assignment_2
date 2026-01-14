class time:
    def _init_(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def print_time(t):
    print(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}")

def time_to_int(t):
    minutes=t.hour*60 + t.minute
    seconds=minutes*60 + t.second
    return seconds

def int_to_time(seconds):
    t=Time()
    minutes, t.second = divmod(seconds,60)
    t.hour, t.minute = divmod(minutes,60)
    return t

def is_after(t1,t2):
    return time_to_int(t1) > time_to_int(t2)

saat1 = time(9 , 5 , 2)
saat2 = time(8 , 21 , 7)

print_time(saat1)

print("/n1. Saatin toplam saniyesi:")
saniye = time_to_int(saat1)
print(saniye)
