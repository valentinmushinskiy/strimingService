FitnessFunction = @shufcn;
numberOfVariables = 2;

opts = optimoptions(opts,'MaxGenerations',150,'MaxStallGenerations', 100);
[x,Fval,exitFlag,Output] = ga(FitnessFunction,numberOfVariables,[],[],[], ...
    [],[],[],[],opts);

fprintf('The number of generations was : %d\n', Output.generations);
fprintf('The number of function evaluations was : %d\n', Output.funccount);
fprintf('The best function value found was : %g\n', Fval);
