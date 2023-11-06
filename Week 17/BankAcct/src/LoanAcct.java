//Subclass
class LoanAcct extends BankAcct {
    protected double _rate;
    protected double _limit;

    public LoanAcct(int aNum, double bal, double rate, double limit) {
        // Write your code here
        super(aNum, bal);

        _rate = rate;
        _limit = limit;
    }

    //New method in subclass
    public void payInterest() {
        // Write your code here
        _balance += _balance * _rate;

    }

    //Method Overriding
    public boolean withdraw(double amount) {
        // Write your code here
        if (((-_balance) + amount) <= _limit){
            _balance -= amount;
            return true;
        }
        return false;
    }

    public void deposit(double amount) {
        // Write your code here
        if (amount <= 0) return;
        _balance += amount;
    }

    public boolean transfer(BankAcct fromAcct, BankAcct toAcct, double amount) {
        if (fromAcct.withdraw(amount)) {
            toAcct.deposit(amount);
            return true;
        }
        return false;
    }
}

