x = 0:0.1:10;
y = gaussmf(x,[2 5]);
plot(x,y)
xlabel('gaussmf, P=[2 5]')
ylim([-0.05 1.05])