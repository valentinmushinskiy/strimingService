function y = parameterized_fitness(x,a,b)
    y = a * (x(1)^2 - x(2)) ^2 + (b - x(1))^2; 
