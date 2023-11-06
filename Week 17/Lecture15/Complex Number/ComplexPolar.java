class ComplexPolar implements Complex {
  private double mag;   // magnitude
  private double ang;   // angle
  // CONSTRUCTORS
  ComplexPolar (double m, double r) { mag = m; ang = r; } 

  // ACCESSORS
  public double realpart ()  { return mag * Math.cos(ang); }
  public double imagpart ()  { return mag * Math.sin(ang); }   
  public double magnitude () { return mag; }
  public double angle ()     { return ang; }
  
  // MUTATORS
  public void add (Complex c)   {     // this = this + c
    double real =  realpart() + c.realpart();
    double imag =  imagpart() + c.imagpart(); 
    mag = Math.sqrt(real*real + imag*imag);
    if (real != 0) { 
      if (real < 0) ang = (Math.PI + Math.atan(imag/real));
      else ang = Math.atan(imag/real);
    }
    else if (imag == 0) ang = 0;
    else if(imag > 0) ang = Math.PI/2;
    else ang = -Math.PI/2;
  }
  
  public void minus (Complex c)   {     // this = this - c
    double real =  mag * Math.cos(ang) - c.realpart(); 
    double imag =  mag * Math.sin(ang) - c.imagpart();
    mag = Math.sqrt(real*real + imag*imag);
    if (real != 0) { 
      if (real < 0) ang = (Math.PI + Math.atan(imag/real));
      else ang = Math.atan(imag/real);
    }
    else if (imag == 0) ang = 0;
    else if(imag > 0) ang = Math.PI/2;
    else ang = -Math.PI/2;
  }
  
  public void times (Complex c)  {   // this = this * c
    mag *= c.magnitude(); 
    ang += c.angle();
    ang = ang % (2*Math.PI); // maintain ang within 2*pi 
  }
  
  public String toString() {
    if ( imagpart() == 0 ) return ( this.realpart() + "");
    else if ( imagpart() < 0 ) 
      return ( realpart() + "" + imagpart() + "i");
    else 
      return ( realpart() + "+" + imagpart() + "i");
  }
  
}  

