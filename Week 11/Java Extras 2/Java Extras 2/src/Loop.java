public class Loop {
    public static void main(String[] args) {
        int i;

        i = 1;
        while (true) {
            i--;

            if (i < - 2147483645 | i > 2147483645) System.out.println(i);
        }

    }

}