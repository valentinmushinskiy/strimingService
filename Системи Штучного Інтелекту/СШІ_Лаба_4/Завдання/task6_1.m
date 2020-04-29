x = iris_dataset;
size(x);

net = selforgmap([9 9]);
view(net)

[net,tr] = train(net,x);
nntraintool

y = net(x);
cluster_index = vec2ind(y);

plotsomplanes(net)
