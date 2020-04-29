I1 = imread('s9.jpg');
figure;
imshow(I1);
figure;
imhist(I1);
 
I_imadjust = imadjust(I1);
I_histeq = histeq(I1);
I_adapthisteq = adapthisteq(I1);

figure;
imshow(I_imadjust);
figure;
imhist(I_imadjust);
 
figure
imshow(I_histeq)
figure;
imhist(I_histeq);
 
figure
imshow(I_adapthisteq)
figure;
imhist(I_adapthisteq);
