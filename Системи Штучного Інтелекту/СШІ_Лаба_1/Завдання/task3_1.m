x = 0:0.1:10;
y = zmf(x,[3 7]);
plot(x,y)
xlabel('zmf, P = [3 7]')
ylim([-0.05 1.05])
