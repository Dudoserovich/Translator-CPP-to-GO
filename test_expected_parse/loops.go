package main 

func main ( ) { 
	var c int = 10; 
	var r int = 0; 
	
	for i := 1; i <= 5; i = i + 1{ 
		r = r + 1; 
	} 
	
	for r <= 20{ 
		r = r + 1; 
	} 
	
	for ok := true; ok; ok = (r<=30) { 
		r = r + 1; 
	} 
	
	
	return 0; 
} 