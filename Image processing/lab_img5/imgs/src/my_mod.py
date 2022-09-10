import numpy as np
import matplotlib.pyplot as plt

def my_equalize(im):
    out = np.zeros_like(im)
    pix,c = np.unique(im,return_counts=True)
    c_sum=np.cumsum(c)
    cdf=c_sum/ar.size

    L= 2**8-1
    y=((cdf-cdf.min())/(cdf.max()-cdf.min()))*L
    y=np.round(y,0).astype(np.uint8)

    pix_map=dict(zip(pix,y))
    
    for pix,new in pix_map.items():
        idx = im == pix
        out[idx] = new
    return out



def img_show(*args, h=0):
    if args:
        number_of_imgs = len(args)
        if number_of_imgs == 1:
            if h:
                plt.hist(args[0].ravel(), bins=256)
            else:
                plt.gray()
                plt.imshow(args[0])
        else:
            f,axs = plt.subplots(1,number_of_imgs,figsize=(number_of_imgs*5,5))
            axs = axs.ravel()
            if h:
                for i,img in enumerate(args):
                    axs[i].hist(img.ravel(), bins=256)
            else:
                plt.gray()
                for i,img in enumerate(args):
                    axs[i].imshow(img)
    else:
        print("ERROR : You need to give at least on image to display")