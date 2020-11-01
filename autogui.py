#import pyautogui as pg
#print(dir(pg))
N=(int(input())%86400)
print(N//3600,":",(N-N%3600)//60 ,":",(N-N%3600)%60)