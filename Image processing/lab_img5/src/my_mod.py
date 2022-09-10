import numpy as np
import matplotlib.pyplot as plt

def my_equalize(im):
    out = np.zeros_like(im)
    pix,c = np.unique(im,return_counts=True)
    c_sum=np.cumsum(c)
    cdf=c_sum/im.size

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

"""def convol_img(ar,kernel):
    out = ar.copy()
    #pad = kernel.shape[0]
    ar_con = np.pad(ar, pad)
    aux_row = kernel[0].shape[0]
    aux_col = kernel[1].shape[0]
    for row in range(pad, ar_con.shape[0]-aux_row):
        for col in range(1, ar_con.shape[1]-aux_col):
            window = ar_con[row-1:row+aux_row-1, col-1:col+aux_col-1]
            new_pixel = kernel_multi(kernel, window)
            out[row-1, col-1] = new_pixel
    return out
"""
def kernel_multi(kernel, ar):
    ker = kernel.copy()
    window = ar.copy()
    kernel_sum = ker.sum()

    if kernel_sum == 0:
        kernel_sum = 1
    
    res = (kernel * window).sum() / kernel_sum
    return int(res)

    
def my_convolution(im, kernel):
    out = im.copy()
    kernel = kernel.copy()

    pad = int((kernel.shape[0] - 1) / 2)
    im = im.pad(im, pad)
    
    for row in range(pad, im.shape[0] - pad):
        for col in range(pad, im.shape[1] - pad):
            window = im[row - pad:row + pad + 1, col - pad:col + pad + 1]
            new_pixel = kernel_multi(kernel, window)
            out[row - pad, col - pad] = new_pixel
    return out
