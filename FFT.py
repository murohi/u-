#Aに画像をグレースケールに変換していれる
A = rgb2gray(imread('images/1-140105025213.jpg'))
imshow(A)
#plt.color()
plt.show()
#LgTransという関数を定義
def LgTrans(x):
    C = 1/log(1+1)
    return C*log(1+x)
#フーリエ変換をする
im = np.abs(np.fft.fft2(A))

h,w = im.shape
im = np.roll(im,h//2,0)
im = np.roll(im,w//2,1)

for i in range(h):
    for j in range(w):
        im[i][j] = LgTrans(im[i][j])

imshow(im, vmin=0)
plt.colorbar()
plt.show()

print("max: ",im.max())
print("min: ",im.min())
