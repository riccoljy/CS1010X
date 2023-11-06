import java.util.Scanner;

public class Counting {
    public static void main(String[] args) {
        int i, n;
        int count2 = 0, count3 = 0, count5 = 0;
        Scanner in = new Scanner(System.in);

        n = in.nextInt();

        for (i = 0; i <= n; i=i+1)
        {
            if (i%5 == 0)
            {
                count5 = count5 + 1;
                if (i%3 == 0)
                    count3 = count3 + 1;
            }
            else
            {
                if (i%2 == 0)
                    count2 = count2 + 1;
            }
        }
        System.out.println((n/5+1) + " " + (n/15+1) + " " + (n/2-n/10));
        System.out.printf("%d %d %d\n", count5, count3, count2);
    }
}