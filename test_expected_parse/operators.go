package main 

func main ( ) { 
	
	var a int = 10; 
	var b int = 20; 
	var c int = 0; 
	var too bool = true ; 
	var foo bool = false ; 
	var roo bool ; 
	
	c = a + b ; 
	c = a - b ; 
	c = a * b ; 
	c = a / b ; 
	c = a % b ; 
	
	roo = ! foo ; 
	roo = too || foo ; 
	roo = foo && too ; 
	
	foo = a > b ; 
	foo = a < b ; 
	foo = a >= b ; 
	foo = a <= b ; 
	foo = a == b ; 
	foo = a != b ; 
	
	return 0; 
} 