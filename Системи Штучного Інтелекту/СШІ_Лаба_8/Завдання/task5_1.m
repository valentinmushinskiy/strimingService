I = imread('coins.png');
figure
imshow(I)
title('Original Image')
h = ones(7,7)/49;
I2 = imfilter(I,h);
figure
imshow(I2)
title('Filtered Image(7*7)')
