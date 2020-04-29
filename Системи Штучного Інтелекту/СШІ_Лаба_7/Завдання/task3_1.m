t = fitctree(meas(:,1:2), species,'PredictorNames',{'SL' 'SW' });

[grpname,node] = predict(t,[x y]);
gscatter(x,y,grpname,'grb','sod')

view(t,'Mode','graph');

dtResubErr = resubLoss(t)

cvt = crossval(t,'CVPartition',cp);
dtCVErr = kfoldLoss(cvt)
