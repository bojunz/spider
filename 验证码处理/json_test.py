aaa = {'err_no': 0, 'err_str': 'OK', 'pic_id': '2239315301283060002', 'pic_str': '159,158|242,150|158,198', 'md5': 'e2d7ff97121cd5e65e81ddfd6a6dae04'}

pic_list = [[int(j) for j in i.split(',')] for i in aaa.get('pic_str').split('|')]
print(pic_list)