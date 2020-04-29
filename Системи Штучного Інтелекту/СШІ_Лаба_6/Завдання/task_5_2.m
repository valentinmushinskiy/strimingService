a = 100; b = 1; % define constant values
FitnessFunction = @(x) parameterized_fitness(x,a,b);
numberOfVariables = 2;
[x,fval] = ga(FitnessFunction,numberOfVariables)  
