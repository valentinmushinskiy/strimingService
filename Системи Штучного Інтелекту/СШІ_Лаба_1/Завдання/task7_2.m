x = 0:0.1:10;
mfparams = [1 3 5];
mftype = 'gbellmf';
y = evalmf(x,mfparams,mftype);
%
% Plot the evaluation.
plot(x,y)
xlabel('gbellmf, P = [1 3 5]')
ylim([-0.05 1.05])