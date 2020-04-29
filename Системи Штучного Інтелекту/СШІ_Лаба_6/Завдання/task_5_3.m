FitnessFunction = @(x) vectorized_fitness(x,100,1);
numberOfVariables = 2;
options = optimoptions(options,'UseVectorized',true);
[x,fval] = ga(FitnessFunction,numberOfVariables,[],[],[],[],[],[],[],options)
