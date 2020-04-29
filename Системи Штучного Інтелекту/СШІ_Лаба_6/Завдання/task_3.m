FitnessFunction = @shufcn;
numberOfVariables = 2;

opts = optimoptions(@ga,'PlotFcn',{@gaplotbestf,@gaplotstopping});
opts.PopulationSize = 10;
Population = rand(3,2);
opts.InitialPopulationRange = [-1 0; 1 2];
[x,Fval,exitFlag,Output] = ...
    ga(FitnessFunction,numberOfVariables,[],[],[],[],[],[],[],opts);


fprintf('The number of generations was : %d\n', Output.generations);
fprintf('The number of function evaluations was : %d\n', Output.funccount);
fprintf('The best function value found was : %g\n', Fval);
