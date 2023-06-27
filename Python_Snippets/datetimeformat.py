""" datetime formatting """

from datetime import datetime

now = datetime.now()
print(f'{now}')
print(f'will return date: {now:%d}')
print(f'will return month: {now:%m}')
print(f'will return year: {now:%Y}')
print(f'will return datetime {now:%d/%m/%Y %H:%M:%S}')
