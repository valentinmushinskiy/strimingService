he=imread('hestain.png');
imshow(he), title('H&E изображение');
text(size(he, 2),size(he, 1)+15,'Image courtesy of Alan Partin, Johns Hopkins University', 'FontSize',7,'HorizontalAlignment','right');

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

mean_cluster_val=zeros(3, 1);
for k=1:nColors
  mean_cluster_val(k)=mean(cluster_center(k));
end
[mean_cluster_val,idx]=sort(mean_cluster_val);
blue_cluster_num=idx(2);
L=lab_he(:, :, 1);
blue_idx=find(pixel_labels==blue_cluster_num);
L_blue=L(blue_idx);
is_light_blue=im2bw(L_blue,graythresh(L_blue));

nuclei_labels=repmat(uint8(0), [nrows ncols]);
nuclei_labels(blue_idx(is_light_blue==false))=1;
nuclei_labels=repmat(nuclei_labels, [1 1 3]);
blue_nuclei=he;
blue_nuclei(nuclei_labels~=1)=0;
imshow(blue_nuclei), title('синие ядра');

