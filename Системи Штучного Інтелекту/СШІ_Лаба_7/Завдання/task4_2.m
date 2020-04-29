b5v = fillProximities(b5v);
figure
histogram(b5v.OutlierMeasure)
xlabel('Outlier Measure')
ylabel('Number of Observations')

extremeOutliers = b5v.Y(b5v.OutlierMeasure>40)
percentGood = 100*sum(strcmp(extremeOutliers,'g'))/numel(extremeOutliers)