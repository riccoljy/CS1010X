class BankAcct
{
  protected int _acctNum;
  protected double _balance; 
  //Constructors
  public BankAcct( ) {   
    //initialize all attributes to 0
  }
  public BankAcct( int aNum, double bal ) {
    //initialize attributes with user provided values
    _acctNum = aNum;
    _balance = bal;
  }
  
  //Methods
  public boolean withdraw( double amount ) {   
    if ( _balance < amount )
      return false;    
    _balance -= amount;
    return true;            
  }

  public void deposit( double amount ) {
    if ( amount <= 0 )
      return; 
    _balance += amount;
  }
 
  public void print() {
    System.out.println( "Account Number: " + _acctNum );
    System.out.printf( "Balance: $%.2f\n", _balance );
  }
}

