rng(0,'twister');
cp = cvpartition(species,'KFold',10)

cvlda = crossval(lda,'CVPartition',cp);
ldaCVErr = kfoldLoss(cvlda)

cvqda = crossval(qda,'CVPartition',cp);
qdaCVErr = kfoldLoss(cvqda)
