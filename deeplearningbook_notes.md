## Chapter 4 Numerical Computation	

Machine learning algorithms usually require a hight amount of numerical computation. This typically refers to algorithms that solve mathematical problems by methods that update estimates of the solution via an iterative process, rather than analytically deriving a formula providing a symbolic expression for the correct solution. Common operations inlude optimization(finding the value of an argument that minimizes or maximizes a function) and solving systems of linear equations. Even just evaluting a mathematical function on a digital computer can be difficult when the function involves real numbers, which cannot be represented precisely using a finite amount of memory.

#### 4.1 Overflow and underflow

**Underflow:** when numbers near zeos are rounded to zero.

**Overflow**: when numberss with large magnitude are approximated as $\infin$ or $-\infin$.