# -*- coding: utf-8 -*- #
"""
Created on Thu Oct 19 21:12:19 2023

@author: ion
"""
from os.path import realpath as opr
from random import randint as r
dirpath = opr(__file__).split("/Cpkg/ConV2erter.py")[0]

def Et(T,sr):
        def TD(x): return (("0"*((len(str(x))-2)*-1)+str(x)) if len(str(x)) <= 2 and len(str(x)) > 0 else "")
        def Shift(x,sa): return ((TD((ord(x)+sa-2)%94)+"94") if ord(x)-32<0 else TD((ord(x)+sa-32)%94)) if sr == "e" else chr((ord(x)+sa-32)%94-v+32)
        En,V="",""
        if sr == "e":
            EM, OM=r(1,93), r(1,93)
            EK,OK = str((EM-1)*OM),str(94-OM)
            En = "".join(i+str(r(0,9)) for i in "".join([str(ord(i)-32) for i in EK]+["13"]+[str(ord(i)-32) for i in OK]+["13"]+[str(Shift(T[i],i*EM if i%2==0 else OM)) for i in range(len(T)-1,-1,-1)]))
            En = "".join(chr(int(Shift(chr(int(b)*10+32),a*3))+32) for a, b in enumerate(En))
        elif sr == "d":
            global v
            EM=OM=EK=OK=""
            v=c=0
            V=[str(int(((ord(Shift(d,c*-3)))-32)/10)) for c,d in enumerate(T)]
            T="".join(chr(int(b+V[a+2])+32) for a,b in enumerate(V) if a%4==0)
            del V
            for i in T:
                if i == chr(45):break
                else:EK += i
            for i in T[len(EK)+1:]: 
                if i == chr(45):break
                else:OK += i
            OM = 94-int(OK)
            EM,T=int(int(EK)/OM+1),T[(len(EK)+len(OK)+2):]
            for i in range(len(T)):
                if T[len(T)-i-1]==chr(126):v+=30;c+=1;continue
                En,v = str(En)+str(Shift(T[len(T)-i-1],0-((i-c)*EM if (i+c)%2 == 0 else OM))),0
        if sr in ("e","d"):return En
            
def Run(T,M):
    global sr
    sr=M[0].lower()
    k = int(str(ord(T[-2])-3)[-1]) if sr == "d" else r(1,3)
    if sr == "d":T = T[:-2]
    for i in range(k):T=Et(T,sr)
    if sr == "e":T+=chr(r(3,12)*10+k+3)+chr(r(32,126))
    return T
    
def Start(text="",selector=""):
    b=text
    o=False
    try:return Run(text,selector)
    except KeyboardInterrupt:o=True;print("\nSee you soon!")
    except Exception as e:
        if not o:
            from sys import exc_info
            from traceback import extract_tb
            print("An unexpected error occured.\n\nLogging error...")
            l = extract_tb(exc_info()[-1])[-1][1]
            try:
                with open(f"{dirpath}/Cpkg/ErrorLogs.txt","a") as L:
                        L.write(f" T '{b}' in mode '{selector}' caused '{e}' line {l}.\n")
                        print(f"Error successfully saved to {dirpath}/Cpkg/ErrorLogs.txt.")
            except Exception as e: print("Unable to log error:",e)
