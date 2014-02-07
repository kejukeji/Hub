# coding: UTF-8

def out_image_name():
    '''输出奶粉图片名字'''
    count = 0
    while True:
        temp_count = str(count)
        temp_len = len(temp_count)
        if temp_len == 1:
            print "<img src='/static/images/milk/金装爱儿加奶粉罐_000"+ str(temp_count)+".png'>"
        if temp_len == 2:
            print "<img src='/static/images/milk/金装爱儿加奶粉罐_00"+ str(temp_count)+".png'>"
        if temp_len == 3:
            print "<img src='/static/images/milk/金装爱儿加奶粉罐_0"+ str(temp_count)+".png'>"

        if count >= 100:
            break
        count = count + 1

if __name__ == '__main__':
    out_image_name()