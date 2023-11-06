class TestReverse_4 {
  public static void printArray( int[] x){
    for (int i=0; i < x.length; i++) 
      System.out.print(x[i]+" ");
    System.out.println();
  }
  
  /* method #1 */
  public static void reverseArray_r(int[] x){
    reverse_r(x, 0, x.length - 1);
  }
  // have to recurse from both ends to avoid using extra array
  public static void reverse_r (int[] x, int i, int j){
    if(i<j){//Swap
      int tmp = x[i];
      x[i] = x[j];
      x[j] = tmp;
      reverse_r(x, ++i, --j);//Recursive
    }   
  }
    
  public static void main(String [] args) {  
    int[] s = {1,2,3,4,5,6,7};    
    reverseArray_r(s);
    printArray(s);    
  }
} // end of class