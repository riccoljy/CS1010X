public class ArithmeticSum {
    public int getSum(int n) {
        // TODO: Your code here
        int res = 0;
        int x = 0;

        for (int i = 0; i <= n; i++)
            res += i;

        return res;
    }

    public static void main(String[] args) {
        double res = new ArithmeticSum().getPi(1.0E-2);
        System.out.println(new ArithmeticSum().getApproxPi(201));
        System.out.println(res);
    }

    public int getMoreSum(int n) {
        // TODO: Your code here
        int res = 0;
        int i = 1;

        while (i <= n) {
            res += i * 2 - 1;
            i += 1;
        }
        return res;
    }

    public int getAltSum(int n) {
        // TODO: Your code here
        int res = 0;
        int i = 1;

        while (i <= n) {
            if (i % 2 == 1) res += 2 * i - 1;
            else res -= 2 * i - 1;
            i++;
        }
        return res;
    }

    public double getApproxPi(int n) {
        // TODO: Your code here
        int numer = 4;
        double res = 0;

        for (int i = 1; i <= n; i++){
            int denom = i * 2 - 1;
            if (i % 2 == 1) res += (double) numer/denom;
            else res -= (double) numer/denom;
        }
        return res;
    }

        public double getPi(double t) {
            double prevPi = 4;
            double currPi = prevPi - (double) 4/3;
            double diff = Math.abs(prevPi - currPi);
            int i = 3;
            while (diff > t){
                prevPi = currPi;
                if (i % 2 == 1) currPi += (double) 4/(i * 2 - 1);
                else currPi -= (double) 4/(i * 2 - 1);
                diff = Math.abs(currPi - prevPi);
                i++;
            }
            return currPi;
        }
    }
