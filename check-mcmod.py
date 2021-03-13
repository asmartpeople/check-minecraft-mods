import requests as r
from bs4 import BeautifulSoup
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#检查是否要重新输入数据
if os.path.exists('first-time.txt')==True:
    reload=str(input('是否要重新更新数据(y/n):'))
    #重新更新数据
    if reload=='y':
        print('正在打开TXT')
        cfr=open('fr-data.txt','w',encoding='utf-8')
        print('成功打开TXT')

        count=1
        weicount=0
        print('正在输入数据中...')
        for i in range(7000):

            url = r.get('https://www.mcmod.cn/class/'+str(count)+'.html')
            soup = BeautifulSoup(url.content, 'html.parser',from_encoding='utf-8')
            detials = str(soup.select('title')[0].text)
            if detials[0] != '出':
                cfr.write(str(count)+'-->'+str(detials))  # 写入
                cfr.write('\n')
                count+=1
                weicount=0
            else:
                count+=1
                weicount+=1
                if weicount==5:
                    break
                continue


        print('数据已经更新完成，请重启程序！')
    else:
        pass
else:
    print('欢迎使用本软件，这款软件使用必须在联网的状态下运行')
    print('此款软件支持')







