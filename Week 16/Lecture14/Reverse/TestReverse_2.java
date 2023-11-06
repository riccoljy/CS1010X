class TestReverse_2 {
  public static void printArray( int[] x){
    for (int i=0; i < x.length; i++) 
      System.out.print(x[i]+" ");
    System.out.println();
  }

  /* method #2 */
  public static void reverseArray_i (int[] x){
    int size = x.length;
    for (int i=0; i < size/2; i++) {
      int tmp = x[i];
      x[i] = x[size-i-1];
      x[size-i-1] = tmp;
    }   
  }

  public static void main(String [] args) {  
    int[] t = {1,2,3,4,5,6,7};
    reverseArray_i(t);
    printArray(t);
  }
} // end of class