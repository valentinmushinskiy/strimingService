x = 0:0.1:10;
y = gaussmf(x,[1 4]);
plot(x,y)
xlabel('gaussmf, P=[4 1]')
ylim([-0.05 1.05])