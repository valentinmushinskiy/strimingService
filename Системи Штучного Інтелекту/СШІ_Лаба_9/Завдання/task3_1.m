rgb = imread('R9.png');
imshow(rgb)

hBright = viscircles(centersBright, radiiBright,'Color','b');

[centersBright,radiiBright,metricBright] = imfindcircles(rgb,[30 35], ...
    'ObjectPolarity','bright','Sensitivity',0.97,'EdgeThreshold',0.1);

delete(hBright)
hBright = viscircles(centersBright, radiiBright,'Color','b');

h = viscircles(centers,radii);