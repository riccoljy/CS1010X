public interface Complex { 
  public double realpart ( );        // returns this.real
  public double imagpart( );         // returns this.imag
  public double angle ( );           // returns this.angle
  public double magnitude      ( );  // returns this.mag
  public void  add   (Complex c);    // this = this + c
  public void  minus (Complex c);    // this = this - c
  public void  times (Complex c);    // this = this * c
}

