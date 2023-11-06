class TestReverse_3 {
  public static void printArray( int[] x){
    for (int i=0; i < x.length; i++) 
      System.out.print(x[i]+" ");
    System.out.println();
  }
  
  /* method #3: not good, but here to illustrate conditional statement */
  public static void reverseArray_3 (int[] x){
    int size = x.length;
    for (int i=0; i < size; i++) {
      if (i >= size/2)
        break;
      int tmp = x[i];
      x[i] = x[size-i-1];
      x[size-i-1] = tmp;
    }   
  }
  
  public static void main(String [] args) {  
    int[] u = {1,2,3,4,5,6,7};
    reverseArray_3(u);
    printArray(u);
  }
} // end of class