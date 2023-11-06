class TestBankAcct
{
  public static void transfer (BankAcct fromAcct, 
                               BankAcct toAcct, double amt) 
  {
    if (fromAcct.withdraw(amt))
      toAcct.deposit(amt);
    else
      System.out.println("Money not enough");
  }
  public static void main( String[] args )
  {
    /*BankAcct ba1 = new BankAcct();
    BankAcct ba2 = new BankAcct(1234, 99.99);

    ba1._acctNum = 1;

    ba1.deposit( 1000 );
    ba2.withdraw( 50.25 );      
    transfer( ba1, ba2, 50.0);
    System.out.println("printing ba1");
    ba1.print();  
    System.out.println("printing ba2");
    ba2.print();
    transfer( ba2, ba1, 100);
    System.out.println("printing ba1");
    ba1.print();
    System.out.println("printing ba2");
    ba2.print();  */

    LoanAcct la = new LoanAcct(1, -100, 0.1, 120);
    SavingAcct sa = new SavingAcct(1, 100, 0.1);
    System.out.println("Before transferring,");
    System.out.println("LoanAcct:" );
    la.print();
    System.out.println("SavingAcct:" );
    sa.print();

    transfer(sa, la, 13);
    System.out.println("After transferring,");
    System.out.println("LoanAcct:" );
    la.print();
    System.out.println("SavingAcct:" );
    sa.print();

  }
} 
