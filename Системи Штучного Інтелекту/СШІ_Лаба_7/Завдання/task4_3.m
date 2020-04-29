gPosition = find(strcmp('g',b5v.ClassNames))
figure
[s,e] = mdsProx(b5v,'Colors','rb');
xlabel('First Scaled Coordinate')
ylabel('Second Scaled Coordinate')

figure
bar(e(1:20))
xlabel('Scaled Coordinate Index')
ylabel('Eigenvalue')

[Yfit,Sfit] = oobPredict(b5v);
[fpr,tpr] = perfcurve(b5v.Y,Sfit(:,gPosition),'g');
figure
plot(fpr,tpr)
xlabel('False Positive Rate')
ylabel('True Positive Rate')

[fpr,accu,thre] = perfcurve(b5v.Y,Sfit(:,gPosition),'g','YCrit','Accu');
figure(20)
plot(thre,accu)
xlabel('Threshold for ''good'' Returns')
ylabel('Classification Accuracy')

accu(abs(thre-0.5)<eps)
[maxaccu,iaccu] = max(accu)
thre(iaccu)
