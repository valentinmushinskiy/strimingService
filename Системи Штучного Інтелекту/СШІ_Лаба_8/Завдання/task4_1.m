[X,map] = imread('shadow.tif');
shadow = ind2rgb(X,map); 
shadow_lab = rgb2lab(shadow);

figure;
imshow(shadow);

max_luminosity = 100;
L = shadow_lab(:,:,1)/max_luminosity;

shadow_imadjust = shadow_lab;
shadow_imadjust(:,:,1) = imadjust(L)*max_luminosity;
shadow_imadjust = lab2rgb(shadow_imadjust);

shadow_histeq = shadow_lab;
shadow_histeq(:,:,1) = histeq(L)*max_luminosity;
shadow_histeq = lab2rgb(shadow_histeq);

shadow_adapthisteq = shadow_lab;
shadow_adapthisteq(:,:,1) = adapthisteq(L)*max_luminosity;
shadow_adapthisteq = lab2rgb(shadow_adapthisteq);

figure;
imshow(shadow_imadjust);
figure;
imshow(shadow_histeq);
figure;
imshow(shadow_adapthisteq);
