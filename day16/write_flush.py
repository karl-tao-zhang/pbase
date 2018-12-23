# write_flush.py



f = open('myflush.txt', 'w')

f.write('我是第一行数据')
f.flush()    #把缓冲区的内容直接写到磁盘上
s = input("暂停中．．．")
f.write('我是第二行数据')
f.close()
