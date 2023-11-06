public interface Complex {
    public double realpart ( );        // returns this.real
    public double imagpart( );         // returns this.imag
    public double angle ( );           // returns this.angle
    public double magnitude      ( );  // returns this.mag
    public void  add   (Complex c);    // this = this + c
    public void  minus (Complex c);    // this = this - c
    public void  times (Complex c);    // this = this * c
    public void  divides(Complex c);
    public Complex conjugate();

    public static void main(String[] args){
        Complex c3plus4i = new ComplexCart(3,4);
        Complex c5plus6i = new ComplexCart(5,6);
        c3plus4i.divides(c5plus6i);
        System.out.println(c3plus4i);
    }
}

class ComplexCart implements Complex {
    private double real;
    private double imag;
    // CONSTRUCTORS
    public ComplexCart (double r, double i) { real = r; imag = i; }

    // ACCESSORS
    public double realpart ()  {  return this.real; }
    public double imagpart ()  { return this.imag; }
    public double magnitude () { return Math.sqrt(real * real + imag * imag); }
    public double angle ()  {
        if (real != 0) {
            if (real < 0 ) return (Math.PI + Math.atan(imag/real));
            return Math.atan(imag / real);
        }
        else if (imag == 0) return 0;
        else if (imag > 0) return Math.PI/2;
        else return -Math.PI/2;
    }

    // MUTATORS
    public void add (Complex c)  {
        this.real += c.realpart();
        this.imag += c.imagpart();
    }

    public void minus (Complex c)   {
        this.real -= c.realpart();
        this.imag -= c.imagpart();
    }

    public void times (Complex c)   {
        double tempReal=real*c.realpart() - imag*c.imagpart();
        imag = real * c.imagpart() + imag * c.realpart();
        real = tempReal;
    }

    public void divides (Complex c) {
        // Write your code here
        Complex denom = new ComplexCart(c.realpart(), c.imagpart());
        denom.times(denom.conjugate()); // which should equal real^2 + imag^2

        this.times(c.conjugate());

        //denom is a real number, hence only taking the real part
        //ie denom = a + bi, where b = 0
        real /= denom.realpart();
        imag /= denom.realpart();
    }

    public Complex conjugate (){
        return new ComplexCart(real, -imag);
    }

    // for printing...
    public String toString() {
        if ( imag == 0 ) return ( realpart() + "");
        else if ( imag < 0 )
            return ( real + "" + imag + "i");
        else
            return ( real + "+" + imag + "i");
    }
}

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

    public void divides (Complex c) {
        // Write your code here
        mag /= c.magnitude();
        ang -= c.angle();
    }

    public Complex conjugate(){
        return new ComplexPolar(mag, -ang);
    }

    public String toString() {
        if ( imagpart() == 0 ) return ( this.realpart() + "");
        else if ( imagpart() < 0 )
            return ( realpart() + "" + imagpart() + "i");
        else
            return ( realpart() + "+" + imagpart() + "i");
    }
}
