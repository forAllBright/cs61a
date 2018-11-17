>This example illustrates two related big ideas in computer science. First, naming and functions allow us to abstract away a vast amount of complexity. While each function definition has been trivial, the computational process set in motion by our evaluation procedure is quite intricate. Second, it is only by virtue of the fact that we have an extremely general evaluation procedure for the Python language that small components can be composed into complex processes. Understanding the procedure of interpreting programs allows us to validate and inspect the process we have created.
* 在函数嵌套调用中，将函数作为返回实际上返回的是一种运算规则，分析时从外
层到内层的分析，不断的返回，再去调用这个返回，然后悔再返回一个函数，再去
调用...，但外层的参数在内层函数调用时是可以使用的，这意味着内层返回函数
调用时能将外层传入的参数直接使用。对于一个内层函数只考虑外层的影响，不必
去考虑它内层的函数。