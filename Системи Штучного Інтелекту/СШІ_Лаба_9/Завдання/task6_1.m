he=imread('C9.png');
imshow(he), title('H&E изображение');

cform=makecform('srgb2lab');
lab_he=applycform(he, cform);

ab=double(lab_he(:, :, 2:3));
nrows=size(ab, 1);
ncols=size(ab, 2);
ab=reshape(ab, nrows*ncols, 2);
nColors=3;
[cluster_idx, cluster_center]=kmeans(ab, nColors, 'distance', 'sqEuclidean','Replicates',3);

pixel_labels=reshape(cluster_idx, nrows,ncols);
imshow(pixel_labels, []), title('изображение, отмеченное кластерными индексами');

segmented_images=cell(1, 3);
rgb_label=repmat(pixel_labels, [1 1 3]);
for k=1 : nColors
  color=he;
  color(rgb_label~=k)=0;
  segmented_images{k}=color;
end
imshow(segmented_images{1}), title('объекты в кластере 1');

imshow(segmented_images{2}), title('объекты в кластере 2');

imshow(segmented_images{3}), title('объекты в кластере 3');
