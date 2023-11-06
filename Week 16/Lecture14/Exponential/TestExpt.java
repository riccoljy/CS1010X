class TestExpt {
 
  float expt(float x, int n){
    if (n==0)
      return 1;
    else {
      return x * expt(x, n-1);
    }
  }
  
  public static void main(String [] args) {  
    TestExpt a = new TestExpt();
    System.out.println(a.expt((float)5.3,4));
  } 
}