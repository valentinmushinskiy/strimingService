I = imread('c2.png');

h = ones(7,7)/49;
I2 = imfilter(I,h);
figure
imshow(I2)
title('Filtered Image')
imwrite (I2, 'c2_filtered.png');