import json
from skimage import io


n = int(input('How many resolutions do you want to write down? '))
res_by_month = dict() 
img_src = 'https://static-bebeautiful-in.unileverservices.com/New%20Year%20Resolution%20for%20This%20year%20will%20be%20different.jpg'
image = io.imread(img_src)

for i in range(n):
    sent = input('Please input the number of month and your resolution ').split()
    month = int(sent[0])
    if month == 1:
      month = 'January'
    elif month == 2:
      month = 'February'
    elif month == 3:
      month = 'March'
    elif month == 4:
      month = 'April'
    elif month == 5:
      month = 'May'
    elif month == 6:
      month = 'June'
    elif month == 7:
      month = 'July'
    elif month == 8:
      month = 'August'
    elif month == 9:
      month = 'September'
    elif month == 10:
      month = 'October'
    elif month == 11:
      month = 'November'
    elif month == 12:
      month = 'December'
      
    res = sent[1:]
    if month not in res_by_month:
        res_by_month[month] = []
    res_by_month[month].append(res)


def out_red(text):
    print("\033[34m{}".format(text))
out_red('Hurray! Your list of resolutions was created!')


io.imshow(image)
io.show()

with open('resolutions2023.json', 'w') as f:
  json.dump(res_by_month, f, indent=2, sort_keys=True)


