# coding: UTF-8

def out_image_name():
    '''输出奶粉图片名字'''
    count = 100
    while True:
        temp_count = str(count)
        temp_len = len(temp_count)
        if temp_len == 1:
            print "<img src='/static/images/golds/000"+ str(temp_count)+".png'>"
        if temp_len == 2:
            print "<img src='/static/images/golds/00"+ str(temp_count)+".png'>"
        if temp_len == 3:
            print "<img src='/static/images/golds/0"+ str(temp_count)+".png'>"

        if count <= 0:
            break
        count = count - 1




if __name__ == '__main__':
    out_image_name()
    #import Image
    #import glob, os
    #dir_outpath=r'/Users/K/Documents/Plugin/huishi/golds//'
    #size = 640, 380
    #for files in  glob.glob(r'/Users/K/Documents/Plugin/huishi/s/*.png'):
    #    #print files
    #    filepath,filename = os.path.split(files)
    #    filterame,exts = os.path.splitext(filename)
    #    #print filepath,'/n',filename,'/n',filterame,'/n',exts
    #    if(os.path.isdir(dir_outpath)==False):
    #        os.mkdir(dir_outpath)
    #        print 'make dir:',dir_outpath
    #    im=Image.open(files)
    #    w,h=im.size
    #    im.thumbnail(size,Image.ANTIALIAS)
    #    temp_name = filterame.split('_')[1]
    #    #im_s.show()
    #    im.save(dir_outpath+temp_name+'.png')
    #    print dir_outpath+temp_name+'.png'
    #print 'ok!'
