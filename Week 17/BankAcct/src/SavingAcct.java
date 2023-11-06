//Subclass
class SavingAcct extends BankAcct
{
  protected double _rate;
  public SavingAcct(int aNum, double bal, double rate) {
    super( aNum, bal );
    _rate = rate;
  }
  
  //New method in subclass
  public void payInterest()
  {
    _balance += _balance * _rate;
  }
  
  //Method Overriding
  public void print( ) {
    super.print();
    System.out.printf( "Interest: %.2f\n", _rate );
  }
}

