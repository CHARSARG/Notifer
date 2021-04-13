from notifypy import Notify
lines = []
with open('notify.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    #print(f'{count},{line}')
    text=f'{count},{line}'
    split_text = text.split(',')
    #print(split_text)
    if split_text[0] == '1':
        title=split_text[1]
    if split_text[0] == '2':
        subtitle=split_text[1]
def noti123(title,subtitle):
    notification = Notify()
    notification.title = title
    notification.message = subtitle
    notification.send()
noti123(title,subtitle)
