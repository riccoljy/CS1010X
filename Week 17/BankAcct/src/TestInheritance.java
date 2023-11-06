class TestInheritance
{
  public static void main( String[] args ) {
    SavingAcct sa1 = new SavingAcct( 2, 1000.0, 0.03 );
    sa1.print();
    sa1.withdraw( 50.0 );
    sa1.payInterest();
    sa1.print();
    
    BankAcct ba = new BankAcct(1234, 99.99);
    ba.print();
    ba = sa1;
    // ba.payInterest(); // can't do this
    ba.print(); // interest rate is also printed
  }
} 
