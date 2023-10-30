import pandas as pd

# 示例数据
data = {
    'date_strings': ['2023-10-21', '2023-10-22', '2023-10-23'],
    'timestamp_seconds': [1603267200, 1603353600, 1603440000],
    'timestamp_milliseconds': [1603267200000, 1603353600000, 1603440000000]
}

df = pd.DataFrame(data)

# 将字符串表示的日期转换为 Pandas 日期时间
df['date_from_strings'] = pd.to_datetime(df['date_strings'])

# 将整数表示的秒级时间戳转换为 Pandas 日期时间
df['date_from_seconds'] = pd.to_datetime(df['timestamp_seconds'], unit='s')

# 将整数表示的毫秒级时间戳转换为 Pandas 日期时间
df['date_from_milliseconds'] = pd.to_datetime(df['timestamp_milliseconds'], unit='ms')

print(df)
