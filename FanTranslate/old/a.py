
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger("aaa")
    logger.error("111")

    f=open("D:/printlog/aa.txt",'a')

    print("asdadsa",file=f)
    print("asdadsa",file=f)
    print("asdadsa",file=f)
    print("asdadsa",file=f)
    print("asdadsa",file=f)
    print("asdadsa",file=f)
    print("asdadsa",file=f)

    pass