val add = (x: Int, y: Int) => "Addition is " + (x + y)

val apply_operation = (f: (Int, Int) => String, x: Int, y: Int) => f(x, y) + ", Wow!"

@main def hello(): Unit =
	println("Hello world!")
	print(apply_operation(add, 2, 3): String)