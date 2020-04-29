rgb = imread('coloredChips.png');
imshow(rgb)

d = imdistline;
delete(d)

gray_image = rgb2gray(rgb);
imshow(gray_image)

[centers,radii] = imfindcircles(rgb,[20 25],'ObjectPolarity','dark', ...
    'Sensitivity',0.98)

imshow(rgb)
h = viscircles(centers,radii);


