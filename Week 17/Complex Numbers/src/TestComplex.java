class TestComplex {
  public static void main(String [] args) {
    // Testing ComplexCart
    Complex a = new ComplexCart(10.0, 12.0);
    Complex b = new ComplexCart(1.0, 2.0); 
    a.add(b);
    System.out.println("a=a+b is " +  a );
    a.minus(b);
    System.out.println("a-b (which is the original a) is " + a); 
    System.out.println("Angle of a is " + a.angle()); 
    a.times(b);
    System.out.println("a x b is " + a);   
    
    // Testing ComplexPolar
    Complex c = new ComplexPolar(10.0,Math.PI/6.0);
    Complex d = new ComplexPolar(10.0,Math.PI/3.0);
    System.out.println("c is " +  c);
    System.out.println("d is " +  d);
    c.add(d);
    System.out.println("c=c+d is " +  c);
    c.minus(d);
    System.out.println("c-d (which is the original c) is " + c);
    c.times(d);
    System.out.println("c=c*d is " + c);
    
    // Testing Combine
    System.out.println("a is " + a );
    System.out.println("d is " + d );
    a.minus(d);
    System.out.println("a=a-d is " + a);
    a.times(d);
    System.out.println("a=a*d is " + a);
    d.add(a);
    System.out.println("d=d+a is " + d);
    d.times(a);
    System.out.println("d=d*a is " + d);
  }
}

