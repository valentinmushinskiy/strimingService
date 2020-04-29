I1 = imread('11_0.jpg');

I_adapthisteq = adapthisteq(I1);
I_imadjust = imadjust(I_adapthisteq);
I_histeq = histeq(I_imadjust);
I_imadjust = imadjust(I_histeq);
I_adapthisteq = adapthisteq(I_histeq);

figure;
imshow(I_adapthisteq);
imhist(I_adapthisteq);