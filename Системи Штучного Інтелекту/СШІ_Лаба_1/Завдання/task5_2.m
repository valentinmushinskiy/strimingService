x = 0:0.1:10;
y = pimf(x,[1 3 5 8]);
plot(x,y)
xlabel('pimf, P = [1 3 5 8]')
ylim([-0.05 1.05])
