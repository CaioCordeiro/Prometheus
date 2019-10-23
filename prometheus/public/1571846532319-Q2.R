tempfn3 <- function(x,n ){
  sum<- 0
  for(i in 1:n){
    if(i==1){
      sum<- 1+ x/1
    }else{
      sum<- sum + ((x**i)/i)
    }
    
  }
  return(sum)
}

a<- tempfn3(2,2)