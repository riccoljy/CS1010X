class TestReverse_1 {
  
  public static void main(String [] args) {  
    int[] u = new int[] {1,2,3,4,5,6, 7};
    int size = u.length;
    for (int i=0; i < size/2; i++) {
      int tmp = u[i];
      u[i] = u[size-i-1];
      u[size-i-1] = tmp;
    }   
    
    for (int i=0; i < u.length; i++) 
      System.out.print(u[i]+" ");
    System.out.println();
    
  }
} // end of class